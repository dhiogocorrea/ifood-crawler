# Ifood-Crawler

---
## Sem docker:

1. Instale as dependências:
```
pip install -r requirements.txt
```

2. Rode o servidor uvicorn:
```
uvicorn main:app --app-dir app/ --reload
```

A documentação (Swagger) da API estará disponível em: _localhost:8000/docs_

---

## Com docker:

1. Faça o build do docker:
```
docker build -t ifoodonation_ifood_crawler:latest .
```

2. Rode o docker:
```
docker run -p 8000:80 -d ifoodonation_ifood_crawler:latest
```