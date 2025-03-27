# 🛠️ Plantão do Controlador

## 📌 Sobre o Projeto

O **Plantão do Controlador** é um sistema desenvolvido em **Django** com o objetivo de auxiliar no registro das ocorrências durante os plantões do controlador. Ele foi projetado para ser integrado ao sistema **Webcco**, proporcionando uma solução mais eficiente e organizada para a gestão de incidentes.

## 🚀 Funcionalidades

- 📋 Cadastro e listagem de ocorrências
- 📝 Adição de comentários a cada ocorrência
- 🔍 Filtros para facilitar a busca por ocorrências
- 📊 Painel informativo sobre o status do plantão

## 🏗️ Tecnologias Utilizadas

- **Python** 🐍
- **Django** 🎯
- **HTML, CSS e Bootstrap** 🎨
- **Banco de Dados PostgreSQL** 🗄️

## ⚙️ Como Rodar o Projeto

1. Clone este repositório:
   ```sh
   git clone https://github.com/seuusuario/plantao-controlador.git
   ```
2. Acesse a pasta do projeto:
   ```sh
   cd plantao-controlador
   ```
3. Crie e ative um ambiente virtual:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```
4. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
5. Execute as migrações do banco de dados:
   ```sh
   python manage.py migrate
   ```
6. Inicie o servidor:
   ```sh
   python manage.py runserver
   ```

Acesse no navegador: **http://127.0.0.1:8000/** 🚀
