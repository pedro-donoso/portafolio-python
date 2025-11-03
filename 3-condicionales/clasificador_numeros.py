def clasificar_numero():
    print("CLASIFICADOR DE NÚMEROS")
    
    while True:
        try:
            num = float(input("\nNúmero (o 'q' para salir): "))
            
            if num > 0:
                print('POSITIVO', end='')
            elif num < 0:
                print('NEGATIVO', end='')
            else:
                print('CERO', end='')
                
                
            if num == int(num):
                if int(num) % 2 == 0:
                    print("| PAR", end="")
                else:
                    print("| IMPAR", end="")
                    
            print()
            
            
        except:
            print("¡Adiós!")
            break
        
if __name__ == "__main__":
    clasificar_numero()