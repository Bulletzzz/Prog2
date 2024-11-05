import csv
import pandas as pd

# Dados dos carros
carros = [
    {"marca": "Ferrari", "velocidade final": 340, "potência": 800, "categoria": "coupé esportivo"},
    {"marca": "Volkswagen", "velocidade final": 204, "potência": 150, "categoria": "SUV"},
    {"marca": "Mercedes", "velocidade final": 254, "potência": 255, "categoria": "sedan"},
    {"marca": "Hyundai", "velocidade final": 230, "potência": 204, "categoria": "Hatchback"},
]

arquivo_csv = "carros.csv"

with open(arquivo_csv, mode="w", newline="", encoding='utf-8') as arquivo:
    escritor_csv = csv.DictWriter(arquivo, fieldnames=["marca", "velocidade final", "potência", "categoria"])
    escritor_csv.writeheader()
    for carro in carros:
        escritor_csv.writerow(carro)

print(f"Arquivo '{arquivo_csv}' criado com sucesso!")

try:
    df = pd.read_csv(arquivo_csv, encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv(arquivo_csv, encoding='latin1')

mediap = df["potência"].mean()

df.loc[len(df)] = ["Média", "", f"{mediap:.2f}", ""]

df.to_csv(arquivo_csv, index=False, encoding='utf-8') 
print("Média de potência adicionada ao arquivo CSV com sucesso!")