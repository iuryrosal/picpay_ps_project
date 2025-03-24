Funcionalidade: (Controller de Usuário - UserController) Permitir operar a criação, seleção, atualização e remoção de usuários a partir de uma API

    Cenario: Solicitada criação de usuário com todos os atributos fornecidos.
        Dado a requisição de criação de um novo usuário com todos os atributos: primeiro nome, sobrenome e email (por meio do body da requisição)
        Quando o método de criação for utilizado no controller passando esses atributos por meio do método POST no endpoint `/users/`
        Entao o algoritmo irá validar a requisição
        E realizar a chamada do método de criação de usuário no serviço (UserService)
        E irá retornar o objeto do usuário criado com HTTP_STATUS OK (200)

        Dado a requisição de criação de um novo usuário com atributos obrigatórios faltantes (por meio do body da requisição)
        Quando o método de criação for utilizado no controller passando esses atributos por meio do método POST no endpoint `/users/`
        Entao o algoritmo irá validar a requisição
        E irá retornar com HTTP_STATUS Bad Request (400) pela falta de atributos obrigatórios sem realizar contato com a camada de serviço (UserService)

    Cenario: Solicitada seleção de usuário específico.
        Dado a requisição de seleção de um usuário a partir de um ID específico existente no banco de dados (passado via pârametro de caminho)
        Quando o método de seleção for utilizado no controller passando esses atributos por meio do método GET no endpoint `/users/{user_id}`
        Entao o algoritmo irá validar a requisição 
        E realizar a chamada do método de seleção de usuário pelo ID no serviço (UserService)
        E irá retornar o objeto do usuário selecionado com HTTP_STATUS OK (200)

        Dado a requisição de seleção de um usuário a partir de um ID específico que não existente no banco de dados (passado via pârametro de caminho)
        Quando o método de seleção for utilizado no controller passando esses atributos por meio do método GET no endpoint `/users/{user_id}`
        Entao o algoritmo irá validar a requisição
        E realizar a chamada do método de seleção de usuário pelo ID no serviço (UserService)
        E irá retornar com HTTP_STATUS NOT FOUND (404) por não encontrar o ID específico, com code=UserNotExists e msg especificando o usuário não encontrado com o id fornecido.

    Cenario: Solicitada seleção de todos os usuários.
        Dado a requisição de seleção de vários usuários
        Quando o método de seleção for utilizado no controller por meio do método GET no endpoint `/users`
        Entao o algoritmo irá validar a requisição 
        E realizar a chamada do método de seleção de todos os usuários (UserService)
        E irá retornar a lista dos objetos do usuário selecionados com HTTP_STATUS OK (200)
    
    Cenario: Solicitada atualização de usuário específico.
        Dado a requisição de atualização de um usuário a partir de um ID específico existente no banco de dados (passado via pârametro de caminho), com novos valores de atributos respectivos.
        Quando o método de atualização for utilizado no controller passando esses atributos por meio do método PUT no endpoint `/users/{user_id}`
        Entao o algoritmo irá validar a requisição 
        E realizar a chamada do método de atualização de usuário pelo ID no serviço (UserService), passando os novos valores dos atributos fornecidos
        E irá retornar o objeto do usuário atualizado (considerando apenas os atributos fornecidos, os não fornecidos manterá o valor original) com HTTP_STATUS OK (200)

        Dado a requisição de seleção de um usuário a partir de um ID específico que não existente no banco de dados (passado via pârametro de caminho)
        Quando o método de atualização for utilizado no controller passando esses atributos por meio do método PUT no endpoint `/users/{user_id}`
        Entao o algoritmo irá validar a requisição
        E realizar a chamada do método de atualização de usuário pelo ID no serviço (UserService)
        E irá retornar com HTTP_STATUS NOT FOUND (404) por não encontrar o ID específico, com code=UserNotExists e msg especificando o usuário não encontrado com o id fornecido.

    Cenario: Solicitada deleção de usuário específico.
        Dado a requisição de deleção de um usuário a partir de um ID específico existente no banco de dados (passado via pârametro de caminho).
        Quando o método de deleção for utilizado no controller passando esses atributos por meio do método DELETE no endpoint `/users/{user_id}`
        Entao o algoritmo irá validar a requisição 
        E realizar a chamada do método de deleção de usuário pelo ID no serviço (UserService)
        E irá retornar com HTTP_STATUS OK (200), contendo code='UserDeleted' e msg com especificando o usuário deletado com o ID fornecido.