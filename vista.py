from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
from tkinter.ttk import *
from modelo import SpotMusicModel


# ##############################################
# VISTA
# ##############################################

class SpotMusicApp:

    def __init__(self, root):
        self.root = root
        self.modelo = SpotMusicModel () ## to use modelo in vista
        self.root.title("SPOTMUSIC")
            
        self.titulo = Label(self.root, text="Almacená tus canciones favoritas", anchor=CENTER, background="chocolate1", foreground="black", font=("Almacena tus canciones favoritas", 10, 'roman'))
        self.titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky=W+E)
        
        self.playlist_label = Label(self.root, text="Playlist")
        self.playlist_label.grid(row=1, column=0, sticky=W)
        self.artista_label = Label(self.root, text="Artista")
        self.artista_label.grid(row=2, column=0, sticky=W)
        self.cancion_label = Label(self.root, text="Canción")
        self.cancion_label.grid(row=3, column=0, sticky=W)
        
        self.a_val, self.b_val, self.c_val = StringVar(), StringVar(), StringVar()
        self.w_ancho = 20
        
        self.entrada1 = Entry(self.root, textvariable=self.a_val, width=self.w_ancho)
        self.entrada1.grid(row=1, column=1)
        self.entrada2 = Entry(self.root, textvariable=self.b_val, width=self.w_ancho)
        self.entrada2.grid(row=2, column=1)
        self.entrada3 = Entry(self.root, textvariable=self.c_val, width=self.w_ancho)
        self.entrada3.grid(row=3, column=1)
        
        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = ("col1", "col2", "col3")
        self.tree.column("#0", width=90, minwidth=50, anchor=W)
        self.tree.column("col1", width=200, minwidth=80)
        self.tree.column("col2", width=200, minwidth=80)
        self.tree.column("col3", width=200, minwidth=80)
        
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Playlist")
        self.tree.heading("col2", text="Artista")
        self.tree.heading("col3", text="Canción")
        self.tree.grid(row=100, column=0, columnspan=4)
        
        style = Style()
        style.configure('TButton', font=('calibri', 12, 'bold'), borderwidth='4')
        style.map('TButton', foreground=[('active', '!disabled', 'orange')], background=[('active', 'black')])
        

        self.boton_alta=Button(root, text="Alta", command=lambda:self.modelo.alta(self.a_val.get(), self.b_val.get(), self.c_val.get(), self.tree))
        self.boton_alta.grid(row=7, column=0)

        self.boton_consulta=Button(root, text="Consultar", command=lambda:self.modelo.consultar(self.a_val.get(), self.b_val.get(), self.c_val.get(), self.tree))
        self.boton_consulta.grid(row=7, column=1)

        self.boton_modificar=Button(root, text="Modificar", command=lambda:self.modelo.modificar(self.a_val.get(), self.b_val.get(), self.c_val.get(), self.tree))
        self.boton_modificar.grid(row=7, column=2)

        self.boton_borrar=Button(root, text="Borrar", command=lambda:self.modelo.borrar(self.a_val.get(),self.tree))
        self.boton_borrar.grid(row=7, column=3)

        self.boton_consultar_lista_playlist=Button(root, text="Consultar mis playlist",command=lambda:self.modelo.consultar_lista_playlist(self.tree))
        self.boton_consultar_lista_playlist.grid(row=1, column=3)

        self.boton_borrar_playlist=Button(root, text="Borrar playlist",command=lambda:self.modelo.borrar_playlist(self.a_val.get(),self.tree))
        self.boton_borrar_playlist.grid(row=2, column=3)
        
        self.tree.bind("<<TreeviewSelect>>", self.actualizar)

    def actualizar(self, evento):
        selection = self.tree.selection()
        if selection:
            playlist_seleccionada = self.tree.item(selection[0], "values")[0]
            artista_seleccionada = self.tree.item(selection[0], "values")[1]
            cancion_seleccionada = self.tree.item(selection[0], "values")[2]
            self.a_val.set(playlist_seleccionada)
            #self.b_val.set(artista_seleccionada)
            #self.c_val.set(cancion_seleccionada)

        




