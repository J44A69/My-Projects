import tkinter as tk
from tkinter import messagebox
import string
import random
import os

ARCHIVO_GUARDADO = "contraseñas_guardadas.txt"

def generar_password():
    try:
        longitud = int(entry_longitud.get())
        usar_mayus = var_mayus.get()
        usar_minus = var_minus.get()
        usar_num = var_num.get()
        usar_sym = var_sym.get()

        if longitud < 4:
            messagebox.showerror("Error", "La longitud debe ser mayor o igual a 4.")
            return

        if not (usar_mayus or usar_minus or usar_num or usar_sym):
            messagebox.showwarning("Advertencia", "Selecciona al menos una opción.")
            return

        caracteres = ""
        grupo_caracteres = []

        if usar_mayus:
            caracteres += string.ascii_uppercase
            grupo_caracteres.append(string.ascii_uppercase)
        if usar_minus:
            caracteres += string.ascii_lowercase
            grupo_caracteres.append(string.ascii_lowercase)
        if usar_num:
            caracteres += string.digits
            grupo_caracteres.append(string.digits)
        if usar_sym:
            caracteres += string.punctuation
            grupo_caracteres.append(string.punctuation)

        if longitud < len(grupo_caracteres):
            messagebox.showerror("Error", f"La longitud debe ser al menos {len(grupo_caracteres)} para incluir todos los tipos seleccionados.")
            return

        password_chars = [random.choice(grupo) for grupo in grupo_caracteres]
        password_chars += [random.choice(caracteres) for _ in range(longitud - len(password_chars))]
        random.shuffle(password_chars)
        password = ''.join(password_chars)

        entry_resultado.config(state="normal")
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, password)
        entry_resultado.config(state="readonly")

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido para la longitud.")

def copiar_password():
    password = entry_resultado.get()
    if password:
        ventana.clipboard_clear()
        ventana.clipboard_append(password)
        messagebox.showinfo("Copiado", "La contraseña se copió al portapapeles ✅")
    else:
        messagebox.showwarning("Aviso", "No hay contraseña para copiar.")

def limpiar_campos():
    entry_longitud.delete(0, tk.END)
    entry_resultado.config(state="normal")
    entry_resultado.delete(0, tk.END)
    entry_resultado.config(state="readonly")

def guardar_password():
    password = entry_resultado.get()
    if not password:
        messagebox.showwarning("Aviso", "Genera una contraseña primero para guardar.")
        return
    
    try:
        with open(ARCHIVO_GUARDADO, "a", encoding="utf-8") as f:
            f.write(password + "\n")
        messagebox.showinfo("Guardado", f"Contraseña guardada en:\n{os.path.abspath(ARCHIVO_GUARDADO)}")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar la contraseña:\n{e}")

ventana = tk.Tk()
ventana.title("🔐 Generador de Contraseñas Mejorado")
ventana.geometry("420x470")
ventana.configure(bg="#f0f0f0")

tk.Label(ventana, text="Generador de Contraseñas", font=("Helvetica", 16, "bold"), bg="#f0f0f0").pack(pady=10)

tk.Label(ventana, text="Longitud de la contraseña:", font=("Helvetica", 11), bg="#f0f0f0").pack()
entry_longitud = tk.Entry(ventana, font=("Helvetica", 11), justify="center")
entry_longitud.pack(pady=5)

var_mayus = tk.BooleanVar(value=True)
var_minus = tk.BooleanVar(value=True)
var_num = tk.BooleanVar(value=True)
var_sym = tk.BooleanVar(value=False)

tk.Checkbutton(ventana, text="Incluir Mayúsculas", variable=var_mayus, font=("Helvetica", 10), bg="#f0f0f0").pack()
tk.Checkbutton(ventana, text="Incluir Minúsculas", variable=var_minus, font=("Helvetica", 10), bg="#f0f0f0").pack()
tk.Checkbutton(ventana, text="Incluir Números", variable=var_num, font=("Helvetica", 10), bg="#f0f0f0").pack()
tk.Checkbutton(ventana, text="Incluir Símbolos", variable=var_sym, font=("Helvetica", 10), bg="#f0f0f0").pack()

tk.Button(ventana, text="Generar Contraseña", command=generar_password,
          font=("Helvetica", 11), bg="#4CAF50", fg="white", padx=10, pady=5).pack(pady=10)

tk.Label(ventana, text="Contraseña generada:", font=("Helvetica", 11, "bold"), bg="#f0f0f0").pack(pady=5)
entry_resultado = tk.Entry(ventana, font=("Courier", 12), justify="center", width=30, state="readonly")
entry_resultado.pack()

frame_botones = tk.Frame(ventana, bg="#f0f0f0")
frame_botones.pack(pady=10)

btn_copiar = tk.Button(frame_botones, text="Copiar al portapapeles", command=copiar_password,
                       font=("Helvetica", 10), bg="#2196F3", fg="white", padx=10, pady=5)
btn_copiar.grid(row=0, column=0, padx=5)

btn_limpiar = tk.Button(frame_botones, text="Limpiar campos", command=limpiar_campos,
                        font=("Helvetica", 10), bg="#f44336", fg="white", padx=10, pady=5)
btn_limpiar.grid(row=0, column=1, padx=5)

btn_guardar = tk.Button(frame_botones, text="Guardar contraseña", command=guardar_password,
                        font=("Helvetica", 10), bg="#607D8B", fg="white", padx=10, pady=5)
btn_guardar.grid(row=1, column=0, columnspan=2, pady=5)

ventana.mainloop()
