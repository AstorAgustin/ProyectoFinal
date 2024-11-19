import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

# Lista para almacenar los gastos
gastos = []

# Función para registrar un gasto
def registrar_gasto():
    fecha = entry_fecha.get()
    categoria = entry_categoria.get()
    try:
        monto = float(entry_monto.get())
    except ValueError:
        messagebox.showerror("Error", "El monto debe ser un número válido.")
        return
    descripcion = entry_descripcion.get()
    
    if not fecha or not categoria or not descripcion:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return

    gasto = {"Fecha": fecha, "Categoría": categoria, "Monto": monto, "Descripción": descripcion}
    gastos.append(gasto)
    messagebox.showinfo("Éxito", "¡Gasto registrado exitosamente!")
    limpiar_campos()

# Función para limpiar los campos después de registrar
def limpiar_campos():
    entry_fecha.delete(0, tk.END)
    entry_categoria.delete(0, tk.END)
    entry_monto.delete(0, tk.END)
    entry_descripcion.delete(0, tk.END)

# Función para mostrar los gastos registrados
def ver_gastos():
    if not gastos:
        messagebox.showinfo("Información", "No hay gastos registrados.")
        return
    
    ventana_ver = tk.Toplevel(root)
    ventana_ver.title("Gastos registrados")
    
    tree = ttk.Treeview(ventana_ver, columns=("Fecha", "Categoría", "Monto", "Descripción"), show="headings")
    tree.heading("Fecha", text="Fecha")
    tree.heading("Categoría", text="Categoría")
    tree.heading("Monto", text="Monto")
    tree.heading("Descripción", text="Descripción")
    
    for gasto in gastos:
        tree.insert("", tk.END, values=(gasto["Fecha"], gasto["Categoría"], gasto["Monto"], gasto["Descripción"]))
    
    tree.pack(fill=tk.BOTH, expand=True)

# Función para exportar los gastos a un archivo Excel
def exportar_excel():
    if not gastos:
        messagebox.showinfo("Información", "No hay datos para exportar.")
        return

    df = pd.DataFrame(gastos)
    try:
        df.to_excel("gastos.xlsx", index=False)
        messagebox.showinfo("Éxito", "¡Datos exportados exitosamente a 'gastos.xlsx'!")
    except Exception as e:
        messagebox.showerror("Error", f"Error al exportar los datos: {e}")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Seguimiento de Gastos")
root.geometry("400x400")

# Etiquetas y entradas para registrar gastos
tk.Label(root, text="Fecha (DD-MM-YYYY):").pack(pady=5)
entry_fecha = tk.Entry(root)
entry_fecha.pack(pady=5)

tk.Label(root, text="Categoría:").pack(pady=5)
entry_categoria = tk.Entry(root)
entry_categoria.pack(pady=5)

tk.Label(root, text="Monto:").pack(pady=5)
entry_monto = tk.Entry(root)
entry_monto.pack(pady=5)

tk.Label(root, text="Descripción:").pack(pady=5)
entry_descripcion = tk.Entry(root)
entry_descripcion.pack(pady=5)

# Botones para las acciones
btn_registrar = tk.Button(root, text="Registrar Gasto", command=registrar_gasto)
btn_registrar.pack(pady=10)

btn_ver = tk.Button(root, text="Ver Gastos", command=ver_gastos)
btn_ver.pack(pady=10)

btn_exportar = tk.Button(root, text="Exportar a Excel", command=exportar_excel)
btn_exportar.pack(pady=10)

# Ejecutar el loop principal de Tkinter
root.mainloop()