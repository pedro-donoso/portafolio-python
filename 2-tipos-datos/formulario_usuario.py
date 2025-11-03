def formulario():
    print("FORMULARIO DE USUARIO")
    
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    altura = float(input("Altura (m): "))
    es_estudiante = input("¿Eres estudiante? (s/n): ").lower() == 's'
    
    print(f"\nDatos registrados:")
    print(f"Nombre: {nombre} ({type(nombre)})")
    print(f"Edad: {edad} años ({type(edad)})")
    print(f"Altura: {altura}m ({type(altura)})")
    print(f"Estudiante: {'Sí' if es_estudiante else 'No'} ({type(es_estudiante)})")
    
    
if __name__ == "__main__":
    formulario()