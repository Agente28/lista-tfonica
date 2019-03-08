agenda = []

def pede_nome():
     return(input("Nome: "))

def pede_telefone():
     return(input("Telefone: "))

def mostra_dados(nome, telefone):
     print("Nome: %s Telefone: %s" % (nome, telefone))
     
def pesquisa(nome):
     mnome = nome.lower()
     for p, e in enumerate(agenda):
         if e[0].lower() == mnome:
               return p
     return None

def novo():
     global agenda
     nome = pede_nome()
     telefone = pede_telefone()
     agenda.append([nome, telefone])

def apaga():
     global agenda
     nome = pede_nome()
     p = pesquisa(nome)
     if p != None:
         del agenda[p]
     else:
         print("Nome não encontrado.")

def lista():
     print("\nAgenda\n\n------")
     for e in agenda:
         mostra_dados(e[0], e[1])
     print("------\n")

def valida_faixa_inteiro(pergunta, inicio, fim):
     while True:
         try:
               valor = int(input(pergunta))
               if inicio <= valor <= fim:
                   return(valor)
         except ValueError:
               print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))

def menu():
     print("""
   1 - Novo
   2 - Apaga
   3 - Lista
   0 - Sai
""")
     return valida_faixa_inteiro("Escolha uma opção: ",0,3)

while True:
     opção = menu()
     if opção == 0:
         break
     elif opção == 1:
         novo()
     elif opção == 2:
         apaga()
     elif opção == 3:
         lista()
