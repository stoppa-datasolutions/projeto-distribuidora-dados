import pandas as pd
import os

# Pega o caminho da pasta onde este script (transform.py) está salvo
diretorio_do_script = os.path.dirname(os.path.abspath(__file__))

# Sobe um nível para chegar na pasta raiz do projeto (onde ficam data, etl, docs)
projeto_raiz = os.path.dirname(diretorio_do_script)

# Constrói o caminho para buscar o dado na Bronze e onde salvar na Silver
caminho_entrada = os.path.join(projeto_raiz, 'data', 'bronze', 'vendas_janeiro_2024_bruto.csv')
caminho_saida = os.path.join(projeto_raiz, 'data', 'silver', 'vendas_janeiro_2024_limpo.csv')

print(f"Buscando arquivo em: {caminho_entrada}")

# Tenta carregar o arquivo CSV
try:
    # O encoding 'utf-8' é o padrão, mas garantimos ele aqui para evitar erros de acentuação
    df = pd.read_csv(caminho_entrada, encoding='utf-8')
    print("Arquivo carregado com sucesso!")
    
    # Exibe as 5 primeiras linhas para conferirmos a 'sujeira'
    print("\n--- Amostra dos dados brutos: ---")
    print(df.head())
    
    # Exibe os tipos de dados identificados automaticamente (provavelmente tudo como 'object')
    print("\n--- Tipos de dados iniciais: ---")
    print(df.dtypes)

except Exception as e:
    print(f"Erro ao carregar o arquivo: {e}")

# --- TRATAMENTO DE DATAS (VERSÃO CORRIGIDA) ---
print("\nLimpando datas...")

# Usamos format='mixed' para avisar ao Pandas que cada linha pode ter um formato diferente
df['data_venda'] = pd.to_datetime(df['data_venda'], format='mixed', errors='coerce')

# Se houver algum problema com o 'mixed' (dependendo da sua versão do pandas), 
# uma alternativa comum é:
# df['data_venda'] = pd.to_datetime(df['data_venda'], errors='coerce')

datas_invalidas = df['data_venda'].isna().sum()
print(f"Datas convertidas! (Restaram {datas_invalidas} datas inválidas)")

# Vamos ver como ficaram as primeiras datas convertidas
print(df['data_venda'].head())

# --- TRATAMENTO DE INTEGRIDADE E NULOS ---
print("\nVerificando integridade dos registros...")

# 1. Removendo registros sem ID de Venda
# Em Engenharia, dados sem chave primária (ID) geralmente são descartados na Silver
linhas_antes = len(df)
df = df.dropna(subset=['id_venda'])
linhas_depois = len(df)
print(f"Registros removidos por falta de ID: {linhas_antes - linhas_depois}")

# 2. Preenchendo Formas de Pagamento vazias
# Em vez de NaN, deixamos explícito que não foi informado
df['forma_pagamento'] = df['forma_pagamento'].fillna('Não Informado')

# 3. Corrigindo o ID de Venda (Removendo o .0 do float)
# Como o ID era float por causa dos nulos, agora que limpamos, voltamos para Inteiro
df['id_venda'] = df['id_venda'].astype(int)

print("Integridade tratada com sucesso!")

# --- REGRAS DE NEGÓCIO ---
print("\nAplicando regras de negócio...")

# 1. Garantir que quantidade seja sempre positiva
# O .clip(lower=1) transforma qualquer número menor que 1 em 1
df['quantidade'] = df['quantidade'].astype(int).clip(lower=1)

# 2. Validação de B2B (Comércio sem CNPJ)
# Criamos uma coluna nova para ajudar o analista de dados na camada Gold
import numpy as np
df['validacao_cnpj'] = np.where(
    (df['tipo_cliente'] == 'comercio') & (df['cnpj'].isna()), 
    'PENDENTE', 
    'OK'
)

print("Regras de negócio aplicadas!")

# --- CARGA (SAVE) ---
print(f"\nSalvando dados na camada Silver...")
df.to_csv(caminho_saida, index=False, encoding='utf-8')

print(f"\n✅ PROCESSO CONCLUÍDO COM SUCESSO!")
print(f"Arquivo final gerado em: {caminho_saida}")
print(f"Total de linhas exportadas: {len(df)}")