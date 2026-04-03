import pandas as pd

df = pd.read_csv("clientes.csv", engine="python")
df = df.replace('"', '', regex=True)

df = df["id,nome,data_compra,status,plataforma,produto,regiao,valor"].str.split(",", expand=True)
df.columns = ["id","nome","data_compra","status","plataforma","produto","regiao","valor"]

df["valor"] = df["valor"].astype(float)
df["data_compra"] = pd.to_datetime(df["data_compra"], errors="coerce")

df["nome"] = df["nome"].str.title()
df["produto"] = df["produto"].str.title()
df["regiao"] = df["regiao"].str.title()

df["status"] = df["status"].str.lower().replace({
    "pend.": "pendente",
    "pendente": "pendente",
    "entregue": "entregue"
})

df["plataforma"] = df["plataforma"].str.lower().replace({
    "ios": "iOS",
    "android": "Android"
})

df.to_csv("clientes_tratado.csv", index=False)

print("Arquivo criado com sucesso!")