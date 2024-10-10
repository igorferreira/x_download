# Twitter Video Download Script
# --------------------------------
# Este script permite fazer download de vídeos do Twitter utilizando a biblioteca yt_dlp.
# O vídeo baixado é movido para uma pasta chamada 'x_downloads' após o download ser concluído.
# Requisitos: Python 3, yt_dlp
# Uso: python x_download.py <url_do_twitter>

import yt_dlp
import sys
import os
import shutil

def baixar_video_twitter(url):
    # 1.0 - Imprimir mensagem indicando o início do download
    print(f"Iniciando o download do vídeo para a URL: {url}")
    
    # 1.1 - Definir as opções do yt_dlp, incluindo o template para nome do arquivo de saída
    ydl_opts = {
        'outtmpl': 'x_downloads/%(title)s.%(ext)s',  # Template para nome do arquivo (título e extensão do vídeo)
    }
    
    # 1.2 - Criar uma instância do YoutubeDL com as opções definidas
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            # 1.3 - Tentar fazer o download do vídeo
            ydl.download([url])
            print("Download concluído com sucesso.")
        except Exception as e:
            # 1.4 - Imprimir mensagem de erro caso o download falhe
            print(f"Erro durante o download: {e}")

if __name__ == "__main__":
    # 2.0 - Verificar se o script está recebendo o número correto de argumentos de linha de comando
    print("Verificando argumentos de linha de comando...")
    if len(sys.argv) != 2:
        # 2.1 - Imprimir instruções de uso se os argumentos forem incorretos
        print("Uso: python script.py <url_do_twitter>")
    else:
        # 2.2 - Capturar a URL fornecida e iniciar o processo de download
        url = sys.argv[1]
        print(f"URL recebida: {url}")
        baixar_video_twitter(url)