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