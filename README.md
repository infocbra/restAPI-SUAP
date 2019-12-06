# Projeto_PPI (Painel de Senhas)

 **Professor Orientador**: Fábio Henrique M. Oliveira

 **Disciplina**: Programação para Internet II (PPI-II)

 **Alunos** : Daniel Barros e Levi Alves

 **Link para o sistema** : http://danielb.pythonanywhere.com/
 
 **Objetivo do Projeto**:
 Implementar API e telas para controle de senhas.

### Estrutura de Arquivos
 * demo: Exemplo do uso do Django rest framework;
 * Modelo: Modelo Relacional com estrutura do banco de dados;
 * painel: projeto Django;
 * panelEnv: ambiente virtual python;
 * presentation: Apresentação powerpoint sobre API's.

### Estrutura de Arquivos Django
 * 
 *
 *

### Requisitos:
    - Python <= 3.6;
    - Django; 
    - Django rest framework;

### Uso da API
#### Endpoints:
     /api/senha
        - POST
            - Cria uma nova senha;
            obs: Necessita de uma categoria e um tipo. 

        - GET
            - Retorna todas as senhas existentes.

     /api/senha/categoria
        - GET
            - Retorna todas as categorias existentes no banco.

     /api/senha/tipo 
        - GET
            - Retorna todos os tipos existentes no banco.

    /api/user/create 
        - POST
            - Cria um usuário e a senha para acesso ao token da API.
    
    /api/user/token 
        - POST
            - Acesso com o usuário já cadastrado para a geração do token.
    
#### Parser Types Endpoints:
    - x-www-former-urlencoded

![Alt text](Prints/Postman_imagem.png?raw=true "Title")
