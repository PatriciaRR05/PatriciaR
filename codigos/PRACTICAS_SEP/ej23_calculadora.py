import tkinter as tk

# Función que se llama cuando el usuario presiona un botón
def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)  # Borra el contenido de la caja de entrada
    entry.insert(tk.END, current + value)

# Función para borrar el contenido de la caja de entrada
def clear():
    entry.delete(0, tk.END)

# Función para calcular el resultado de la operación
def calculate():
    try:
        result = eval(entry.get())  # eval evalúa la expresión matemática
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora")

# Crear una caja de entrada (Entry) para mostrar los números y resultados
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Botones de la calculadora
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Crear los botones y asignarles las funciones correspondientes
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=calculate)
    elif text == "C":
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=clear)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=lambda value=text: click_button(value))
    
    button.grid(row=row, column=col)