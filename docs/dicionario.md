# Dicionário de Dados - Vendas Janeiro 2024

| Coluna | Descrição | Tipo Original | Tipo Final (Silver) |
| :--- | :--- | :--- | :--- |
| **id_venda** | Identificador único da transação | Float | Integer |
| **data_venda** | Data da ocorrência da venda | Object (Texto) | Datetime |
| **tipo_cliente** | Categoria do comprador (consumidor_final ou comercio) | Object | Object |
| **produto** | Item vendido (ex: gas_p13, agua_500ml) | Object | Object |
| **preco_unitario** | Valor de uma unidade do produto | Object (R$) | Float |
| **faturamento_total** | Cálculo de preço_unitario * quantidade | N/A | Float (Gold) |
| **validacao_cnpj** | Flag que indica se um comércio possui CNPJ preenchido | N/A | String (Flag) |