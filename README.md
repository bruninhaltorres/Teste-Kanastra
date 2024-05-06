# Teste Kanastra - Sistema de Cobranças

## Tecnologias utilizadas:

- Python
- Django
- Django Rest Framework
- Docker
- 
- Postman

## Requisitos
Certifique-se de ter o Docker e o Docker Compose instalados em sua máquina antes de prosseguir.

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Instalação e Execução do sistema

### Passo 1: Clonar o Repositório
Clone o repositório do GitHub para sua máquina local:

```bash
git clone https://github.com/seu-usuario/seu-projeto.git
```
### Passo 2: Iniciar o sistema

#### 2.1: No terminal, navegue até o diretório onde você clonou este repositório.

#### 2.2: Execute o seguinte comando para iniciar o teste do sistema:
```bash
docker-compose up
```

#### 2.3: Aguarde até que o Docker Compose construa as imagens e inicie os contêineres.

### Passo 3: Acessar o Sistema

#### FrontEnd:

    http://localhost:3000/

#### BackEnd:
  
    http://localhost:8000/
    
##### Documentação Swagger:

    http://localhost:8000/swagger/

### Passo 4: Encerrar o sistema
Para interromper a execução do teste e desligar os contêineres, pressione Ctrl + C no terminal onde o docker-compose up está sendo executado.