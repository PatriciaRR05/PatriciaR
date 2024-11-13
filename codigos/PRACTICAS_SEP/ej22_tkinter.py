import tkinter as tk
import csv

ventana = tk.Tk()
ventana.title("MiPrimerVentana")
ventana.geometry("500x500")

#para crear la etiqueta
nombreContacto=tk.Entry(ventana,text="Nombre")
nombreContacto.pack()

#para crear la etiqueta
telefonoContacto=tk.Entry(ventana,text="Telefono")
telefonoContacto.pack()

#para crear la etiqueta
direccionContacto=tk.Entry(ventana,text="Direccion")
direccionContacto.pack()

#para crear la etiqueta
edadContacto=tk.Entry(ventana,text="Edad")
edadContacto.pack()

#sirve para rellenar la entrada
entradaNombre=tk.Entry(ventana)
entradaNombre.pack()

entradaTelefono=tk.Entry(ventana)
entradaTelefono.pack()

entradaDireccion=tk.Entry(ventana)
entradaDireccion.pack()

entradaEdad=tk.Entry(ventana)
entradaEdad.pack()


def guardar():
    nombre = entradaNombre.get()
    telefono= entradaTelefono.get()
    direccion= entradaDireccion.get()
    edad = entradaEdad.get()
    with open("agenta.csv", "a", nweline="")as archivo:
        contacto=csv.writer(archivo)
        contacto.writerow([nombre, telefono, edad, direccion])





botonGuardar=tk.Button(ventana, text="Guardar contactos", command=guardar)
botonGuardar.pack()



ventana.mainloop()