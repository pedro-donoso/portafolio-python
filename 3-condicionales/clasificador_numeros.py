def clasificar_numero():
    print("CLASIFICADOR DE NÚMEROS")
    
    while True:
        try:
            num = float(input("\nNúmero (o 'q' para salir): "))
            
            if num > 0:
                print("POSITIVO", end="")
            elif num < 0:
                print("NEGATIVO", end="")
            else:
                print("CERO", end="")
                
                
            