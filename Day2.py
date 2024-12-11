
# Día 2. Tip Calculator

print("¡Bienvenido a la calculadora de propinas!")

factura = float(input("Factura total: $"))
propina = int(input("¿Cuánta propina le gustaría dar? ¿10, 12 o 15?: "))
personas = int(input("Cuántas personas se dividirán la cuenta: "))

total = (propina / 100 + 1) * factura / personas
print(f"Cada persona deberá pagar: ${total:.2f} pesos")
