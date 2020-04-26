import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='-')


async def play(ctx, sound_path):
    vc = ctx.author.voice.channel
    if ctx.voice_client is None:
        voice_channel = await vc.connect()
    else:
        await ctx.voice_client.move_to(vc)
        voice_channel = ctx.voice_client
    if not voice_channel.is_playing():
        voice_channel.play(discord.FFmpegPCMAudio(sound_path))


def is_user_connected(ctx):
    if ctx.author.voice is None or ctx.author.voice.channel is None:
        return False
    return True


@bot.command()
async def pisco(ctx):
    """"Vómito pisco a lo macho"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/pisco_a_lo_macho.mp3')


@bot.command()
async def oof(ctx):
    """Roblox oof"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/oof.mp3')


@bot.command()
async def moof(ctx):
    """Minecraft oof"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/moof.mp3')


@bot.command()
async def tension(ctx):
    """Sonido intrigante"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/tension.mp3')


@bot.command()
async def bolsa(ctx):
    """W3 la bolsa o la vida"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/bolsa.wav')


@bot.command()
async def mrlgr(ctx):
    """W3 murloc"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/mrlgr.mp3')


@bot.command()
async def death(ctx):
    """W3 humano muriendo"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/death.wav')


@bot.command()
async def death2(ctx):
    """W3 priest muriendo"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/death2.wav')


@bot.command()
async def malganis(ctx):
    """W3 Arthas maldiciendo a malganis"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/malganis.mp3')


@bot.command()
async def illi1(ctx):
    """W3 Illidan: me estoy impacientando"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/illi1.wav')


@bot.command()
async def dri1(ctx):
    """W3 Dríade: abriendo puertas"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/dri1.wav')


@bot.command()
async def dwarf1(ctx):
    """W3 Dwarf: chupate esa, chúpatela tú"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/dwarf1.wav')


@bot.command()
async def berlini(ctx):
    """Un berlini"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/berlini.mp3')


@bot.command()
async def s1(ctx):
    """Arrudorranador"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/s1.mp3')


@bot.command()
async def s2(ctx):
    """Tengo 4"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/s2.mp3')


@bot.command()
async def arthas1(ctx):
    """W3 Arthas: No es necesario hacer una reverencia"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/arthas1.wav')


@bot.command()
async def arthas2(ctx):
    """W3 Arthas: Estupido bellaco"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/arthas2.wav')


@bot.command()
async def arthas3(ctx):
    """W3 Arthas: Por mi padre el rey"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/arthas3.wav')


@bot.command()
async def arthas4(ctx):
    """W3 Arthas: Ha llegado la justicia"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/arthas4.wav')


@bot.command()
async def arthas5(ctx):
    """W3 Arthas: No te lo permitiré malganis"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/arthas5.mp3')


@bot.command()
async def hola(ctx):
    """W3: Hola"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/hola.wav')


@bot.command()
async def kel1(ctx):
    """W3 Kel'thuzad: chupate esa"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/kel1.wav')


@bot.command()
async def kel2(ctx):
    """W3 Kel'thuzad: He estado pensando"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/kel2.wav')


@bot.command()
async def kael1(ctx):
    """W3 Kael'thas: Estoy nerviosillo"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/kael1.wav')


@bot.command()
async def kael2(ctx):
    """W3 Kael'thas: Persivo algo escurridizo"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/kael2.wav')


@bot.command()
async def cap1(ctx):
    """W3 Capitán: Bestia estúpida"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/cap1.wav')


@bot.command()
async def cap2(ctx):
    """W3 Capitán: Tenía que haberle hecho caso a mi padre y haberme metido a granjero"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/cap1.wav')


@bot.command()
async def sor1(ctx):
    """W3 hechicera: Ayúdame a ayudarte"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/sor1.wav')


@bot.command()
async def be1(ctx):
    """W3 Blood Elf: Estoy trabajando"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/be1.wav')


@bot.command()
async def be2(ctx):
    """W3 Blood Elf: No no no, déjame a mi"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/be2.wav')


@bot.command()
async def bonv1(ctx):
    """Bonvallet: Ahueonao"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/aweonao.mp3')


@bot.command()
async def pini1(ctx):
    """Piñera: Enemigo implacable"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/piñi1.mp3')


@bot.command()
async def min1(ctx):
    """Minecraft: Villager Sound"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/min1.mp3')


@bot.command()
async def min2(ctx):
    """Minecraft: Theme song"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/min2.mp3')


@bot.command()
async def gay(ctx):
    """Chang: Ha-Gay!"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/ha-gay.mp3')


@bot.command()
async def yoshi(ctx):
    """Yoshi: tongue"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/yoshi-tongue.mp3')


@bot.command()
async def oof2(ctx):
    """Roblox: oof lento"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/oof_slow.mp3')


@bot.command()
async def efukt(ctx):
    """Efukt: song"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/efukt.mp3')


@bot.command()
async def sad(ctx):
    """Sad Trombone"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/sadtrombone.swf.mp3')


@bot.command()
async def grillos(ctx):
    """Crickets"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/crickets.mp3')


@bot.command()
async def tudumtss(ctx):
    """Tum Dum Tss"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/tudumtss.mp3')


@bot.command()
async def spanishflea(ctx):
    """Spanish flea"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/spanish_flea.mp3')


@bot.command()
async def sad2(ctx):
    """Sad violin"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/sad_violin.mp3')


@bot.command()
async def poetboy1(ctx):
    """Niño poeta: Fama máxima"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/poetboy1.mp3')


@bot.command()
async def poetboy2(ctx):
    """Niño poeta: famoso"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/poetboy2.mp3')


@bot.command()
async def funeral(ctx):
    """Negros funeral"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/african_funeral.mp3')


@bot.command()
async def deadman(ctx):
    """deadman"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/deadman.mp3')


@bot.command()
async def tuturu(ctx):
    """tuturu"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/tuturu.mp3')


@bot.command()
async def karol(ctx):
    """Hola hablas con karol"""
    if is_user_connected(ctx):
        await play(ctx, '../sounds/karol1.mp3')


bot.run(TOKEN)
