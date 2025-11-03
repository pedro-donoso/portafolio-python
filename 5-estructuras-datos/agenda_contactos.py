def agenda_contactos():
    print("AGENDA DE CONTACTOS")
    
    agenda = {}
    
    while True:
        print("\n1. Agregar\n2. Ver todos\n3. Buscar\n4. Salir")
        opcion = input("Elige: ")
        
        if opcion == '1':
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            agenda[nombre] = telefono
            print("Contacto agregado")
            
        elif opcion == '2':
            print("\n CONTACTOS:")
            for nombre, telefono in agenda.items():
                print(f"{nombre}: {telefono}")
                
        elif opcion == '3':
            nombre = input("Buscar contacto: ")
            if nombre in agenda:
                print(f"Encontrado: {agenda[nombre]}")
        
        elif opcion == '4':
            print('¡Adiós!')
            break
        
if __name__ == "__main__":
    agenda_contactos()