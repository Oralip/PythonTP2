
Documentación de SpotMusic
==========================


**SPOTMUSIC** es una interfaz que permite la creacion de PLAYLIST.

En las PLAYLIST se pueden agregar/modificar/eliminar canciones y sus respectivos artistas

.. note::

   Proyecto aun en construcción, correspodiente a la diplomatura de python en la UTN 2024.


**SPOTMUSIC** posee una estructura MVC, por lo que contiene 3 modulos.


Modelo.py
==========================

El módulo `Modelo` proporciona la clase `SpotMusicModel` para gestionar las listas de reproducción, artistas y canciones en una base de datos SQLite.



Métodos
--------------------------

- ``__init__``: Inicializa el objeto `SpotMusicModel`.
- ``conexion``: Establece una conexión con la base de datos SQLite.
- ``crear_tabla``: Crea una tabla en la base de datos si no existe.
- ``consultar_tabla``: Verifica si una tabla existe en la base de datos.
- ``consultar_cancion``: Consulta la existencia de una canción en una lista de reproducción por nombre de artista y canción en la base de datos.
- ``alta``: Añade una canción a una lista de reproducción en la base de datos.
- ``actualizar_treeview``: Actualiza el widget TreeView con datos de la base de datos.
- ``execute_query``: Ejecuta una consulta en la base de datos y actualiza el widget TreeView.
- ``consultar``: Recupera datos de la base de datos basados en la lista de reproducción, artista o nombre de la canción.
- ``consultar_lista_playlist``: Recupera una lista de listas de reproducción de la base de datos.
- ``actualizar_playlist``: Añade una canción a una lista de reproducción en la base de datos.
- ``modificar``: Modifica una canción en una lista de reproducción en la base de datos.
- ``borrar``: Elimina una canción de una lista de reproducción en la base de datos.
- ``borrar_playlist``: Elimina una lista de reproducción de la base de datos.


Vista.py
==========================

El módulo `Vista` define la interfaz gráfica de usuario de SpotMusic usando `tkinter`




Métodos
--------------------------

- ``__init__``: Inicializa la interfaz gráfica de la aplicación.
- ``actualizar``: Actualiza los campos de entrada con la selección actual del TreeView.


Controler.py
==========================


El módulo `Controler` inicializa la aplicación de SpotMusic.


Interfaz gráfica
==========================

.. image:: interfazgraficaspotmusic.png
   :height: 300
   :width: 900





















