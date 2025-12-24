import pandas as pd
import os

# 1. MAPEAMENTO DE CAMINHOS
diretorio_script = os.path.dirname(os.path.abspath(__file__))
projeto_raiz = os.path.dirname(diretorio_script)

# O input agora é a SILVER (dado limpo)
caminho_silver = os.path.join(projeto_raiz, 'data', 'silver', 'vendas_janeiro_2024_limpo.csv')

# O output será na GOLD
caminho_gold_faturamento = os.path.join(projeto_raiz, 'data', 'gold', 'faturamento_por_produto.csv')
caminho_gold_canais = os.path.join(projeto_raiz, 'data', 'gold', 'performance_canais.csv')

# Carregando o dado limpo
df = pd.read_csv(caminho_silver)

# Criando a coluna de Faturamento Total por linha
df['faturamento_total'] = df['preco_unitario'] * df['quantidade']

print("\nGerando indicadores para a camada Gold...")

# KPI 1: Faturamento Total por Produto e Marca
# O sum() soma os valores financeiros
faturamento_produto = df.groupby(['produto', 'marca'])['faturamento_total'].sum().reset_index()

# KPI 2: Volume de Vendas por Canal de Venda
# O count() conta quantas vendas aconteceram em cada canal
performance_canais = df.groupby('canal_venda')['id_venda'].count().reset_index()
performance_canais.columns = ['canal_venda', 'quantidade_vendas']

print("KPIs calculados com sucesso!")

# 2. SALVAMENTO
faturamento_produto.to_csv(caminho_gold_faturamento, index=False)
performance_canais.to_csv(caminho_gold_canais, index=False)

print(f"\n✅ CAMADA GOLD GERADA!")
print(f"Arquivos disponíveis em: {os.path.join(projeto_raiz, 'data', 'gold')}")