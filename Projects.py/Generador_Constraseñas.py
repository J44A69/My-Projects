import tkinter as tk
from tkinter import messagebox
import string
import random

# <<Generador de contraseña>>
def generar_password():
    try:
        longitud = int(entry_longitud.get())
        usar_mayus = var_mayus.get()
        usar_minus = var_minus.get()
        usar_num = var_num.get()
        usar_sym = var_sym.get()

        if not (usar_mayus or usar_minus or usar_num or usar_sym):
            messagebox.showwarning("Advertencia", "Selecciona al menos una opción.")
            return

        caracteres = ""
        if usar_mayus:
            caracteres += string.ascii_uppercase
        if usar_minus:
            caracteres += string.ascii_lowercase
        if usar_num:
            caracteres += string.digits
        if usar_sym:
            caracteres += string.punctuation

        if longitud < 4:
            messagebox.showerror("Error", "La longitud debe ser mayor a 3.")
            return

        password = ''.join(random.choice(caracteres) for _ in range(longitud))
        entry_resultado.config(state="normal")
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, password)
        entry_resultado.config(state="readonly")
        ventana.clipboard_clear()
        ventana.clipboard_append(password)
        messagebox.showinfo("Copiado", "La contraseña se copió al portapapeles ✅")

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido para la longitud.")

# <<Interfaz>>
ventana = tk.Tk()
ventana.title("🔐 Generador de Contraseñas")
ventana.geometry("400x400")
ventana.configure(bg="#f1f1f1")

# <<Etiqueta principal>>
tk.Label(ventana, text="Generador de Contraseñas", font=("Helvetica", 16, "bold"), bg="#f1f1f1").pack(pady=10)

# <<Longitud>>
tk.Label(ventana, text="Longitud de la contraseña:", font=("Helvetica", 11), bg="#f1f1f1").pack()
entry_longitud = tk.Entry(ventana, font=("Helvetica", 11), justify="center")
entry_longitud.pack(pady=5)

# <<Checkboxes>>
var_mayus = tk.BooleanVar(value=True)
var_minus = tk.BooleanVar(value=True)
var_num = tk.BooleanVar(value=True)
var_sym = tk.BooleanVar(value=False)

tk.Checkbutton(ventana, text="Incluir Mayúsculas", variable=var_mayus, font=("Helvetica", 10), bg="#f1f1f1").pack()
tk.Checkbutton(ventana, text="Incluir Minúsculas", variable=var_minus, font=("Helvetica", 10), bg="#f1f1f1").pack()
tk.Checkbutton(ventana, text="Incluir Números", variable=var_num, font=("Helvetica", 10), bg="#f1f1f1").pack()
tk.Checkbutton(ventana, text="Incluir Símbolos", variable=var_sym, font=("Helvetica", 10), bg="#f1f1f1").pack()

# <<Botón generar>>
tk.Button(ventana, text="Generar Contraseña", command=generar_password,
          font=("Helvetica", 11), bg="#4CAF50", fg="white", padx=10, pady=5).pack(pady=15)

# <<Resultado>>
tk.Label(ventana, text="Contraseña generada:", font=("Helvetica", 11, "bold"), bg="#f1f1f1").pack(pady=5)
entry_resultado = tk.Entry(ventana, font=("Courier", 12), justify="center", width=30, state="readonly")
entry_resultado.pack()

ventana.mainloop()
