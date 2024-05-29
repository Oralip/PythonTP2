from tkinter import *
from tkinter.messagebox import *
import sqlite3
from tkinter import ttk
from tkinter.ttk import *
import re


class SpotMusicModel:
    def __init__(self):
        self.con = self.conexion()

    def conexion(self):
        return sqlite3.connect("mibase.db")

    def crear_tabla(self, tablename):
        con = self.conexion()
        cursor = con.cursor()
        sql = """CREATE TABLE IF NOT EXISTS {}
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 playlist varchar(20) NOT NULL,
                 artista varchar(20),
                 cancion varchar(20))
        """
        sql = sql.format(tablename)
        cursor.execute(sql)
        con.commit()

    def consultar_tabla(self, tablename):
        con = self.conexion()
        cursor = con.cursor()
        sql = """SELECT * from {}"""
        sql = sql.format(tablename)
        try:
            cursor.execute(sql)
        except:
            print('playlist no esta')
            return False

    def consultar_cancion(self, playlist, artista, cancion):
        con = self.conexion()
        cursor = con.cursor()
        data = (artista, cancion)
        sql = "SELECT playlist from {} WHERE artista= ? AND cancion= ?"
        sql = sql.format(playlist)
        try:
            result = cursor.execute(sql, data)
            result = result.fetchall()
            return len(result)
        except:
            print('except consultar_cancion - cancion no esta')
            return False

    def alta(self, playlist, artista, cancion, tree):
        playlist, artista, cancion = playlist.upper(), artista.upper(), cancion.upper()
        if playlist:
            if re.match('^[a-zA-Z0-9_]*$', playlist):  # Regex to match just alphanumeric and whitespace characters
                if artista:
                    if cancion:
                        if self.consultar_tabla(playlist) == False:
                            self.crear_tabla(playlist)
                            self.actualizar_playlist(playlist, artista, cancion, tree)
                        else:
                            self.actualizar_playlist(playlist, artista, cancion, tree)
                    else:
                        showerror('WARNING', 'Campo CANCION no puede estar vacio')
                else:
                    showerror('WARNING', 'Campo ARTISTA no puede estar vacio')
            else:
                showerror('WARNING', 'Usar solo caracteres ALPHANUMERICOS para campo PLAYLIST')
        else:
            showerror('WARNING', 'Campo PLAYLIST no puede estar vacio')

    def actualizar_treeview(self, playlist, tree):
        for row in tree.get_children():
            tree.delete(row)

        sql = "SELECT * FROM {} ORDER BY id ASC"
        sql = sql.format(playlist)
        con = self.conexion()
        cursor = con.cursor()
        datos = cursor.execute(sql)
        self.execute_query(datos, tree)

    def execute_query(self, datos, tree):
        resultado = datos.fetchall()
        for fila in resultado:
            tree.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3]))
            

    def consultar(self, playlist, artista, cancion, tree):
        playlist, artista, cancion = playlist.upper(), artista.upper(), cancion.upper()
        
        for row in tree.get_children():
            tree.delete(row)
        
        if not (playlist or artista or cancion):
            showerror('WARNING', 'Debe indicar el nombre de la PLAYLIST, ARTISTA o CANCION a consultar')
            return

        con = self.conexion()
        cursor = con.cursor()

        if playlist:
            sql = "SELECT * FROM {}"
            sql = sql.format(playlist)
            datos = cursor.execute(sql)
            self.execute_query(datos, tree)         

        if artista:
            sql = "SELECT * FROM SQLITE_SEQUENCE"
            datos = cursor.execute(sql)
            resultado = datos.fetchall()
            
            for i in range (0,(len(resultado))):
                data=(artista,)
                artista1=resultado [i]
                artista1=artista1[0]
                sql = "SELECT * FROM {} WHERE artista= ?"
                sql = sql.format(artista1)
                datos = cursor.execute(sql,data)
                self.execute_query(datos, tree)
        if cancion:
            sql = "SELECT * FROM SQLITE_SEQUENCE"
            datos = cursor.execute(sql)
            resultado = datos.fetchall()
            
            for i in range (0,(len(resultado))):
                data=(cancion,)
                cancion1=resultado [i]
                cancion1=cancion1[0]
                sql = "SELECT * FROM {} WHERE cancion= ?"
                sql = sql.format(cancion1)
                datos = cursor.execute(sql,data)
                self.execute_query(datos, tree)

        con.close()

    def consultar_lista_playlist(self, tree):
        for row in tree.get_children():
            tree.delete(row)
        sql = "SELECT * FROM SQLITE_SEQUENCE"
        con = self.conexion()
        cursor = con.cursor()
        try:
            datos = cursor.execute(sql)
            resultado = datos.fetchall()
            for fila in resultado:
                tree.insert("", 0, values=(fila[0], "- - -", "- - -"))
        except:
            showerror('WARNING', 'No tienes playlists creadas. Creá tu primera playlist usando el botón de ALTA')

    def actualizar_playlist(self, playlist, artista, cancion, tree):
        con = self.conexion()
        cursor = con.cursor()
        if self.consultar_cancion(playlist, artista, cancion) == 0:
            data = (playlist, artista, cancion)
            sql = "INSERT INTO {} (playlist, artista, cancion) VALUES(?, ?, ?)"
            sql = sql.format(playlist)
            cursor.execute(sql, data)
            con.commit()
            showinfo('Agregar', 'Cancion ' + cancion + ' agregada')
            self.actualizar_treeview(playlist, tree)
        else:
            showerror('WARNING', 'Esta canción ya existe en esta PLAYLIST, podes agregarla en otra')

    def modificar(self, playlist, artista, cancion, tree):
        playlist, artista, cancion = playlist.upper(), artista.upper(), cancion.upper()
        valor = tree.selection()
        item = tree.item(valor)

        if not valor:
            showerror("Error", "Seleccione el registro a Modificar")
            return

        if playlist == "" or artista == "" or cancion == "":
            showerror("Error", "Por favor, complete todos los campos.")
            return

        con = self.conexion()
        cursor = con.cursor()
        mi_id = item['text']
        data = (artista, cancion, mi_id)
        sql = '''UPDATE {} SET artista = ?, cancion = ? WHERE id = ?'''
        sql = sql.format(playlist)
        cursor.execute(sql, data)
        con.commit()
        con.close()
        self.actualizar_treeview(playlist, tree)

    def borrar(self, playlist, tree):
        valor = tree.selection()
        item = tree.item(valor)

        if not valor:
            showerror("Error", "Seleccione el registro a borrar")
            return

        con = self.conexion()
        cursor = con.cursor()
        mi_id = item['text']
        data = (mi_id,)
        sql = "DELETE FROM {} WHERE id = ?;"
        sql = sql.format(playlist)
        cursor.execute(sql, data)
        con.commit()
        showinfo('Eliminar', 'Cancion eliminada')
        tree.delete(valor)

    def borrar_playlist(self, playlist, tree):
        valor = tree.selection()
        item = tree.item(valor)

        if not valor:
            showerror("Error", "Seleccione el playlist a borrar")
            return
        question=askyesno(title='Eliminar', message= 'Seguro que quiere eliminar '+ playlist + '?')
        if question == True :
            con = self.conexion()
            cursor = con.cursor()
            sql = "DROP table {};"
            sql = sql.format(playlist)
            cursor.execute(sql)
            con.commit()
            showinfo('Eliminar', 'Playlist ' + playlist + ' eliminada')
            tree.delete(valor)
