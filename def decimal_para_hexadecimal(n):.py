def decimal_para_hexadecimal(n):
    simbolos_hex = '0123456789ABCDEF'
   
    if n == 0:
        return '0'

    resultado = ''
   
    while n > 0:
        resto = n % 16
        resultado = simbolos_hex[resto] + resultado
        n = n // 16
   
    return resultado

numero_decimal = int(input("Digite um número decimal: "))

numero_hexadecimal = decimal_para_hexadecimal(numero_decimal)

print(f"O número {numero_decimal} em hexadecimal: {numero_hexadecimal}")