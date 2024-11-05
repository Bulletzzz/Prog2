import csv

def fibo(n): 
    resultado = []
    a, b = 1, 1
    for _ in range(n):
        resultado.append(a)
        a, b = b, a + b
    return resultado

num = 20
resultfibo = fibo(num)

arquivo_fibo = "fibonacci.csv"

with open(arquivo_fibo, mode="w", newline="", encoding='utf-8') as arquivo:
    escrever_csv = csv.writer(arquivo)
    escrever_csv.writerow(["Position", "Number"])

    for i, numero in enumerate(resultfibo):
        escrever_csv.writerow([i + 1, numero])

print(f"Arquivo '{arquivo_fibo}' criado com sucesso!")
