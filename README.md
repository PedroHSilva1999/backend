# API de Filmes - Guia de Uso

## Como Usar a API

### 1. Iniciando o Projeto
Para começar a usar a API, siga estes passos:

1. Clone o repositório
2. No terminal ou prompt de comando, execute:

```bash
docker-compose up --build
```

### 2. Endpoints Disponíveis

#### Listar Todos os Filmes

```bash
GET http://localhost:8000/filmes

# Exemplo de resposta:
[
    {
        "id": 1,
        "titulo": "Matrix",
        "diretor": "Lana Wachowski",
        "ano": 1999,
        "genero": "Ficção Científica"
    }
]

#### Cadastrar Novo Filme
```bash
POST http://localhost:8000/filmes

# Corpo da requisição:
{
    "titulo": "Matrix",
    "diretor": "Lana Wachowski",
    "ano": 1999,
    "genero": "Ficção Científica"
}
```

#### Buscar Filme por ID
```bash
GET http://localhost:8000/filmes/1

# Exemplo de resposta:
{
    "id": 1,
    "titulo": "Matrix",
    "diretor": "Lana Wachowski",
    "ano": 1999,
    "genero": "Ficção Científica"
}
```

### 3. Exemplos de Uso

#### Usando cURL

1. Listar filmes:
```bash
curl http://localhost:8000/filmes
```

2. Cadastrar filme:
```bash
curl -X POST http://localhost:8000/filmes \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Matrix",
    "diretor": "Lana Wachowski",
    "ano": 1999,
    "genero": "Ficção Científica"
  }'
```

3. Buscar filme específico:
```bash
curl http://localhost:8000/filmes/1
```

#### Usando Python (requests)

```python
import requests

# URL base da API
base_url = "http://localhost:8000"

# Listar todos os filmes
response = requests.get(f"{base_url}/filmes")
filmes = response.json()

# Cadastrar novo filme
novo_filme = {
    "titulo": "Matrix",
    "diretor": "Lana Wachowski",
    "ano": 1999,
    "genero": "Ficção Científica"
}
response = requests.post(f"{base_url}/filmes", json=novo_filme)
filme_criado = response.json()

# Buscar filme por ID
filme_id = 1
response = requests.get(f"{base_url}/filmes/{filme_id}")
filme = response.json()
```

### 4. Documentação Interativa

A API possui documentação interativa disponível em:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### 5. Possíveis Erros

1. **Filme não encontrado (404)**
   - Ocorre quando tenta buscar um filme com ID inexistente

2. **Erro de validação (422)**
   - Ocorre quando os dados enviados não seguem o formato esperado
   - Exemplo: ano negativo ou campos obrigatórios faltando

### 6. Dicas

- Todos os campos são obrigatórios ao cadastrar um filme
- O ID é gerado automaticamente pelo sistema
- A API retorna os dados no formato JSON
- Use a documentação Swagger para testar a API de forma interativa
