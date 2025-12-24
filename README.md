# 🚰 Data Pipeline: Distribuidora de Água e Gás

Este projeto simula um ecossistema de dados real de uma distribuidora, focado na transição de um usuário de csv para uma **Arquitetura de Dados Profissional** utilizando Python e a arquitetura Medalhão (Bronze, Silver, Gold).

## 🚀 Objetivo
Automatizar o processo de Extração, Transformação e Carga (ETL) de 20.000 registros mensais, garantindo a integridade dos dados e gerando indicadores de performance (KPIs) para o negócio.

## 🏗️ Arquitetura do Projeto
O projeto segue a **Medallion Architecture**, garantindo rastreabilidade e qualidade:

* **Bronze (Raw):** Dados brutos como extraídos da fonte, com inconsistências de data, preço e registros duplicados.
* **Silver (Cleansed):** Dados limpos, tipados e com regras de integridade aplicadas.
* **Gold (Curated):** Tabelas agregadas prontas para consumo em Dashboards (Power BI/Tableau).

## 🛠️ Tecnologias Utilizadas
* **Python 3.x**
* **Pandas:** Manipulação e tratamento de dados.
* **NumPy:** Lógica condicional e validação de regras de negócio.
* **OS/Pathlib:** Gerenciamento dinâmico de diretórios (portabilidade).

## 📂 Arquitetura de Pastas
```text
├── data/
│   ├── bronze/  # CSVs originais "sujos"
│   ├── silver/  # Dados limpos e normalizados
│   └── gold/    # KPIs e agregações finais
├── etl/
│   ├── extract.py    # Simulação da geração/coleta de dados
│   ├── transform.py  # O coração do ETL (Limpeza e Regras)
│   └── aggregate.py  # Criação dos datasets de inteligência
├── docs/             # Regras de negócio e dicionário de dados
└── README.md

## 📖 Documentação Adicional
Para detalhes sobre o significado de cada coluna e as transformações de tipos de dados, acesse o nosso:
👉 [Dicionário de Dados](docs/dicionario.md)