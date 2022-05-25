from xml.dom import minidom

def verificaTurma(nome):
    if not "AEE" in nome:
        return True
    else:
        return False

def retornaNomeTurma(objTurma):
    return objTurma.getAttribute("name")

def objToList(turmas):
    lista = []
    for turma in turmas:
        if verificaTurma(retornaNomeTurma(turma)):
            lista.append(retornaNomeTurma(turma))
    return lista

def retornaObjTurma(listaObjTurmas, nome):
    for turma in listaObjTurmas:
        if nome == turma.getAttribute("name"):
            return turma

def retornaListaDisciplinas(objTurmas, nome):
    disciplinasNome = []
    turma = retornaObjTurma(objTurmas, nome)
    disciplinas = turma.getElementsByTagName("Subject")
    for disciplina in disciplinas:
        if not disciplina.getAttribute("name") in disciplinasNome:
            disciplinasNome.append(disciplina.getAttribute("name"))

    return disciplinasNome

doc = minidom.parse("important/ifba.sea.2022v1_subgroups.xml")
turmas = doc.getElementsByTagName("Subgroup")

turmasTexto = objToList(turmas)
for c in range(len(turmasTexto)):
    print(f"[ {c + 1} ] {turmasTexto[c]}".replace("Subgrupo Automático", ""))

turmaEscolhida = int(input("Escolha a sua turma: "))

disciplinas = retornaListaDisciplinas(turmas, turmasTexto[turmaEscolhida - 1])

# for turma in turmas:
#     if verificaTurma(turma.getAttribute("name")):
#         print(turma.getAttribute("name"))
#         print(turma.getElementsByTagName("Day")[0].getAttribute("name"))
#         print(turma.getElementsByTagName("Hour")[0].getAttribute("name"))
#         print(turma.getElementsByTagName("Teacher")[0].getAttribute("name"))
#         print(turma.getElementsByTagName("Subject")[0].getAttribute("name"))
#         print(turma.getElementsByTagName("Activity_Tag")[0].getAttribute("name"))
#         print("\n")

#exemplo de pegar cada um dos dados do xml da turma
# print(turmas)
# print(turmas[0].getAttribute("name"))
# print(turmas[0].getElementsByTagName("Day")[0].getAttribute("name"))
# print(turmas[0].getElementsByTagName("Hour")[0].getAttribute("name"))
# print(turmas[0].getElementsByTagName("Teacher")[0].getAttribute("name"))
# print(turmas[0].getElementsByTagName("Subject")[0].getAttribute("name"))
# print(turmas[0].getElementsByTagName("Activity_Tag")[0].getAttribute("name"))
