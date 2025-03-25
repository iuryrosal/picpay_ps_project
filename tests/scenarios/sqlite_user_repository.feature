# language: pt
Funcionalidade: (Repositório de Usuário do SQLite - SQLiteUserRepository) Permitir operar a criação, seleção, atualização e remoção de usuários do banco de dados SQLite

    Cenario: Solicitada criação de usuário com todos os atributos fornecidos.
        Dado a criação de um novo usuário com todos os atributos: primeiro nome, sobrenome e email
        Quando o método de criação for utilizado no repositório passando esses atributos
        Entao o algoritmo irá utilizar essas informações para gerar um novo usuário, atribuindo um ID (identificador único) incremental ao usuário criado
        E irá retornar esse objeto dentro de uma tupla, junto com dois campos nulos (que representa falhas detectadas, que será nula, pela operação ser bem executada).

        Dado a criação de um novo usuário com atributos obrigatórios apenas: primeiro nome e email
        Quando o método de criação for utilizado no repositório passando esses atributos
        Entao o algoritmo irá utilizar essas informações para gerar um novo usuário, considerando o sobrenome nulo (optativo), atribuindo um ID (identificador único) incremental ao usuário criado
        E irá retornar esse objeto dentro de uma tupla, junto com dois campos nulos (que representa falhas detectadas, que será nula, pela operação ser bem executada).

        Dado a criação de um novo usuário com algum atributo obrigatório faltante
        Quando o método de criação for utilizado no repositório passando esses atributos
        Entao o algoritmo irá gerar uma Exceção por falta de parâmetro obrigatório.
    
    Cenario: Solicitada seleção de todos os usuários do banco de dados.
        Dado a seleção de todos os usuários
        Quando o método de seleção total for utilizado no repositório
        Entao o algoritmo irá retornar os objetos de usuário selecionado, contendo todos os usuários da tabela User do banco de dados. Juntamente com dois campos nulos (que representa falhas detectadas, que será nula, pela operação ser bem executada).
    
    Cenario: Solicitada seleção de um usuário específico.
        Dado a seleção de um usuário específico a partir de um ID (identificação única).
        Quando o método de seleção de usuário por ID for utilizado no repositório
        Entao o algoritmo irá utilizar o ID para pegar um usuário específico
        E irá retornar esse objeto dentro de uma tupla, junto com dois campos nulos (que representa falhas detectadas, que será nula, pela operação ser bem executada).

        Dado a seleção de um usuário específico a partir de um ID (identificação única) que não existe na tabela User.
        Quando o método de seleção de usuário por ID for utilizado no repositório
        Entao o algoritmo irá detectar a não existência do ID
        E irá retornar o primeiro campo da Tupla vazio (por não achar o objeto), junto com os dois campos seguintes preenchidos com a claúsula 'UserDoesNotExist' e mensagem de erro (que representa falhas detectadas).
    
    Cenario: Solicitada atualização de um usuário específico.
        Dado a solicitação de atualização de um usuário específico a partir de um ID (identificação única), passando os novos valores para os atributos respectivos.
        Quando o método de atualização de usuário por ID for utilizado no repositório
        Entao o algoritmo irá utilizar o ID para pegar um usuário específico
        E irá atualizar os atributos fornecidos com os novos valores, mantendo os não especificados com o valor original
        E irá retornar o objeto de usuário atualizado dentro de uma tupla, junto com dois campos nulos (que representa falhas detectadas, que será nula, pela operação ser bem executada).

        Dado a solicitação de atualização de um usuário específico a partir de um ID (identificação única) que não existe na tabela User, passando os novos valores para os atributos respectivos.
        Quando o método de atualização de usuário por ID for utilizado no repositório
        Entao o algoritmo irá detectar a não existência do ID
        E irá retornar o primeiro campo da Tupla vazio (por não achar o objeto), junto com os dois campos seguintes preenchidos com a claúsula 'UserDoesNotExist' e mensagem de erro (que representa falhas detectadas).

    Cenario: Solicitada deleção de um usuário específico.
        Dado a solicitação de deleção de um usuário específico a partir de um ID (identificação única).
        Quando o método de deleção de usuário por ID for utilizado no repositório
        Entao o algoritmo irá utilizar o ID para pegar um usuário específico
        E irá deletar esse registro de usuário da tabela User
        E irá retornar o objeto de usuário deletado dentro de uma tupla, junto com dois campos nulos (que representa falhas detectadas, que será nula, pela operação ser bem executada).

        Dado a solicitação de deleção de um usuário específico a partir de um ID (identificação única) que não existe na tabela User.
        Quando o método de deleção de usuário por ID for utilizado no repositório
        Entao o algoritmo irá detectar a não existência do ID
        E irá retornar o primeiro campo da Tupla vazio (por não achar o objeto), junto com os dois campos seguintes preenchidos com a claúsula 'UserDoesNotExist' e mensagem de erro (que representa falhas detectadas).
