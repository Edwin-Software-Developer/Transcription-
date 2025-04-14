import tkinter as tk
from tkinter import filedialog, messagebox
import whisper
import os

def transcribir_audio():
    ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos de Audio", "*.mp3;*.wav;*.m4a")])
    if not ruta_archivo:
        return
    
    messagebox.showinfo("Transcripción", "Transcribiendo audio, por favor espera...")
    modelo = whisper.load_model("base")
    resultado = modelo.transcribe(ruta_archivo)
    
    salida_texto.delete("1.0", tk.END)
    salida_texto.insert(tk.END, resultado["text"])
    
    messagebox.showinfo("Éxito", "Transcripción completada!")

def guardar_transcripcion():
    texto = salida_texto.get("1.0", tk.END).strip()
    if not texto:
        messagebox.showwarning("Advertencia", "No hay texto para guardar!")
        return
    
    ruta_guardado = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de Texto", "*.txt")])
    if ruta_guardado:
        with open(ruta_guardado, "w", encoding="utf-8") as archivo:
            archivo.write(texto)
        messagebox.showinfo("Éxito", "Transcripción guardada!")

# Crear interfaz gráfica
ventana = tk.Tk()
ventana.title("Transcriptor de Audio a Texto")
ventana.geometry("500x400")

marco = tk.Frame(ventana)
marco.pack(pady=20)

btn_seleccionar = tk.Button(marco, text="Seleccionar Archivo de Audio", command=transcribir_audio)
btn_seleccionar.pack(side=tk.LEFT, padx=10)

btn_guardar = tk.Button(marco, text="Guardar Transcripción", command=guardar_transcripcion)
btn_guardar.pack(side=tk.RIGHT, padx=10)

salida_texto = tk.Text(ventana, wrap=tk.WORD, height=15, width=50)
salida_texto.pack(padx=10, pady=10)

ventana.mainloop()