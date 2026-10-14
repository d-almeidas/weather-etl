<div align="center">

![Open-Meteo Free Weather API](banner.png)

# 🌦️ weather-etl

**Mini projeto de ETL: coleta dados de clima da API Open-Meteo e carrega em um banco PostgreSQL.**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?logo=postgresql&logoColor=white)
![Requests](https://img.shields.io/badge/requests-HTTP-informational)

</div>

---

## Sobre o projeto

Este projeto implementa o fluxo básico de um pipeline de dados:

1. **Extract**: consome a API gratuita [Open-Meteo](https://open-meteo.com/) (não precisa de chave de API) usando `requests`.
2. **Transform**: limpa e organiza o JSON retornado (tipos de dados, nomes de colunas, datas).
3. **Load**: grava os dados em tabelas do **PostgreSQL**, evitando duplicatas.

Foi criado para praticar o consumo de APIs, o tratamento de erros (retry/backoff) e a persistência em banco relacional, como um primeiro passo rumo à engenharia de dados.

> ⚠️ Este projeto ainda está em desenvolvimento!

---
