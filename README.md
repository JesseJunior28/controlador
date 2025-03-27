# Plantão do Controlador

Este é um projeto desenvolvido em **Django** para auxiliar no registro das ocorrências do plantão do controlador. Ele foi projetado para garantir um controle mais eficiente e organizado das informações relacionadas ao plantão.

## Funcionalidades
- Cadastro e listagem de ocorrências do plantão.
- Edição e exclusão de ocorrências registradas.
- Adição e gerenciamento de comentários em cada ocorrência.

## Tecnologias Utilizadas
- **Django** (Backend)
- **SQLite/PostgreSQL** (Banco de Dados)
- **Bootstrap** (Frontend para estilização)
- **HTML, CSS e JavaScript**

## Instalação e Configuração
### 1. Clonar o repositório
```sh
git clone https://github.com/seu-usuario/plantao-controlador.git
cd plantao-controlador
```

### 2. Criar e ativar um ambiente virtual
```sh
python -m venv venv  # Ou use virtualenv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instalar dependências
```sh
pip install -r requirements.txt
```

### 4. Configurar o banco de dados
```sh
python manage.py migrate
```

### 5. Criar um superusuário (opcional)
```sh
python manage.py createsuperuser
```

### 6. Rodar o servidor
```sh
python manage.py runserver
```
Acesse o sistema em **http://127.0.0.1:8000/**

## Contribuição
Fique à vontade para contribuir com melhorias no projeto. Basta fazer um fork, criar uma branch e enviar um pull request!

---
Projeto desenvolvido para otimizar o registro de ocorrências do plantão do controlador. ✨

