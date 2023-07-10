import discord
from discord.ext import commands
import os
import random
import webbrowser as web
import vlc
import time

def media ():
    musics = ("C:/Users/www/OneDrive/Masaüstü/Yeni klasör/musics/music.mp3","C:/Users/www/OneDrive/Masaüstü/Yeni klasör/musics/music1.mp3","C:/Users/www/OneDrive/Masaüstü/Yeni klasör/musics/music2.mp3")
    secim = random.choice(musics)
    G = vlc.MediaPlayer(secim)
    G.play()
    print(secim)
    time.sleep(10)
media ()
