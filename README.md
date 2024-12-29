# Sistema de Gerenciamento de Estoque

# Descrição

O Sistema de Gerenciamento de Estoque é uma aplicação web desenvolvida para gerenciar produtos em estoque, com funcionalidades de listagem, adicionamento e remoção de produtos. A aplicação permite a visualização de produtos, controle de inventário e a administração eficiente dos itens em estoque.

# Tecnologias Utilizadas

FastAPI: Framework moderno e rápido para a construção da API backend.

Streamlit: Biblioteca de interface para construir a interface gráfica do frontend.

Python: Linguagem de programação principal utilizada no backend.

JavaScript: Para interações no frontend, como remoção de produtos dinâmicas.

HTML/CSS: Utilizado para estilização e formatação da interface.

Uvicorn: Servidor ASGI para rodar o FastAPI em modo de desenvolvimento.

requests: Biblioteca para realizar chamadas HTTP no frontend (quando necessário).

APIRouter (FastAPI): Utilizado para estruturar as rotas de API de forma modular e organizada.

# Funcionalidades

Listar Produtos: Exibe todos os produtos cadastrados no estoque com informações detalhadas (nome, categoria, preço, quantidade e localização).

Adicionar Produto: Permite adicionar novos produtos ao estoque, com a inclusão de dados como nome, categoria, quantidade, preço e localização.

Remover Produto: Permite excluir um produto do estoque. A remoção é feita via requisição HTTP DELETE, com a interface atualizando dinamicamente a lista de produtos.

Interface de Usuário Intuitiva: Desenvolvida com Streamlit para fornecer uma experiência de usuário simples e interativa.

# Objetivos

Gerenciamento Eficiente de Estoque: Facilitar o controle de inventário para empresas, lojas e qualquer organização que precise gerenciar produtos de forma prática.

Acesso Rápido e Simples: Fornecer uma interface fácil de usar para visualizar, adicionar e remover produtos com agilidade.

Escalabilidade: Permitir a futura expansão das funcionalidades, como a integração com bancos de dados ou APIs de terceiros, a adição de autenticação de usuários e a geração de relatórios.

# Como Rodar o Projeto

Backend (FastAPI)

Instale as dependências do backend: pip install -r requirements.txt

Execute o servidor FastAPI: uvicorn app.main:app --reload

Acesse a API em http://localhost:8000.

Frontend (Streamlit)
Instale as dependências do frontend: pip install -r requirements.txt

Execute o aplicativo Streamlit: streamlit run app/streamlit_app.py

Acesse a interface em http://localhost:8501.

# Contribuições
Sinta-se à vontade para contribuir com melhorias no código, novas funcionalidades ou correções de bugs. Basta fazer um fork deste repositório, realizar suas modificações e abrir um pull request.
