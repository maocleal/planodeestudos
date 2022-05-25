import pandas as pd
import lendoXML

turno = []
semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
disciplinas = []
dificuldades = []
professores = []

planodeestudos = pd.read_excel("planodeestudos.xlsx")
atendimentos = pd.read_excel("Pasta1 - Cópia (3).xlsx")

tabela = pd.read_excel("Pasta1 - Cópia.xlsx")

print("Escolha as disciplinas por ordem de dificuldade:")
for c in range(len(disciplinas)):
    print(f"{c + 1} {disciplinas[c]}")

escolha = map(int, input("Digite os números das disciplinas separados por vírgula:\n> ").split(","))
for item in escolha:
    dificuldades.append(disciplinas[item - 1])

print(dificuldades)
planodeestudos.to_excel("planodeestudos - Cópia.xlsx", index = False)

#Procurar o horário de cada professor
for disciplina in dificuldades:
    for dia in semana:
        print(dia)
        print(len(atendimentos[dia]))
        for i in range(len(atendimentos[dia])):
            if "Atendimento" in str(atendimentos[dia][i]):
                pass
            print(str(atendimentos[dia][i]))
            