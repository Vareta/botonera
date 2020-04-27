import os

import discord
import logging
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
ID = os.getenv('DISCORD_ID')
bot = commands.Bot(command_prefix='-')
logging.basicConfig(level=logging.INFO)


async def play(ctx, sound_path):
    vc = ctx.author.voice.channel
    if ctx.voice_client is None:
        voice_channel = await vc.connect()
    else:
        if not bot_in_channel(vc):
            await ctx.voice_client.move_to(vc)
        voice_channel = ctx.voice_client
    if not voice_channel.is_playing():
        voice_channel.play(discord.FFmpegPCMAudio(sound_path))


def bot_in_channel(channel):
    for member in channel.members:
        if member.id == ID:
            return True
    return False


def is_user_connected(ctx):
    if ctx.author.voice is None or ctx.author.voice.channel is None:
        return False
    return True


@bot.command()
async def pisco(ctx):
    """"Vómito pisco a lo macho"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/pisco_a_lo_macho.mp3')


@bot.command()
async def oof(ctx):
    """Roblox oof"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/oof.mp3')


@bot.command()
async def moof(ctx):
    """Minecraft oof"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/moof.mp3')


@bot.command()
async def tension(ctx):
    """Sonido intrigante"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/tension.mp3')


@bot.command()
async def bolsa(ctx):
    """W3 la bolsa o la vida"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/bolsa.wav')


@bot.command()
async def mrlgr(ctx):
    """W3 murloc"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/mrlgr.mp3')


@bot.command()
async def death(ctx):
    """W3 humano muriendo"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/death.wav')


@bot.command()
async def death2(ctx):
    """W3 priest muriendo"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/death2.wav')


@bot.command()
async def malganis(ctx):
    """W3 Arthas maldiciendo a malganis"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/malganis.mp3')


@bot.command()
async def illi1(ctx):
    """W3 Illidan: me estoy impacientando"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/illi1.wav')


@bot.command()
async def dri1(ctx):
    """W3 Dríade: abriendo puertas"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/dri1.wav')


@bot.command()
async def dwarf1(ctx):
    """W3 Dwarf: chupate esa, chúpatela tú"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/dwarf1.wav')


@bot.command()
async def berlini(ctx):
    """Un berlini"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/berlini.mp3')


@bot.command()
async def s1(ctx):
    """Arrudorranador"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/s1.mp3')


@bot.command()
async def s2(ctx):
    """Tengo 4"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/s2.mp3')


@bot.command()
async def arthas1(ctx):
    """W3 Arthas: No es necesario hacer una reverencia"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/arthas1.wav')


@bot.command()
async def arthas2(ctx):
    """W3 Arthas: Estupido bellaco"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/arthas2.wav')


@bot.command()
async def arthas3(ctx):
    """W3 Arthas: Por mi padre el rey"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/arthas3.wav')


@bot.command()
async def arthas4(ctx):
    """W3 Arthas: Ha llegado la justicia"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/arthas4.wav')


@bot.command()
async def arthas5(ctx):
    """W3 Arthas: No te lo permitiré malganis"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/arthas5.mp3')


@bot.command()
async def hola(ctx):
    """W3: Hola"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/hola.wav')


@bot.command()
async def kel1(ctx):
    """W3 Kel'thuzad: chupate esa"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/kel1.wav')


@bot.command()
async def kel2(ctx):
    """W3 Kel'thuzad: He estado pensando"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/kel2.wav')


@bot.command()
async def kael1(ctx):
    """W3 Kael'thas: Estoy nerviosillo"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/kael1.wav')


@bot.command()
async def kael2(ctx):
    """W3 Kael'thas: Persivo algo escurridizo"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/kael2.wav')


@bot.command()
async def cap1(ctx):
    """W3 Capitán: Bestia estúpida"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/cap1.wav')


@bot.command()
async def cap2(ctx):
    """W3 Capitán: Tenía que haberle hecho caso a mi padre y haberme metido a granjero"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/cap2.wav')


@bot.command()
async def sor1(ctx):
    """W3 hechicera: Ayúdame a ayudarte"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/sor1.wav')


@bot.command()
async def be1(ctx):
    """W3 Blood Elf: Estoy trabajando"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/be1.wav')


@bot.command()
async def be2(ctx):
    """W3 Blood Elf: No no no, déjame a mi"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/be2.wav')


@bot.command()
async def bonv1(ctx):
    """Bonvallet: Ahueonao"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/aweonao.mp3')


@bot.command()
async def pini1(ctx):
    """Piñera: Enemigo implacable"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/piñi1.mp3')


@bot.command()
async def min1(ctx):
    """Minecraft: Villager Sound"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/min1.mp3')


@bot.command()
async def min2(ctx):
    """Minecraft: Theme song"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/min2.mp3')


@bot.command()
async def gay(ctx):
    """Chang: Ha-Gay!"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/ha-gay.mp3')


@bot.command()
async def yoshi(ctx):
    """Yoshi: tongue"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/yoshi-tongue.mp3')


@bot.command()
async def oof2(ctx):
    """Roblox: oof lento"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/oof_slow.mp3')


@bot.command()
async def efukt(ctx):
    """Efukt: song"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/efukt.mp3')


@bot.command()
async def sad(ctx):
    """Sad Trombone"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/sadtrombone.swf.mp3')


@bot.command()
async def sad2(ctx):
    """Sad violin"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/sad_violin.mp3')


@bot.command()
async def sad3(ctx):
    """Sad naruto"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/sad_naruto.mp3')


@bot.command()
async def grillos(ctx):
    """Crickets"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/crickets.mp3')


@bot.command()
async def tudumtss(ctx):
    """Tum Dum Tss"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/tudumtss.mp3')


@bot.command()
async def spanishflea(ctx):
    """Spanish flea"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/spanish_flea.mp3')


@bot.command()
async def poetboy1(ctx):
    """Niño poeta: Fama máxima"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/poetboy1.mp3')


@bot.command()
async def poetboy2(ctx):
    """Niño poeta: famoso"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/poetboy2.mp3')


@bot.command()
async def funeral(ctx):
    """Negros funeral"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/african_funeral.mp3')


@bot.command()
async def deadman(ctx):
    """deadman"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/deadman.mp3')


@bot.command()
async def tuturu(ctx):
    """tuturu"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/tuturu.mp3')


@bot.command()
async def karol(ctx):
    """Hola hablas con karol"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/karol1.mp3')


@bot.command()
async def aco(ctx):
    """W3 Acolyte: death"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/aco1.wav')


@bot.command()
async def aco2(ctx):
    """W3 Acolyte: Esta es la hora del azote"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/aco2.wav')


@bot.command()
async def aco3(ctx):
    """W3 Acolyte: La muerte limpiará el mundo"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/aco3.wav')


@bot.command()
async def aco4(ctx):
    """W3 Acolyte: Los condenados estan listos"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/aco4.wav')


@bot.command()
async def aco5(ctx):
    """W3 Acolyte: Mi vida por ner'zhul"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/aco5.wav')


@bot.command()
async def aco6(ctx):
    """W3 Acolyte: Si señor"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/aco6.wav')


@bot.command()
async def aco7(ctx):
    """W3 Acolyte: Donde se derramará mi sangre"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/aco7.wav')


@bot.command()
async def aco8(ctx):
    """W3 Acolyte: Mi destino esta sellado"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/aco8.wav')


@bot.command()
async def antabaka(ctx):
    """anta baka"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/anta_baka.mp3')


@bot.command()
async def eggking(ctx):
    """Huevito rey: tu conoces el sexo, tu no conoces el sexo"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/eggking.mp3')


@bot.command()
async def keanu(ctx):
    """breathtaking"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/breathtaking.mp3')


@bot.command()
async def cairne(ctx):
    """W3 Cairne: mm se acerca una tormenta"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/cairne.wav')


@bot.command()
async def thicc(ctx):
    """Damn boy"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/thicc.mp3')


@bot.command()
async def malcom(ctx):
    """El futuro es hoy, oiste viejo"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/el_futuro_es_hoy.mp3')


@bot.command()
async def enfermedad(ctx):
    """Eres la enfermedad y yo la cura"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/eres_la_enfermedad.mp3')


@bot.command()
async def earthas(ctx):
    """W3 Arthas: Fuí un estupido confiando en la luz"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/earthas.wav')


@bot.command()
async def earthas2(ctx):
    """W3 Arthas: Gloria al azote"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/earthas2.wav')


@bot.command()
async def earthas3(ctx):
    """W3 Arthas: Habla estúpido"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/earthas3.wav')


@bot.command()
async def earthas4(ctx):
    """W3 Arthas: A mi no me mongonea nadie"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/earthas4.wav')


@bot.command()
async def earthas5(ctx):
    """W3 Arthas: Frostmourne esta hambrienta"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/earthas5.wav')


@bot.command()
async def earthas6(ctx):
    """W3 Arthas: Por fin!"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/earthas6.wav')


@bot.command()
async def simpsons(ctx):
    """Simpsons: hablen del dinero"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/simpsons.mp3')


@bot.command()
async def simpsons2(ctx):
    """Simpsons Homero: me aburren"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/simpsons2.mp3')


@bot.command()
async def grunt(ctx):
    """W3 Grunt: death"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/grunt.wav')


@bot.command()
async def grunt2(ctx):
    """W3 Grunt: Uh, eso ha sido bonito"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/grunt2.wav')


@bot.command()
async def oldman(ctx):
    """Adios viejo"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/joselito.mp3')


@bot.command()
async def onichan(ctx):
    """Onichan"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/onichan.mp3')


@bot.command()
async def onichan2(ctx):
    """Onichan I have a dick"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/onichan2.mp3')


@bot.command()
async def pervertido(ctx):
    """W3 pervertido"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/pervertido.wav')


@bot.command()
async def peon(ctx):
    """W3 Peón: trabajo trabajo"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/peon.wav')


@bot.command()
async def burns(ctx):
    """Simpsons Sr Burns: Realmente eres el rey de reyes"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/burns.mp3')


@bot.command()
async def burns2(ctx):
    """Simpsons Sr Burns: Realmente eres el rey de reyes. Excelente"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/burns2.mp3')


@bot.command()
async def burns3(ctx):
    """Simpsons Sr Burns: Risa"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/burns3.mp3')


@bot.command()
async def smithers(ctx):
    """Simpsons Sr Smithers: Em, volvamos a intentarlo mañana"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/smithers.mp3')


@bot.command()
async def smithers2(ctx):
    """Simpsons Sr Smithers: Damas y caballeros, contemplen a su nuevo dios"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/smithers2.mp3')


@bot.command()
async def flute(ctx):
    """Titanic flauta"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/flute.mp3')


@bot.command()
async def creer(ctx):
    """Uy, no lo puedo creer"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/no_lo_puedo_creer.mp3')


@bot.command()
async def back(ctx):
    """Música de ya volvemos"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/back.mp3')


@bot.command()
async def back2(ctx):
    """Música de ya volvemos"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/back2.mp3')


@bot.command()
async def wololo(ctx):
    """AoE2 Monje: Wololo"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/wololo.mp3')


@bot.command()
async def nyes(ctx):
    """Filthy Frank: nyees"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/nyeeeeeeeees.mp3')


@bot.command()
async def franku(ctx):
    """Filthy Frank: is time to stop"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/time_to_stop.mp3')


@bot.command()
async def franku2(ctx):
    """Filthy Frank: nobody gives a shit"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/nobody_gives_a_shit.mp3')


@bot.command()
async def franku3(ctx):
    """Filthy Frank: moshi moshi motherfucker"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/moshi_moshi_motherfucker.mp3')


@bot.command()
async def massu(ctx):
    """Massu Nada es imposible, niuna wea"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/nada_es_imposible.mp3')


@bot.command()
async def cardib(ctx):
    """Cardi b Coronavairus"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/cardib.mp3')


@bot.command()
async def kekw(ctx):
    """kekw"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/kekw.mp3')


@bot.command()
async def felipito(ctx):
    """Angel para un final inicio"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/angel_para_un_final_ini.mp3')


@bot.command()
async def felipito2(ctx):
    """Angel para un final fin"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/angel_para_un_final_fin.mp3')


@bot.command()
async def king(ctx):
    """King engine"""
    if is_user_connected(ctx):
        await play(ctx, './botonera/sounds/king_engine.mp3')


bot.run(TOKEN)
