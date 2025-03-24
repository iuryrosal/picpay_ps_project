# Objetivo do Projeto:
Desenvolver uma aplicação web usando o framework Flask para realizar operações CRUD
(Create, Read, Update, Delete) em uma entidade de "Usuário". O candidato deve persistir
os dados no banco de dados SQLite.

# Requisitos Técnicos:
1. Utilizar Flask (ou FastAPI) como framework.
2. Utilizar o conceito de orientação a objetos no desenvolvimento da aplicação.
3. Persistir os dados em um banco de dados SQLite.
4. Implementar as operações CRUD para a entidade "Usuário" (GET, POST, PUT, DELETE).
5. Implementar testes unitários
6. O código deve ser bem estruturado e seguir as melhores práticas de programação.

# Endpoints:
1. `GET /users`: Retorna a lista de todos os usuários.
2. `GET /users/{id}`: Retorna os detalhes de um usuário específico.
3. `POST /users`: Adiciona um novo usuário.
4. `PUT /users/{id}`: Atualiza os dados de um usuário existente.
5. `DELETE /users/{id}`: Remove um usuário.

# Instruções
1. É necessário a presença de POETRY na máquina para ativar o ambiente Python e dependências para execução desse projeto.
2. Com POETRY disponível, execute o comando `poetry install` na pasta raiz do projeto (em que está o arquivo `pyproject.toml`) para realizar a instalação de todas as dependências listadas dentro do arquivo `pyproject.toml`.
3. Execute o comando `poetry shell` na pasta raiz do projeto (em que está o arquivo `pyproject.toml`) para ativação do ambiente virtual com Python na versão 3.12 e dependências.
4. Execute o comando `python -m db.init_db` para gerar o banco de dados SQLite localmente e popula-lo com dados fictícios na tabela User.
5. Execute o comando `uvicorn api.app:app --host 0.0.0.0 --port 8080` para ativar a API.

# Melhorias futuras do projeto:
Visando o longo prazo, coloco alguns pontos de evolução possíveis para esse projeto:
- Utilizar classes padrões para controlar os erros internos detectados pela checagens de repositório e service, para auxiliar na padronização, reuso e obter mais detalhes da falha.
- Utilizar logging para auxiliar no registro de execuções e processamentos de requisições, com um track_id gerado para cada requisição, assim como detalhes do payload de processamento, detalhes dos erros. Essas informações também podem ser incorporadas na response da requisição (em caso de falhas detectadas). 
- Evoluir a cobertura de testes (coverage) para obter algo entre 80-90%.
- Melhorar o gerenciamento de contexto da classe SQLiteClient.
- Adicionar possibilidade de paginação no processo de selecionar todos os usuários, assim como query parameters para controlar essa paginação ou colocar limites (isso seria muito bom imaginando casos de muitos usuários na tabela). Padrão: `/?page[offset]=0&page[limit]=10`