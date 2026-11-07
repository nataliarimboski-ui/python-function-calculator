import math

def menu_funcoes():
    print("\\n--- ANALISADOR DE FUNÇÕES ---")
    print("1. Função de 1º Grau (f(x) = ax + b)")
    print("2. Função de 2º Grau (f(x) = ax² + bx + c)")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        a = float(input("Digite o coeficiente 'a': "))
        b = float(input("Digite o coeficiente 'b': "))

        if a == 0:
            print("Não é uma função de 1º grau (a constante f(x) = b).")
        else:
            raiz = -b / a
            tipo = "Crescente" if a > 0 else "Decrescente"
            print(f"\\nResultados:")
            print(f"- Tipo: Função {tipo}")
            print(f"- Raiz (onde f(x) = 0): x = {raiz:.2f}")
            print(f"- Intersecção com eixo Y: (0, {b})")

    elif opcao == "2":
        a = float(input("Digite o coeficiente 'a': "))
        b = float(input("Digite o coeficiente 'b': "))
        c = float(input("Digite o coeficiente 'c': "))

        if a == 0:
            print("Se 'a' é zero, use a opção de 1º grau.")
            return

        delta = (b ** 2) - (4 * a * c)
        xv = -b / (2 * a)
        yv = -delta / (4 * a)
        concavidade = "Voltada para CIMA" if a > 0 else "Voltada para BAIXO"

        print(f"\\nResultados:")
        print(f"- Concavidade: {concavidade}")
        print(f"- Delta (Δ): {delta:.2f}")
        print(f"- Vértice: V({xv:.2f}, {yv:.2f})")

menu_funcoes()
