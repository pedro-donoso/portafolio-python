import math

def area_cuadrado(lado):
    return lado ** 2

def area_rectangulo(base, altura):
    return base * altura

def area_circulo(radio):
    return math.pi * radio ** 2

def area_triangulo(base, altura):
    return (base * altura) / 2

def menu_areas():
    print("CALCULADORA DE ÁREAS")
    
    while True:
        print("\n1. Cuadrado\n2. Rectángulo\n3. Círculo\n4. Triángulo\n5. Salir")
        opcion = input("Elige figura: ")
        
        if opcion == '1':
            lado = float(input("Lado: "))
            print(f"Área: {area_cuadrado(lado):.2f}")
            
        elif opcion == '2':
            base = float(input("Base: "))
            altura = float(input("Altura: "))
            print(f"Área: {area_rectangulo(base, altura):.2f}")
            
        elif opcion == '3':
            radio = float(input("Radio: "))
            print(f"Área: {area_circulo(radio):.2f}")
            
        elif opcion == '4':
            base = float(input("Base: "))
            altura = float(input("Altura: "))
            print(f"Área: {area_triangulo(base, altura):.2f}")
            
        elif opcion == '5':
            print('¡Adiós!')
            break
        
if __name__ == '__main__':
    menu_areas()