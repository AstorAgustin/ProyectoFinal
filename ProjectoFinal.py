"""
Nombre: Axel Agustin Astorga Vecchio
Comision: Martes - Virtual

"""
import pandas as pd

# Lista para almacenar los gastos
gastos = []

# Función para mostrar el menú principal
def menu():
    while True:
        print("\n=== Seguimiento de Gastos ===")
        print("1. Registrar gasto")
        print("2. Ver gastos")
        print("3. Exportar a Excel")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            registrar_gasto()
        elif opcion == "2":
            ver_gastos()
        elif opcion == "3":
            exportar_excel()
        elif opcion == "4":
            print("¡Adiós! Gracias por usar la aplicación.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Función para registrar un gasto
def registrar_gasto():
    print("\n--- Registrar un nuevo gasto ---")
    try:
        fecha = input("Fecha (DD-MM-YYYY): ")
        categoria = input("Categoría: ")
        monto = float(input("Monto: "))
        descripcion = input("Descripción: ")

        gasto = {"Fecha": fecha, "Categoría": categoria, "Monto": monto, "Descripción": descripcion}
        gastos.append(gasto)
        print("¡Gasto registrado exitosamente!")
    except ValueError:
        print("Error: El monto debe ser un número.")

# Función para ver los gastos registrados
def ver_gastos():
    if not gastos:
        print("\nNo hay gastos registrados.")
        return
    
    print("\n--- Lista de Gastos ---")
    for i, gasto in enumerate(gastos, start=1):
        print(f"{i}. Fecha: {gasto['Fecha']}, Categoría: {gasto['Categoría']}, Monto: {gasto['Monto']}, Descripción: {gasto['Descripción']}")

# Función para exportar los gastos a un archivo Excel
def exportar_excel():
    if not gastos:
        print("\nNo hay datos para exportar.")
        return
    
    # Crear un DataFrame de Pandas y exportar a Excel
    df = pd.DataFrame(gastos)
    try:
        df.to_excel("gastos.xlsx", index=False)
        print("\n¡Datos exportados exitosamente a 'gastos.xlsx'!")
    except Exception as e:
        print(f"\nError al exportar los datos: {e}")

# Punto de entrada principal
if __name__ == "__main__":
    menu()