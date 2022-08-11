from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import datetime as dt

ficha = Tk()
ficha.geometry("1200x900")
ficha.title("Ficha del Cliente")

#titulo

titulo_label = Label(text="FICHA DE DIAGNOSTICO Y ASOSORAMIENTO CAPILAR", font=80)
titulo_label.place(x=350, y=50)

# Datos del cliente

cliente_label = Label(text="DATOS DEL CLIENTE", font=80)
cliente_label.place(x=500, y=100)

# Entrada de datos

nombre_label = Label(text="Nombre y Apellido:")
nombre_label.place(x=50, y=150)
nombre = StringVar()
nombre_entry = Entry(textvariable=nombre)
nombre_entry.place(x=205, y=150)
atendido_label = Label(text="Atendido por:")
atendido_label.place(x=50, y=175)
atendido = StringVar()
atendido_entry = Entry(textvariable=atendido)
atendido_entry.place(x=205, y=175)
tratamiento_label = Label(text="Fecha del ultimo tramiento:")
tratamiento_label.place(x=50, y=200)
tratamiento = StringVar()
tratamiento_entry = Entry(textvariable=tratamiento)
tratamiento_entry.place(x=205, y=200)
telefono_label = Label(text="Telefono:")
telefono_label.place(x=500, y=150)
telefono = StringVar()
telefono_entry = Entry(textvariable=telefono)
telefono_entry.place(x=590, y=150)
salon_label = Label(text="Salon:")
salon_label.place(x=500, y=175)
salon = StringVar()
salon_entry = Entry(textvariable=salon)
salon_entry.place(x=590, y=175)
productos_label = Label(text="Productos:")
productos_label.place(x=50, y=225)
productos = StringVar()
productos_entry = Entry(textvariable=productos, width=144)
productos_entry.place(x=205, y=225)
ciudad_label = Label(text="Ciudad:")
ciudad_label.place(x=875, y=150)
ciudad = StringVar()
ciudad_entry = Entry(textvariable=ciudad)
ciudad_entry.place(x=950, y=150)
fecha_label = Label(text="Fecha:")
fecha_label.place(x=875, y=175)
fecha = StringVar()
fecha_entry = Entry(textvariable=fecha)
fecha_entry.place(x=950, y=175)
marca_label = Label(text="Marca:")
marca_label.place(x=875, y=200)
marca = StringVar()
marca_entry = Entry(textvariable=marca)
marca_entry.place(x=950, y=200)

# Estructura del Cabello

cabello_label = Label(text="ESTRUCTURA DEL CABELLO", font=80)
cabello_label.place(x=500, y=250)

longitud_label = Label(text="Longitud", fg="#7A378B", font="12")
longitud_label.place(x=50, y=300)

estado_label = Label(text="Estado", fg="#7A378B", font="12")
estado_label.place(x=200, y=300)

estado1_label = Label(text="Estado", fg="#7A378B", font="12")
estado1_label.place(x=400, y=300)

grosor_label = Label(text="Grosor", fg="#7A378B", font="12")
grosor_label.place(x=600, y=300)

color_label = Label(text="Color Natural", fg="#7A378B", font="12")
color_label.place(x=800, y=300)

canas_label = Label(text="% Canas", fg="#7A378B", font="12")
canas_label.place(x=1000, y=300)

# Check buttons
corto = IntVar()
mediano = IntVar()
largo = IntVar()
natural = IntVar()
tonalizado = IntVar()
colorido = IntVar()
decolorado = IntVar()
mechas = IntVar()
ondulado = IntVar()
alisado = IntVar()
fino = IntVar()
normal = IntVar()
grueso = IntVar()
raices = IntVar()
largocolor = IntVar()
puntas = IntVar()
frontal = StringVar()
coronilla = IntVar()
nuca = IntVar()
laterales = IntVar()

corto_label = Label(text="CORTO")
corto_label.place(x=50, y=350)
corto_checkb = Checkbutton(variable=corto, onvalue = 1, offvalue = 0)
corto_checkb.place(x=125, y=350)

mediano_label = Label(text="MEDIANO")
mediano_label.place(x=50, y=375)
mediano_checkb = Checkbutton(variable=mediano, onvalue = 1, offvalue = 0)
mediano_checkb.place(x=125, y=375)

largo_label = Label(text="LARGO")
largo_label.place(x=50, y=400)
largo_checkb = Checkbutton(variable=largo, onvalue = 1, offvalue = 0)
largo_checkb.place(x=125, y=400)

natural_label = Label(text="NATURAL")
natural_label.place(x=200, y=350)
natural_checkb = Checkbutton(variable=natural, onvalue = 1, offvalue = 0)
natural_checkb.place(x=300, y=350)

tonalizado_label = Label(text="TONALIZADO")
tonalizado_label.place(x=200, y=375)
tonalizado_checkb = Checkbutton(variable=tonalizado, onvalue = 1, offvalue = 0)
tonalizado_checkb.place(x=300, y=375)

colorido_label = Label(text="COLORIDO")
colorido_label.place(x=200, y=400)
colorido_checkb = Checkbutton(variable=colorido, onvalue = 1, offvalue = 0)
colorido_checkb.place(x=300, y=400)

decolorado_label = Label(text="DECOLORADO")
decolorado_label.place(x=200, y=425)
decolorado_checkb = Checkbutton(variable=decolorado, onvalue = 1, offvalue = 0)
decolorado_checkb.place(x=300, y=425)

mechas_label = Label(text="CON MECHAS")
mechas_label.place(x=400, y=350)
mechas_checkb = Checkbutton(variable=mechas, onvalue = 1, offvalue = 0)
mechas_checkb.place(x=500, y=350)

ondulado_label = Label(text="ONDULADO")
ondulado_label.place(x=400, y=375)
ondulado_checkb = Checkbutton(variable=ondulado, onvalue = 1, offvalue = 0)
ondulado_checkb.place(x=500, y=375)

alisado_label = Label(text="ALISADO")
alisado_label.place(x=400, y=400)
alisado_checkb = Checkbutton(variable=alisado, onvalue = 1, offvalue = 0)
alisado_checkb.place(x=500, y=400)

fino_label = Label(text="FINO")
fino_label.place(x=600, y=350)
fino_checkb = Checkbutton(variable=fino, onvalue = 1, offvalue = 0)
fino_checkb.place(x=700, y=350)

normal_label = Label(text="NORMAL")
normal_label.place(x=600, y=375)
normal_checkb = Checkbutton(variable=normal, onvalue = 1, offvalue = 0)
normal_checkb.place(x=700, y=375)

grueso_label = Label(text="GRUESO")
grueso_label.place(x=600, y=400)
grueso_checkb = Checkbutton(variable=grueso, onvalue = 1, offvalue = 0)
grueso_checkb.place(x=700, y=400)

raices_label = Label(text="RAICES")
raices_label.place(x=800, y=350)
raices_checkb = Checkbutton(variable=raices, onvalue = 1, offvalue = 0)
raices_checkb.place(x=900, y=350)

largocolor_label = Label(text="LARGO")
largocolor_label.place(x=800, y=375)
largocolor_checkb = Checkbutton(variable=largocolor, onvalue = 1, offvalue = 0)
largocolor_checkb.place(x=900, y=375)

puntas_label = Label(text="PUNTAS")
puntas_label.place(x=800, y=400)
puntas_checkb = Checkbutton(variable=puntas, onvalue = 1, offvalue = 0)
puntas_checkb.place(x=900, y=400)

frontal_label = Label(text="FRONTAL")
frontal_label.place(x=1000, y=350)
frontal_entry = Entry(textvariable=frontal, width=4)
frontal_entry.place(x=1100, y=350)
porcentaje1_label = Label(text="%")
porcentaje1_label.place(x=1125, y=350)

coronilla_label = Label(text="CORONILLA")
coronilla_label.place(x=1000, y=375)
coronilla_entry = Entry(textvariable=coronilla, width=4)
coronilla_entry.place(x=1100, y=375)
porcentaje2_label = Label(text="%")
porcentaje2_label.place(x=1125, y=375)

nuca_label = Label(text="NUCA")
nuca_label.place(x=1000, y=400)
nuca_entry = Entry(textvariable=nuca, width=4)
nuca_entry.place(x=1100, y=400)
porcentaje3_label = Label(text="%")
porcentaje3_label.place(x=1125, y=400)

laterales_label = Label(text="LATERALES")
laterales_label.place(x=1000, y=425)
laterales_entry = Entry(textvariable=laterales, width=4)
laterales_entry.place(x=1100, y=425)
porcentaje4_label = Label(text="%")
porcentaje4_label.place(x=1125, y=425)

# trabajo a realizar

trabajo_label = Label(text="TRABAJO A REALIZAR", font=80)
trabajo_label.place(x=500, y=475)

trabajorealizado_text = Text(ficha, width=140, height=2)
trabajorealizado_text.place(x=50, y=500)

#imagen

imagen = Image.open("C:/Users/dpuli/Documents/Peluqueria/Programs/logo.png")
imagen = imagen.resize((150,75))

#mostrando el logo

log = ImageTk.PhotoImage(imagen)
lbl_img = Label(ficha, image = log)
lbl_img.place(x=20, y=15)

# botones

nuevoCliente = Button(ficha, text="Anadir Nuevo Cliente", bg="grey")
nuevoCliente.place(x=50, y=600)

consultarCliente = Button(ficha, text="Consultar", bg="grey")
consultarCliente.place(x=200, y=600)

borrar = Button(ficha, text="Borrar", bg="grey")
borrar.place(x=300, y=600)

borrarCliente = Button(ficha, text="Borrar Cliente", bg="red")
borrarCliente.place(x=800, y=600)

ficha.mainloop()