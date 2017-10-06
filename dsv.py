#!/usr/bin/python3
# DSV = Potenciando Youtube-dl
# Darwin Orellana by SEGURIDADS
# Viernes, 6 de Octubre del 2017

import os
import sys

os.system("echo")
url = str(input("\033[1;4;34mLINK > \033[1;m"))
os.system("echo")
opc = str(input(
    " \033[1;33md \033[1;m-> Detallado \n \033[1;33mf \033[1;m-> FullHD\n \033[1;33mm \033[1;m-> mp3\n \033[1;33mp \033[1;m-> PlayList\n \n\033[1;4;34mOPCION > \033[1;m "))


def gracias():
    print(" \033[1;36m \n \tGRACIAS POR USAR DSV \n \033[1;m \n  \033[1;5;37m \twww.seguridads.com \033[1;m ")


if opc == 'd':
    os.system("youtube-dl -vv " + url)
    gracias()
elif opc == 'f':
    os.system("youtube-dl -f 43 --no-warnings " + url)
    gracias()
elif opc == 'm':
    os.system("youtube-dl -x --no-warnings --audio-format mp3 " + url)
    gracias()
elif opc == 'p':
    os.system("youtube-dl -i --no-warnings --yes-playlist " + url)
    gracias()
else:
    print("\033[1;31m No Has Seleccionado Ninguna Opcion \033[1;m")
    os.system("echo")
    gracias()

####
#### VISITANOS >>>  www.seguridads.com
####
