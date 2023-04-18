from conversao import converte_f_para_c, converte_c_para_f

# Fluxo
temp_type = input("Digite F para Fahrenheit\n" "Digite C para Celsius: ")

temperatura = float(input("Digite a temperatura: "))

match (temp_type):
    case "F":
        resultado = converte_f_para_c(temperatura)
        print(f"a temperatura convertidade é {resultado}")
    case "C":
        resultado = converte_c_para_f(temperatura)
        print(f"a temperatura convertidade é {resultado}")
    case _:
        print("Digite F ou C. Tá errado!!!!")
