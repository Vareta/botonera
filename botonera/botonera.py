import os

import discord
import logging

from discord.ext import commands
from dotenv import load_dotenv
from sounds import library

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

logging.basicConfig(level=logging.INFO)


class DiscordBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        library = kwargs.pop('library')
        super().__init__(*args, **kwargs)
        if not library:
            raise AttributeError('el bot no puede iniciar sin una biblioteca de sonidos')
        self.set_library(library)

    def set_library(self, library):
        """
        Carga una librería de sonidos en el bot
        """
        if getattr(self, 'library', False):
            for name in self.library.keys():
                self.remove_command(name)
        self.library = library
        for key, value in self.library.items():
            command = commands.Command(self.play_name, name=key, help=value['desc'])
            self.add_command(command)

    async def play_name(self, ctx, *args, **kwargs):
        """
        Busca el nombre del comando en la biblioteca de sonido y lo reproduce
        """
        name = ctx.command.name
        sound_path = self.library[name]['path']
        if self.is_user_connected(ctx):
            await self.play(ctx, sound_path)

    def is_user_connected(self, ctx):
        """
        Indica si el autor del mensaje está conectado al chat por voz
        """
        if ctx.author.voice is None or ctx.author.voice.channel is None:
            return False
        return True

    async def play(self, ctx, sound_path):
        """
        El bot se mueve al canal de voz del usuario que envió el mensaje y
        reproduce el sonido apuntado por `sound_path`
        """
        author_channel = ctx.author.voice.channel
        voice_client = discord.utils.get(self.voice_clients, guild=author_channel.guild)
        if voice_client:
            if voice_client.channel != author_channel:
                await voice_client.move_to(author_channel)
        else:
            voice_client = await author_channel.connect()
        if not voice_client.is_playing():
            voice_client.play(discord.FFmpegPCMAudio(sound_path))
    
    async def on_voice_state_update(self, member, before, after):
        """
        El bot abandona el canal de voz al quedarse solo.
        """
        if before.channel is not None and len(before.channel.members) == 1:
            voice_client = discord.utils.get(self.voice_clients, channel=before.channel)
            if voice_client:
                await voice_client.disconnect()


bot = DiscordBot(command_prefix='-', library=library)
bot.run(TOKEN)
