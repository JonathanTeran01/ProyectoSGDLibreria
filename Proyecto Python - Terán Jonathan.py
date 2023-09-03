import tkinter as tk
from tkinter import simpledialog

# Definir una clase Libro para representar libros en la biblioteca
class Libro:
    def __init__(self, titulo, autor, ano_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacion = ano_publicacion
        self.disponible = True  # Inicialmente, el libro está disponible

# Definir una clase Usuario para representar a los usuarios de la biblioteca
class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

# Definir la clase Biblioteca para gestionar libros y usuarios
class Biblioteca:
    def __init__(self):
        self.libros = []   # Lista para almacenar libros
        self.usuarios = []   # Lista para almacenar usuarios

    def agregar_libro(self, libro):
        #Agregar un libro a la biblioteca.
        self.libros.append(libro)

    def agregar_usuario(self, usuario):
        #Agregar un usuario a la biblioteca.
        self.usuarios.append(usuario)

    def buscar_libro_por_titulo(self, titulo):
        #Buscar libros por título y devolver una lista de libros encontrados.
        libros_encontrados = []
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                libros_encontrados.append(libro)
        return libros_encontrados

    def buscar_libro_por_autor(self, autor):
        #Buscar libros por autor y devolver una lista de libros encontrados.
        libros_encontrados = []
        for libro in self.libros:
            if libro.autor.lower() == autor.lower():
                libros_encontrados.append(libro)
        return libros_encontrados

    def prestar_libro(self, libro, usuario):
        #Prestar un libro a un usuario.
        if libro.disponible:
            libro.disponible = False
            return f"{usuario.nombre} ha tomado prestado '{libro.titulo}'"
        else:
            return "Lo siento, el libro no está disponible"

    def devolver_libro(self, libro, usuario):
        #Devolver un libro a la biblioteca.
        if not libro.disponible:
            libro.disponible = True
            return f"{usuario.nombre} ha devuelto '{libro.titulo}'"
        else:
            return "El libro ya está disponible"

# Crear una instancia de la biblioteca
biblioteca = Biblioteca()

# Agregar libros manualmente
libro1 = Libro("El Código Da Vinci", "Dan Brown", 2003)
libro2 = Libro("Harry Potter y la piedra filosofal", "J.K. Rowling", 1997)
libro3 = Libro("1984", "George Orwell", 1949)
libro4 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
libro5 = Libro("El Hobbit", "J.R.R. Tolkien", 1937)



biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Definir la clase InterfazBiblioteca (Interfaz de usuario) usando tkinter
class InterfazBiblioteca:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Bibliotecas")

        self.crear_widgets()

    def crear_widgets(self):
        # Etiqueta de título
        etiqueta_titulo = tk.Label(self.root, text="Sistema de Gestión de Bibliotecas")
        etiqueta_titulo.pack(pady=10)

        # Botón para buscar libros por título
        boton_buscar_titulo = tk.Button(self.root, text="Buscar libro por título", command=self.buscar_por_titulo)
        boton_buscar_titulo.pack()

        # Botón para buscar libros por autor
        boton_buscar_autor = tk.Button(self.root, text="Buscar libro por autor", command=self.buscar_por_autor)
        boton_buscar_autor.pack()

        # Botón para prestar un libro
        boton_prestar_libro = tk.Button(self.root, text="Prestar un libro", command=self.prestar_libro)
        boton_prestar_libro.pack()

        # Botón para devolver un libro
        boton_devolver_libro = tk.Button(self.root, text="Devolver un libro", command=self.devolver_libro)
        boton_devolver_libro.pack()

        # Resultado de la acción
        self.resultado_etiqueta = tk.Label(self.root, text="")
        self.resultado_etiqueta.pack(pady=10)

    def buscar_por_titulo(self):
        # Pedir al usuario que ingrese el título del libro
        titulo = simpledialog.askstring("Buscar libro por título", "Ingrese el título del libro:")
        if titulo:
            libros_encontrados = biblioteca.buscar_libro_por_titulo(titulo)
            if libros_encontrados:
                # Mostrar los libros encontrados
                resultado = "Libros encontrados:\n"
                for libro in libros_encontrados:
                    resultado += f"{libro.titulo} por {libro.autor}\n"
                self.resultado_etiqueta.config(text=resultado)
            else:
                self.resultado_etiqueta.config(text="No se encontraron libros con ese título.")

    def buscar_por_autor(self):
        # Pedir al usuario que ingrese el nombre del autor
        autor = simpledialog.askstring("Buscar libro por autor", "Ingrese el nombre del autor:")
        if autor:
            libros_encontrados = biblioteca.buscar_libro_por_autor(autor)
            if libros_encontrados:
                # Mostrar los libros encontrados
                resultado = "Libros encontrados:\n"
                for libro in libros_encontrados:
                    resultado += f"{libro.titulo} por {libro.autor}\n"
                self.resultado_etiqueta.config(text=resultado)
            else:
                self.resultado_etiqueta.config(text="No se encontraron libros de ese autor.")

    def prestar_libro(self):
        # Pedir al usuario que ingrese su nombre y el título del libro que desea tomar prestado
        nombre_usuario = simpledialog.askstring("Prestar un libro", "Ingrese su nombre:")
        if nombre_usuario:
            titulo_libro = simpledialog.askstring("Prestar un libro", "Ingrese el título del libro:")
            if titulo_libro:
                usuario = Usuario(nombre_usuario, "")
                libros_encontrados = biblioteca.buscar_libro_por_titulo(titulo_libro)

                if libros_encontrados:
                    libro = libros_encontrados[0]  # Tomar el primer libro encontrado
                    resultado = biblioteca.prestar_libro(libro, usuario)
                    self.resultado_etiqueta.config(text=resultado)
                else:
                    self.resultado_etiqueta.config(text="No se encontró el libro que está buscando.")

    def devolver_libro(self):
        # Pedir al usuario que ingrese su nombre y el título del libro que desea devolver
        nombre_usuario = simpledialog.askstring("Devolver un libro", "Ingrese su nombre:")
        if nombre_usuario:
            titulo_libro = simpledialog.askstring("Devolver un libro", "Ingrese el título del libro:")
            if titulo_libro:
                usuario = Usuario(nombre_usuario, "")
                libros_encontrados = biblioteca.buscar_libro_por_titulo(titulo_libro)

                if libros_encontrados:
                    libro = libros_encontrados[0]  # Tomar el primer libro encontrado
                    resultado = biblioteca.devolver_libro(libro, usuario)
                    self.resultado_etiqueta.config(text=resultado)
                else:
                    self.resultado_etiqueta.config(text="No se encontró el libro que está buscando.")

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazBiblioteca(root)
    root.mainloop()
