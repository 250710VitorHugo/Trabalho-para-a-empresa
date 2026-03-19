import pandas as pd

# 1. Carregar o seu arquivo atualizado
df = pd.read_csv("historico_total.csv", encoding="latin1")

# 2. Remover registros com erro "#N/D" (Erro do Excel)
df = df[df["cp"] != "#N/D"]

# 3. Remover registros com o caractere "-" (Placeholder vazio)
df = df[df["cp"] != "-"]

# 4. Remover valores nulos/vazios (NaN) nas colunas essenciais
# Isso evita o erro "Input contains NaN" no treinamento
df = df.dropna(subset=["cp", "descricao_do_produto"])

# 5. Salvar o arquivo limpo para o treinamento
df.to_csv("historico_treino_lim.csv", index=False)

# Conferência final
print("--- Limpeza Concluída ---")
print(f"Total de registros após limpeza: {len(df)}")
print(f"Total de CPs únicas: {df['cp'].nunique()}")
print(f"CPs com 50 ou mais exemplos: {len(df['cp'].value_counts()[df['cp'].value_counts() >= 50])}")


