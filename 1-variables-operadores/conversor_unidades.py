def conversor_unidades():
    print("CONVERSOR DE UNIDADES")
    
    while True:
        print("\n1. Temperatura\n2. Monedas\n3. Longitudes\n4. Salir")
        opcion = input("Elige: ")
        
        if opcion == '1':
            # Conversión de temperatura
            temp = float(input("Grados Celsius: "))
            fahrenheit = (temp * 9/5) + 32
            kelvin = temp + 273.15
            print(f"{temp}°C = {fahrenheit:.1f}°F = {kelvin:.1f}K")
            
        elif opcion == '2':
            # Conversión de monedas
            clp = float(input("Pesos CLP: "))
            usd = clp * 0.00105
            eur = clp * 0.00098
            print(f"${clp:,.0f} CLP = ${usd:.2f} USD = €{eur:.2f} EUR")
            
        elif opcion == '3':
            # Conversión de longitudes
            metros = float(input("Metros: "))
            pies = metros * 3.281
            pulgadas = metros * 39.37
            print(f"{metros}m = {pies:.1f} ft = {pulgadas:.1f} in")
            
        elif opcion == '4':
            print("¡Adiós! 👋")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    conversor_unidades()