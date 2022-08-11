import sqlite3

# data base

def database():
    con = sqlite3.connect("peluqueria.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS finanzas (id INTEGER PRIMARY KEY, Personal text, TBolivares TEXT, TDolares TEXT, Ppeluqueria TEXT, Ppersonal TEXT)")
    con.commit()
    con.close()

def addTrans(Personal, TBolivares, TDolares, Ppeluqueria, Ppersonal):
    con = sqlite3.connect("peluqueria.db")
    cur = con.cursor()
    cur.execute("INSERT INTO finanzas VALUES (NULL, ?, ?, ?, ?, ?, ?)", Personal, TBolivares, TDolares, Ppeluqueria, Ppersonal)
    con.commit()
    con.close()

def viewData():
    con = sqlite3.connect("peluqueria.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM finanzas")
    rows = cur.fetchall()
    con.close()
    return rows

def deleteTrans():
     con = sqlite3.connect("peluqueria.db")
    cur = con.cursor()
    cur.execute("DELETE FROM finanzas WHERE id=?", (id,))
    con.commit()
    con.close()

