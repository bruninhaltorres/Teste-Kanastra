# Sistema de Cadastro Cobranças Kanastra

## Visão Geral:
Bem-vindo ao sistema de cadastro de cobranças da Kanastra!

Este sistema foi desenvolvido visando solucionar o desafio de construir um sistema de cadastro de cobranças na plataforma. Com ele, você podera:

- Registrar novas cobranças.
- Visualizar e editar cobranças existentes.
- Apagar cobranças.

## Tecnologias utilizadas:

- Python
- Django e Django Rest Framework
- React.JS
- Docker e Docker Compose
- SQLite
- Postman
- Swagger

## Requisitos
Certifique-se de ter o Docker, o Docker Compose e o Docker Desktop instalados em sua máquina antes de prosseguir.

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Docker Desktop](https://docs.docker.com/desktop/install/windows-install/)    

## Instalação e Execução do sistema

### Passo 1: Clonar o Repositório
Clone o repositório do GitHub para sua máquina local:

```bash
git clone https://github.com/seu-usuario/seu-projeto.git
```

#### 2.1: Docker Desktop
Inicialize o Docker Desktop e espere que o mesmo esteja em execução e pronto pra ser usado antes de seguir para os próximos passos.

#### 2.2: Compilando
No terminal, navegue até o diretório onde você clonou este repositório e execute o seguinte comando para iniciar o sistema:

```bash
docker-compose up
```

Aguarde até que o Docker Compose construa as imagens e inicie os contêineres.

### Passo 3: Acessar o Sistema

#### FrontEnd:

    http://localhost:3000/

#### BackEnd:
  
    http://localhost:8000/
    
##### Documentação Swagger:

    http://localhost:8000/swagger/

### Passo 4: Encerrar o sistema
Para interromper a execução do sistema e desligar os contêineres, pressione Ctrl + C no terminal onde o docker-compose up está sendo executado.
