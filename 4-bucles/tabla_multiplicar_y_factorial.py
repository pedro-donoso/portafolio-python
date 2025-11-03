def tabla_multiplicar():
    print("TABLAS DE MULTIPLICAR")
    

    numero = int(input("Número: "))
    print(f"\nTabla del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
        
        
def factorial():
    print("\nFACTORIAL")
        
    n = int(input("Número: "))
    factorial = 1
    i = 1
    
    while i <= n:
        factorial *= i
        i += 1
                
    print(f"{n}! = {factorial}")
        
if __name__ == "__main__":
    tabla_multiplicar()
    factorial()
    
    
