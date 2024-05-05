# Teste Kanastra - Sistema de Cobranças

## Tecnologias utilizadas:

- Python
- Django
- Django Rest Framework
- Docker
- 
- Postman

## Requisitos
- Docker instalado: [Instruções de instalação do Docker](https://docs.docker.com/get-docker/)
- Navegador web moderno (para acessar o frontend)

## Instalação e Execução do sistema

### Passo 1: Clonar o Repositório
Clone o repositório do GitHub para sua máquina local:

```bash
git clone https://github.com/seu-usuario/seu-projeto.git
```
### Passo 2: Configuração do BackEnd

#### 2.1 Instalar Dependências
Certifique-se de estar no diretório raiz do projeto e execute o seguinte comando para construir a imagem Docker do backend:

```bash
cd seu-projeto
docker build -t nome-imagem-backend .
```

#### 2.2 Iniciar o Contêiner do Backend
Após a construção da imagem, inicie o contêiner do backend:

```bash
docker run -p 8000:8000 nome-imagem-backend
```

### Passo 3: Configuração do FrontEnd

#### 3.1 Instalar Dependências
Certifique-se de estar no diretório raiz do projeto e navegue até o diretório do frontend:

```bash
cd frontend
```
Instale as dependências do frontend:

```bach
npm install
```

#### 3.2 Iniciar o Servidor de Desenvolvimento do Frontend
Após a instalação das dependências, inicie o servidor de desenvolvimento do frontend:

```bach
npm start
```

### Passo 4: Acessar o Sistema

#### FrontEnd:

    http://localhost:3000/charges

#### API:
  
    http://localhost:8000/charges
    
#### Documentação Swagger:

    http://localhost:8000/swagger/

#### Django Admin:
  
    http://localhost:8000/admin/