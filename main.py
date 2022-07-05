from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import datetime as dt

root = Tk()
root.geometry("1200x900")
root.title("Myta´s Salon")

#lista del personal

personal = ttk.Combobox(state="readonly", values=["Eliezer", "Mariangel", "Mariana", "Peluqueria"], font=40)
personal.place(x=200, y=100)

#lista de servicios
servicios = ttk.Combobox(state="readonly", values=["Barberia", "Barberia (Barba)", "Bucles Cabello Largo", "Bucles Cabello Mediano",
"Cejas",
"Cintillos Tornados",
"Cirugia Capilar Aplicacion",
"Cirugia Capilar Completa",
"Corte de Cabello Corto",
"Corte de Cabello Largo",
"Corte de Cabello Mediano",
"Hidratacion",
"Hidratacion Completa",
"Lavado de Cabeza",
"Manicure",
"Manicure y Peducure",
"Mantenimiento de extenciones",
"Mechas",
"Montura de Extenciones",
"Pedicure",
"Peinado Corto",
"Peinado Largo",
"Peinado Medio",
"Pestanas",
"Planchado/Secado",
"Producto",
"Retiro de Acrilico",
"Retiro de esm semi perm",
"Retiro de Extenciones",
"Retiro de Pestanas",
"Tinte Aplicacion",
"Tinte Aplicacion Completa", "Trenzas"],
font=40)
servicios.config(width=20)
servicios.place(x=200, y=150)

# mostrando la fecha
fecha = dt.datetime.now()
fecha = Label(root, text=f"{fecha:%A, %B, %d, %Y}", font=40)
fecha.place(x=100, y=500)

# Calculo total Bolivares
def totalbolivares():
    bolivaresefectivo = float(pago_efect_bolivares.get())
    bolivarespagomovil = float(pago_pgmovil_bolivares.get())
    bolivaresptoventa = float(pago_ptventas_bolivares.get())
    valordolar = float(valor_dolar.get())
    dolaresefect = float(pago_efect_dolares.get())
    bolivares = float(bolivaresefectivo + bolivarespagomovil + bolivaresptoventa)
    dolares = float(bolivares/valordolar + dolaresefect)
    bolivaresr = round(bolivares, 2)
    dolaresr = round(dolares, 2)
    monto_total_dolares.config(text=dolaresr)
    monto_total_bolivares.config(text=bolivaresr)

#imagen

imagen = Image.open("C:/Users/dpuli/Documents/Peluqueria/Programs/logo.png")
imagen = imagen.resize((100,50))

#mostrando el logo

log = ImageTk.PhotoImage(imagen)
lbl_img = Label(root, image = log)
lbl_img.place(x=5, y=5)


# entry points
# personal_entry = Entry()
# personal_entry.place(x=700, y=100)
# servicio_entry = Entry()
# servicio_entry.place(x=700, y=150)
pago_efect_bolivares = StringVar()
pago_efect_bolivares_entry = Entry(textvariable=pago_efect_bolivares, font=40)
pago_efect_bolivares_entry.place(x=825, y=100)
pago_pgmovil_bolivares = StringVar()
pago_pgmovil_bolivares_entry = Entry(textvariable=pago_pgmovil_bolivares, font=40)
pago_pgmovil_bolivares_entry.place(x=825, y=150)
pago_ptventas_bolivares = StringVar()
pago_ptventas_bolivares_entry = Entry(textvariable=pago_ptventas_bolivares, font=40)
pago_ptventas_bolivares_entry.place(x=825, y=200)
pago_efect_dolares = StringVar()
pago_efect_dolares_entry = Entry(textvariable=pago_efect_dolares, font=40)
pago_efect_dolares_entry.place(x=825, y=250)
valor_dolar = StringVar()
valor_dolar_entry = Entry(textvariable=valor_dolar, font=40)
valor_dolar_entry.place(x=700, y=600)

# labels
personal_label = Label(text="Personal", font=40)
personal_label.place(x=100, y=100)
servicio_label = Label(text="Servicio", font=40)
servicio_label.place(x=100, y=150)
pago_efect_bolivares_label = Label(text="Pago en efectivo Bolivares", font=40)
pago_efect_bolivares_label.place(x=500, y=100)
pago_pgmovil_bolivares_label = Label(text="Pago Movil en Bolivares", font=40)
pago_pgmovil_bolivares_label.place(x=500, y=150)
pago_ptventas_bolivares_label = Label(text="Pago Punto de ventas en Bolivares", font=40)
pago_ptventas_bolivares_label.place(x=500, y=200)
pago_efect_dolares_label = Label(text="Pago Efectivo Dolares", font=40)
pago_efect_dolares_label.place(x=500, y=250)
monto_total_bolivares_label = Label(text="Monto Total Bolivares", font=40)
monto_total_bolivares_label.place(x=500, y=300)
monto_total_bolivares = Label(font=40)
monto_total_bolivares.place(x=825, y=300)
monto_total_dolares_label = Label(text="Monto Total Dolares", font=40)
monto_total_dolares_label.place(x=500, y=350)
monto_total_dolares = Label(font=40)
monto_total_dolares.place(x=825, y=350)
vuelto_bolivares_label = Label(text="Vuelto Bolivares", font=40)
vuelto_bolivares_label.place(x=500, y=400)
vuelto_dolares_label = Label(text="Vuelto Dolares", font=40)
vuelto_dolares_label.place(x=500, y=450)
valor_dolar_label = Label(text="Cotizacion del Dolar")
valor_dolar_label.place(x=500, y=600)

# buttons
process_button = Button(root, text="Procesar", font="40", bg="green", command=totalbolivares)
process_button.place(x=500, y=700)
delete_button = Button(root, text="Borrar Todo", font="30", bg="red")
delete_button.place(x=700, y=700)

root.mainloop()