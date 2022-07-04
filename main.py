from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.geometry("1200x900")
root.title("Myta´s Salon")

#lista del personal

personal = ttk.Combobox(state="readonly", values=["Eliezer", "Mariangel", "Mariana", "Peluqueria"])
personal.place(x=700, y=100)

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
"Tinte Aplicacion Completa", "Trenzas"])
servicios.config(width=28)
servicios.place(x=700, y=150)


# Calculo total Bolivares
def totalbolivares():
    bolivaresefectivo = float(pago_efect_bolivares.get())
    bolivarespagomovil = float(pago_pgmovil_bolivares.get())
    bolivaresptoventa = float(pago_ptventas_bolivares.get())
    valordolar = float(valor_dolar.get())
    dolaresefect = float(pago_efect_dolares.get())
    bolivares = float(bolivaresefectivo + bolivarespagomovil + bolivaresptoventa)
    dolares = float(bolivares/valordolar + dolaresefect)
    monto_total_dolares.config(text=dolares)
    monto_total_bolivares.config(text=bolivares)

#imagen

imagen = Image.open("C:/Users/dpuli/Documents/Peluqueria/Programs/logo.png")
imagen = imagen.resize((400,300))

#mostrando el logo

log = ImageTk.PhotoImage(imagen)
lbl_img = Label(root, image = log)
lbl_img.place(x=50, y=50)


# entry points
# personal_entry = Entry()
# personal_entry.place(x=700, y=100)
# servicio_entry = Entry()
# servicio_entry.place(x=700, y=150)
pago_efect_bolivares = StringVar()
pago_efect_bolivares_entry = Entry(textvariable=pago_efect_bolivares)
pago_efect_bolivares_entry.place(x=700, y=200)
pago_pgmovil_bolivares = StringVar()
pago_pgmovil_bolivares_entry = Entry(textvariable=pago_pgmovil_bolivares)
pago_pgmovil_bolivares_entry.place(x=700, y=250)
pago_ptventas_bolivares = StringVar()
pago_ptventas_bolivares_entry = Entry(textvariable=pago_ptventas_bolivares)
pago_ptventas_bolivares_entry.place(x=700, y=300)
pago_efect_dolares = StringVar()
pago_efect_dolares_entry = Entry(textvariable=pago_efect_dolares)
pago_efect_dolares_entry.place(x=700, y=350)
valor_dolar = StringVar()
valor_dolar_entry = Entry(textvariable=valor_dolar)
valor_dolar_entry.place(x=700, y=600)

# labels
personal_label = Label(text="Personal")
personal_label.place(x=500, y=100)
servicio_label = Label(text="Servicio")
servicio_label.place(x=500, y=150)
pago_efect_bolivares_label = Label(text="Pago en efectivo Bolivares")
pago_efect_bolivares_label.place(x=500, y=200)
pago_pgmovil_bolivares_label = Label(text="Pago Movil en Bolivares")
pago_pgmovil_bolivares_label.place(x=500, y=250)
pago_ptventas_bolivares_label = Label(text="Pago Punto de ventas en Bolivares")
pago_ptventas_bolivares_label.place(x=500, y=300)
pago_efect_dolares_label = Label(text="Pago Efectivo Dolares")
pago_efect_dolares_label.place(x=500, y=350)
monto_total_bolivares_label = Label(text="Monto Total Bolivares")
monto_total_bolivares_label.place(x=500, y=400)
monto_total_bolivares = Label()
monto_total_bolivares.place(x=700, y=400)
monto_total_dolares_label = Label(text="Monto Total Dolares")
monto_total_dolares_label.place(x=500, y=450)
monto_total_dolares = Label()
monto_total_dolares.place(x=700, y=450)
vuelto_bolivares_label = Label(text="Vuelto Bolivares")
vuelto_bolivares_label.place(x=500, y=500)
vuelto_dolares_label = Label(text="Vuelto Dolares")
vuelto_dolares_label.place(x=500, y=550)
valor_dolar_label = Label(text="Cotizacion del Dolar")
valor_dolar_label.place(x=500, y=600)

# buttons
process_button = Button(root, text="Procesar", font="40", bg="green", command=totalbolivares)
process_button.place(x=500, y=700)
delete_button = Button(root, text="Borrar Todo", font="30", bg="red")
delete_button.place(x=700, y=700)

root.mainloop()