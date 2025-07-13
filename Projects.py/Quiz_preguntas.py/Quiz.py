import tkinter as tk
from tkinter import messagebox
import pandas as pd

# Cargar preguntas
df = pd.read_csv("preguntas_500_categorias.csv")
categorias_disponibles = df["categoria"].unique()

# Variables globales
puntaje = 0
racha = 0
mejor_racha = 0
preguntas_actuales = []
pregunta_index = 0

def iniciar_quiz(categoria, cantidad=10):
    global preguntas_actuales, puntaje, racha, mejor_racha, pregunta_index
    puntaje = 0
    racha = 0
    mejor_racha = 0
    pregunta_index = 0
    preguntas_actuales = df[df["categoria"] == categoria].sample(n=cantidad).reset_index(drop=True)
    mostrar_pregunta()

def mostrar_pregunta():
    global pregunta_index
    if pregunta_index >= len(preguntas_actuales):
        messagebox.showinfo("¡Quiz finalizado!",
                            f"Puntaje: {puntaje}/{len(preguntas_actuales)}\n"
                            f"Mejor racha: {mejor_racha}")
        menu_categoria()
        return

    row = preguntas_actuales.iloc[pregunta_index]
    lbl_pregunta.config(text=row['pregunta'])
    btn_a.config(text=f"A) {row['opcion_a']}", command=lambda: verificar_respuesta('A'))
    btn_b.config(text=f"B) {row['opcion_b']}", command=lambda: verificar_respuesta('B'))
    btn_c.config(text=f"C) {row['opcion_c']}", command=lambda: verificar_respuesta('C'))
    btn_d.config(text=f"D) {row['opcion_d']}", command=lambda: verificar_respuesta('D'))
    lbl_status.config(text=f"Puntaje: {puntaje}  |  Racha: {racha}  |  Mejor racha: {mejor_racha}")

def verificar_respuesta(respuesta_usuario):
    global puntaje, racha, mejor_racha, pregunta_index
    correcta = preguntas_actuales.iloc[pregunta_index]["respuesta"]
    if respuesta_usuario == correcta:
        puntaje += 1
        racha += 1
        mejor_racha = max(racha, mejor_racha)
        messagebox.showinfo("✅ Correcto", "¡Bien hecho!")
    else:
        racha = 0
        messagebox.showinfo("❌ Incorrecto", f"La respuesta correcta era {correcta}.")
    pregunta_index += 1
    mostrar_pregunta()

def menu_categoria():
    for widget in frame_main.winfo_children():
        widget.destroy()
    lbl_title = tk.Label(frame_main, text="Selecciona una categoría", font=("Arial", 16))
    lbl_title.pack(pady=10)
    for cat in categorias_disponibles:
        btn = tk.Button(frame_main, text=cat, width=30,
                        command=lambda c=cat: (frame_main.pack_forget(), frame_quiz.pack(), iniciar_quiz(c)))
        btn.pack(pady=5)

# Interfaz Tkinter
root = tk.Tk()
root.title("Quiz por Categoría")
root.geometry("600x400")

frame_main = tk.Frame(root)
frame_quiz = tk.Frame(root)

# Widgets del quiz
lbl_pregunta = tk.Label(frame_quiz, text="", wraplength=500, font=("Arial", 14))
lbl_pregunta.pack(pady=20)

btn_a = tk.Button(frame_quiz, text="", width=50)
btn_a.pack(pady=5)
btn_b = tk.Button(frame_quiz, text="", width=50)
btn_b.pack(pady=5)
btn_c = tk.Button(frame_quiz, text="", width=50)
btn_c.pack(pady=5)
btn_d = tk.Button(frame_quiz, text="", width=50)
btn_d.pack(pady=5)

lbl_status = tk.Label(frame_quiz, text="", font=("Arial", 12))
lbl_status.pack(pady=10)

frame_main.pack()
menu_categoria()
root.mainloop()
