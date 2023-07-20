from operations import Operations

class Calculator:
    def __init__(self):
        self.operations = Operations()

    def display_menu(self):
        print("Selecione a operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Potência")
        print("6. Raiz Quadrada")
        print("7. Logaritmo")
        print("8. Fatorial")
        print("0. Sair")

    def get_input(self):
        return int(input("Digite a opção desejada: "))

    def run(self):
        while True:
            self.display_menu()
            choice = self.get_input()

            if choice == 0:
                print("Saindo da calculadora.")
                break
            elif choice in [1, 2, 3, 4]:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                if choice == 1:
                    result = self.operations.add(num1, num2)
                elif choice == 2:
                    result = self.operations.subtract(num1, num2)
                elif choice == 3:
                    result = self.operations.multiply(num1, num2)
                elif choice == 4:
                    result = self.operations.divide(num1, num2)
            elif choice == 5:
                num1 = float(input("Digite a base: "))
                num2 = float(input("Digite o expoente: "))
                result = self.operations.power(num1, num2)
            elif choice == 6:
                num = float(input("Digite o número: "))
                result = self.operations.square_root(num)
            elif choice == 7:
                num = float(input("Digite o número: "))
                base = float(input("Digite a base do logaritmo: "))
                result = self.operations.logarithm(num, base)
            elif choice == 8:
                num = int(input("Digite o número inteiro: "))
                result = self.operations.factorial(num)
            else:
                print("Opção inválida. Tente novamente.")

            print("Resultado:", result)
