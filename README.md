# Cardiovascular Disease Predictor BFF

Este pequeno projeto é a primeira versão do BFF do MVP do Cardiovascular Disease Predictor

O objetivo do projeto é um "backend for front end" responsável por fazer uma conexão entre o front-end com o Modelo Machine Learning de predição de doenças cardiovasculares.

**POST PREDICT**: Uma rota para predição de doenças cardiovasculares.

---

## Como Executar

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas, é bem simples o processo.

Após clonar o repositório, é necessário ir ao diretório raiz do projeto, pelo terminal, para poder executar os comandos descritos abaixo.

Criação do env

```bash
python -m venv env
```
Inicialização do env

```bash
source env/bin/activate
```
Instalação das dependências

```bash
(env)$ pip install -r requirements.txt
```

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```