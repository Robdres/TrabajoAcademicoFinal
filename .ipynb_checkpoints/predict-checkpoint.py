#cargar modelo
import joblib
import tkinter as tk
from tkinter import messagebox,ttk

model = joblib.load('modelo_random_forest.pkl')

tipos_cancer2 = {
    "Pulmón": 0,
    "Mama" : 1,
    "Próstata": 2,
    "Colón":3,
    "Páncreas" :4,
    "Hígado":5,
    "Estómago":6,
    "Leucemia":7
}

genero = {
    "M": 0,
    "F": 1,
    "Otro" :2
}

def on_predict():
    try:
        # Get inputs from entries
        edad = int(entry_edad.get())
        sexo = entry_sexo.get()
        sexo = genero[sexo]
        tipo = combo_tipo.get()
        tipo = tipos_cancer2.get(tipo)
        fumador = entry_fumador.get()
        aire = entry_aire.get()
        alcohol= entry_alcohol.get()
        genes = entry_genetico.get()
        obs = entry_obesidad.get()
        stage = entry_stage.get()

        lista = []
        #Age 	Gender 	Genetic_Risk 	Air_Pollution 	Alcohol_Use 	Smoking 	Obesity_Level 	Cancer_Type 	Cancer_Stage

        # Get inputs from entries
        lista.append(float(edad ))
        lista.append(float(sexo ))
        lista.append(float(genes ))
        lista.append(float(aire ))
        lista.append(float(alcohol ))
        lista.append(float(fumador ))
        lista.append(float(obs ))
        lista.append(tipo)
        lista.append(float(stage ))

        resultado = model.predict([lista])
        messagebox.showinfo("Predicción de Severidad", f"Severidad estimada: {resultado[0]:.2f}")
    except Exception as e:
        messagebox.showerror("Error", f"Error en la entrada: {e}")

# Crear ventana principal
root = tk.Tk()
root.title("Herramienta de Predicción de Severidad")

# Crear etiquetas y campos de entrada
tk.Label(root, text="Age").grid(row=0, column=0)
entry_edad = tk.Entry(root)
entry_edad.grid(row=0, column=1)

tk.Label(root, text="Genero, (M/F/Otro)").grid(row=1, column=0)
entry_sexo = tk.Entry(root)
entry_sexo.grid(row=1, column=1)

tipos_cancer = [
    "Pulmón",
    "Mama",
    "Próstata",
    "Colón",
    "Páncreas",
    "Hígado",
    "Estómago",
    "Leucemia"
]

tk.Label(root, text="Tipo de Cancer").grid(row=2, column=0)
combo_tipo = ttk.Combobox(root, values=tipos_cancer, state="readonly")
combo_tipo.grid(row=2, column=1)
combo_tipo.current(0)  # Selecciona la primera opción por defecto

tk.Label(root, text="Contaminacion del aire (0-10)").grid(row=3, column=0)
entry_aire = tk.Entry(root)
entry_aire.grid(row=3, column=1)

tk.Label(root, text="Consumo de Alcohol (0-10)").grid(row=4, column=0)
entry_alcohol = tk.Entry(root)
entry_alcohol.grid(row=4, column=1)
# Botón para predecir
tk.Label(root, text="Consumo de Tabaco (0-10) ").grid(row=5, column=0)
entry_fumador = tk.Entry(root)
entry_fumador.grid(row=5, column=1)

tk.Label(root, text="Obesidad (0-10)").grid(row=6, column=0)
entry_obesidad = tk.Entry(root)
entry_obesidad.grid(row=6, column=1)

tk.Label(root, text="Peligro genético (0-10)").grid(row=7, column=0)
entry_genetico = tk.Entry(root)
entry_genetico.grid(row=7, column=1)

tk.Label(root, text="Etapa de cancer").grid(row=8, column=0)
entry_stage = tk.Entry(root)
entry_stage.grid(row=8, column=1)

btn_predict = tk.Button(root, text="Predecir Severidad", command=on_predict)
btn_predict.grid(row=9, column=0, columnspan=2, pady=10)

root.mainloop()

model = joblib.load('modelo_random_forest.pkl')
