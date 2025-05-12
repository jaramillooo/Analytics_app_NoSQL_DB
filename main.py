def main_menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Cassandra")
        print("2. MongoDB")
        print("3. Dgraph")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            cassandra_menu()
        elif opcion == "2":
            mongo_menu()
        elif opcion == "3":
            dgraph_menu()
        elif opcion == "0":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")


def cassandra_menu():
    while True:
        print("\n--- Menú Cassandra ---")
        print("1. Conectar")
        print("2. Crear tabla")
        print("3. Volver al menú principal")
        opcion = input("Opción: ")

        if opcion == "3":
            break
        else:
            print(f"Seleccionaste opción {opcion} en Cassandra.")


def mongo_menu():
    while True:
        print("\n--- Menú MongoDB ---")
        print("1. Conectar")
        print("2. Crear colección")
        print("3. Volver al menú principal")
        opcion = input("Opción: ")

        if opcion == "3":
            break
        else:
            print(f"Seleccionaste opción {opcion} en MongoDB.")


def dgraph_menu():
    while True:
        print("\n--- Menú Dgraph ---")
        print("1. Crear esquema")
        print("2. Consultar usuarios")
        print("3. Volver al menú principal")
        opcion = input("Opción: ")

        if opcion == "3":
            break
        else:
            print(f"Seleccionaste opción {opcion} en Dgraph.")


if __name__ == "__main__":
    main_menu()
