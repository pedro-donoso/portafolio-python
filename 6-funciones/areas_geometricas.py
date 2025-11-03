def conversor_unidades():
    print("CONVERSOR DE UNIDADES")
    
    while True:
        print("\n1. Temperatura\n2. Monedas\n3. Longitudes\n4. Salir")
        opcion = input("Elige: ")
        
        if opcion == '1':
            temp = float(input("Grados Celsius: "))
            fahrenheit = (temp * 9/5) + 32
            kelvin = temp + 273.15
            print(f"{temp}ºC = {fahrenheit:.1f}ºF = {kelvin:.1f}K")
            
            
        elif opcion == '2':
            clp = float(input("Pesos CLP: "))
            usd = clp * 0.058
            eur = clp * 0.053
            print(f"${clp} CLP = ${usd:.2f} USD = €{eur:.2f} EUR")