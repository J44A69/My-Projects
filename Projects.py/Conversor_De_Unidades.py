import tkinter as tk
from tkinter import ttk

# Función para mostrar/ocultar tasa de cambio
def actualizar_tasa(*args):
    seleccion = conversion.get()
    if "Dólares" in seleccion or "Pesos" in seleccion:
        frame_tasa.pack(pady=5)
    else:
        frame_tasa.pack_forget()

# Función principal de conversión
def convertir():
    try:
        valor = float(entrada_valor.get())
        seleccion = conversion.get()
        resultado = None

        if seleccion == "Metros a Kilómetros":
            resultado = valor / 1000
        elif seleccion == "Kilómetros a Metros":
            resultado = valor * 1000
        elif seleccion == "Celsius a Fahrenheit":
            resultado = (valor * 9/5) + 32
        elif seleccion == "Fahrenheit a Celsius":
            resultado = (valor - 32) * 5/9
        elif seleccion == "Dólares a Pesos":
            tasa = float(entrada_tasa.get())
            resultado = valor * tasa
        elif seleccion == "Pesos a Dólares":
            tasa = float(entrada_tasa.get())
            resultado = valor / tasa
        else:
            resultado = "Conversión inválida"

        etiqueta_resultado.config(text=f"Resultado: {round(resultado, 2)}")

    except ValueError:
        etiqueta_resultado.config(text="❌ Valor o tasa inválidos")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Conversor de Unidades by J4 🔁")
ventana.geometry("330x350")

# Entrada del valor a convertir
tk.Label(ventana, text="Ingrese un valor:").pack(pady=5)
entrada_valor = tk.Entry(ventana)
entrada_valor.pack()

# Selección del tipo de conversión
conversion = ttk.Combobox(ventana, state="readonly", width=30)
conversion['values'] = [
    "Metros a Kilómetros",
    "Kilómetros a Metros",
    "Celsius a Fahrenheit",
    "Fahrenheit a Celsius",
    "Dólares a Pesos",
    "Pesos a Dólares"
]
conversion.current(0)
conversion.bind("<<ComboboxSelected>>", actualizar_tasa)
conversion.pack(pady=10)

# Campo de tasa de cambio (opcional, solo si aplica)
frame_tasa = tk.Frame(ventana)
tk.Label(frame_tasa, text="Tasa de cambio (1 USD = ? DOP):").pack()
entrada_tasa = tk.Entry(frame_tasa)
entrada_tasa.pack()

# Botón para convertir
boton_convertir = tk.Button(ventana, text="Convertir", command=convertir)
boton_convertir.pack(pady=10)

# Etiqueta de resultado
etiqueta_resultado = tk.Label(ventana, text="Resultado:", font=("Arial", 12))
etiqueta_resultado.pack(pady=10)

# Iniciar GUI
ventana.mainloop()
