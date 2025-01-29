# Día 2. Calculadora de propinas: Pide el total de la factura, pregunta que porcentaje de propina quiere dar 10, 12 0 15%, pregunta entre cuántas personas se repartiran la cuenta y muestra cuanto debe pagar cada persona

print("¡Bienvenido a la calculadora de propinas!")

factura = float(input("Factura total: $"))
propina = int(input("¿Cuánta propina le gustaría dar? ¿10, 12 o 15?: "))
personas = int(input("Cuántas personas se dividirán la cuenta: "))

total = (propina / 100 + 1) * factura / personas
print(f"Cada persona debe pagar: ${total:.2f} pesos")