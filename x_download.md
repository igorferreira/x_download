# README - Twitter Video Download Script

Este script em Python permite fazer download de vídeos do Twitter utilizando a biblioteca `yt_dlp`. Abaixo, você encontrará uma explicação detalhada de cada linha de código.

### Requisitos
- Python 3
- Biblioteca `yt_dlp` (instale usando `pip install yt-dlp`)

### Usando pyenv

Para gerenciar versões do Python com `pyenv` neste projeto, siga as etapas abaixo:

1. **Instalar o pyenv**:
   Siga as instruções abaixo para instalar o `pyenv` via linha de comando no Linux:
   ```
   curl https://pyenv.run | bash
   ```
   Depois, adicione as seguintes linhas ao seu arquivo `~/.bashrc` (ou `~/.zshrc` se você usar Zsh):
   ```
   export PATH="$HOME/.pyenv/bin:$PATH"
   eval "$(pyenv init --path)"
   eval "$(pyenv init -)"
   eval "$(pyenv virtualenv-init -)"
   ```
   Reinicie seu terminal ou rode `source ~/.bashrc` para aplicar as mudanças.

2. **Instalar a versão correta do Python**:
   Certifique-se de que o `pyenv` está instalado e, em seguida, instale a versão desejada do Python:
   ```
   pyenv install 3.12.4  # Substitua 3.12.4 pela versão necessária, por exemplo, 3.9.1
   ```

3. **Definir a versão do Python para o projeto**:
   Dentro do diretório do projeto, defina a versão específica do Python a ser usada:
   ```
   pyenv local 3.12.4  # Substitua 3.12.4 pela versão instalada
   ```
   Isso criará um arquivo `.python-version` no diretório do projeto, indicando qual versão do Python deve ser usada.

4. **Criar um ambiente virtual (opcional, mas recomendado)**:
   Crie um ambiente virtual para o projeto:
   ```
   python -m venv venv
   ```

5. **Ativar o ambiente virtual**:
   No Linux/macOS:
   ```
   source venv/bin/activate
   ```
   No Windows:
   ```
   venv\Scripts\activate
   ```

6. **Instalar as dependências**:
   Com o ambiente virtual ativado, instale a biblioteca necessária:
   ```
   pip install yt-dlp
   ```

### Executando todos os comandos em sequência

Para configurar rapidamente o ambiente e executar o script, siga os comandos abaixo em sequência:

```bash
# Instalar o pyenv
curl https://pyenv.run | bash

# Adicionar pyenv ao PATH e inicializar
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
source ~/.bashrc

# Instalar a versão correta do Python
pyenv install 3.12.4  # Substitua 3.12.4 pela versão necessária

# Definir a versão do Python para o projeto
pyenv local 3.12.4  # Substitua 3.12.4 pela versão instalada

# Criar um ambiente virtual (opcional, mas recomendado)
python -m venv venv

# Ativar o ambiente virtual
source venv/bin/activate

# Instalar as dependências
pip install yt-dlp

# Executar o script de download do vídeo do Twitter
python script.py <url_do_twitter>
```

### Explicação do Código

```python
import yt_dlp
import sys
```

- `import yt_dlp`: Importa a biblioteca `yt_dlp`, que é usada para fazer o download de vídeos de várias plataformas, incluindo o Twitter.
- `import sys`: Importa o módulo `sys`, que permite acessar argumentos da linha de comando.

```python
def baixar_video_twitter(url):
    print(f"Iniciando o download do vídeo para a URL: {url}")
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',  # Template para nome do arquivo
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            print("Download concluído com sucesso.")
        except Exception as e:
            print(f"Erro durante o download: {e}")
```

- `def baixar_video_twitter(url)`: Define uma função chamada `baixar_video_twitter` que recebe uma URL do Twitter como argumento.
- `print(f"Iniciando o download do vídeo para a URL: {url}")`: Imprime uma mensagem indicando que o download do vídeo foi iniciado.
- `ydl_opts = {'outtmpl': '%(title)s.%(ext)s'}`: Define um dicionário de opções para o `yt_dlp`, especificando o formato do nome do arquivo de saída.
- `with yt_dlp.YoutubeDL(ydl_opts) as ydl`: Cria uma instância do `YoutubeDL` com as opções definidas.
- `ydl.download([url])`: Chama o método `download` da instância `ydl` para baixar o vídeo da URL fornecida.
- `print("Download concluído com sucesso.")`: Imprime uma mensagem indicando que o download foi concluído com sucesso.
- `except Exception as e`: Captura qualquer exceção que ocorra durante o download e imprime uma mensagem de erro.

```python
if __name__ == "__main__":
    print("Verificando argumentos de linha de comando...")
    if len(sys.argv) != 2:
        print("Uso: python script.py <url_do_twitter>")
    else:
        url = sys.argv[1]
        print(f"URL recebida: {url}")
        baixar_video_twitter(url)
```

- `if __name__ == "__main__":`: Verifica se o script está sendo executado diretamente (não importado como módulo).
- `print("Verificando argumentos de linha de comando...")`: Imprime uma mensagem indicando que os argumentos da linha de comando estão sendo verificados.
- `if len(sys.argv) != 2`: Verifica se o número de argumentos passados é igual a 2 (o próprio nome do script e a URL).
- `print("Uso: python script.py <url_do_twitter>")`: Se o número de argumentos for incorreto, imprime uma mensagem explicando como usar o script.
- `url = sys.argv[1]`: Obtém a URL do vídeo do argumento da linha de comando.
- `print(f"URL recebida: {url}")`: Imprime a URL recebida.
- `baixar_video_twitter(url)`: Chama a função `baixar_video_twitter` para fazer o download do vídeo.

### Como Usar

1. Certifique-se de ter o Python 3 instalado.
2. Instale a biblioteca `yt_dlp` com o comando:
   ```
   pip install yt-dlp
   ```
3. Execute o script passando a URL do Twitter como argumento:
   ```
   python script.py <url_do_twitter>
   ```
   Substitua `<url_do_twitter>` pela URL do tweet que contém o vídeo.

### Exemplo
```bash
python script.py https://twitter.com/usuario/status/1234567890
```

### Observações
- Certifique-se de que a URL fornecida seja válida e contenha um vídeo para download.
- O script irá salvar o vídeo no mesmo diretório em que for executado, utilizando o título do vídeo como nome do arquivo.