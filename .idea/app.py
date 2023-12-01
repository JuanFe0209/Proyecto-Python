print("Calculadora en Python")

num1 = input("Por favor ingrese un número:")
num2 = input("Ingrese un segundo número:")

operación = input("Por favor ingrese la operacíon que desea realizar con los número escogidos" + "\n" +
                  "1 = Suma\n" +
                  "2 = Resta\n"
                  "3 = Multiplicación\n"
                  "4 = División")

if num1 and num2 and operación:
    num1 = float(num1)
    num2 = float(num2)
    operación = int(operación)

    if operación == 1:
        resultado = num1 + num2
        print("El resultado de la operación es:", resultado)

    elif operación == 2:
        resultado = num1 - num2
        print("El resultado de la operación es:", resultado)

    elif operación == 3:
        resultado = num1 * num2
        print("El resultado de la operación es:", resultado)

    elif operación == 4:
        try:
            resultado = num1 / num2
            print("El resultado de la operación es:", resultado)
        except ZeroDivisionError:
            print("El número dos no puede ser cero para realizar una división")
    else:
        print ("Por favor escoja una opción correcta")
else:
    print("Por favor ingrese los datos solicitados")

