from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch, cm
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import random
from datetime import datetime
import os

# Palabras aleatorias comunes y fáciles
easy_words = [
    "Gato", "Perro", "Casa", "Jardín", "Escuela", "Maestro", "Libro", "Lápiz", "Mesa", "Silla",
    "Ventana", "Puerta", "Coche", "Bicicleta", "Avión", "Tren", "Amigo", "Familia", "Comida", "Agua",
    "Leche", "Juguete", "Pelota", "Música", "Canción", "Baile", "Pintura", "Dibujo", "Televisión", "Computadora",
    "Teléfono", "Árbol", "Planta", "Flor", "Fruta", "Verdura", "Pan", "Queso", "Helado", "Chocolate",
    "Zapato", "Calcetín", "Sombrero", "Camisa", "Pantalón", "Abrigo", "Bufanda", "Guante", "Sombrilla", "Lluvia",
    "Sol", "Nube", "Viento", "Nieve", "Montaña", "Río", "Lago", "Mar", "Playa", "Barco",
    "Tractor", "Granja", "Gallina", "Vaca", "Cerdo", "Caballo", "Oveja", "Pato", "Ganso", "Perico",
    "Tigre", "León", "Elefante", "Jirafa", "Mono", "Canguro", "Delfín", "Ballena", "Tiburón", "Pez",
    "Araña", "Hormiga", "Mariposa", "Mosquito", "Abeja", "Coche", "Autobús", "Moto", "Tren", "Avión",
    "Cohete", "Nave", "Estrella", "Planeta", "Luna", "Sol", "Cometa", "Universo", "Galaxia", "Espacio",
    "Robot", "Alien", "Nave", "Pirata", "Tesoro", "Mapa", "Isla", "Barco", "Sirena", "Monstruo",
    "Dragón", "Caballero", "Princesa", "Rey", "Reina", "Castillo", "Mago", "Bruja", "Hechizo", "Poción",
    "Fantasma", "Esqueleto", "Zombie", "Momia", "Vampiro", "Lobo", "Murciélago", "Rata", "Ratón", "Hámster",
    "Conejo", "Gato", "Perro", "Pájaro", "Pez", "Tortuga", "Serpiente", "Cocodrilo", "Rana", "Sapo",
    "Cangrejo", "Langosta", "Camello", "Cebra", "Rinoceronte", "Hipopótamo", "Pavo", "Gallina", "Pollo", "Pato",
    "Ganso", "Avestruz", "Flamenco", "Colibrí", "Búho", "Águila", "Halcón", "Lechuza", "Cuervo", "Pico",
    "Pluma", "Ala", "Cola", "Pata", "Garra", "Ojo", "Oreja", "Nariz", "Boca", "Diente",
    "Lengua", "Garganta", "Barriga", "Mano", "Brazo", "Pierna", "Pie", "Rodilla", "Codo", "Hombro"
]

# Leer palabras desde el archivo palabras.txt
def read_words(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            words = file.read().splitlines()
    else:
        words = random.sample(easy_words, k=len(easy_words))
    return words

# Función para generar el PDF
def generate_pdf(words, background_image, background_image_alternate):
    try:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"Tarjetas_juego_{timestamp}.pdf"
        print("Comenzando la generación del PDF...")

        c = canvas.Canvas(filename, pagesize=A4)
        print("Canvas creado correctamente.")

        # Tamaño de la página A4 en puntos
        width, height = A4

        # Tamaño de cada celda
        cell_width = (width - 1*inch - 0.25*inch) / 2
        cell_height = 5.4 * cm  # Alto de las celdas
        vertical_spacing = 1.2 * cm  # Separación entre celdas

        # Márgenes
        top_margin = 0.9 * cm  # Margen superior
        bottom_margin = 2.2 * cm  # Margen inferior

        # Configuración del borde
        c.setStrokeColorRGB(0, 0, 0)
        c.setLineWidth(1)

        # Fuente
        c.setFont("Helvetica-Bold", 16) 

        # Verificar si las imágenes de fondo existen
        bg_image_exists = os.path.exists(background_image)
        bg_image_alternate_exists = os.path.exists(background_image_alternate)

        page_count = 1
        words_remaining = list(words)  # Hacemos una copia de la lista para no modificar la original

        while words_remaining or page_count % 2 == 1:
            print(f"Generando página {page_count}...")

            # Determinar la imagen de fondo
            if page_count % 2 == 1:
                # c.drawImage(bg_image_alternate, 0, 0, width=width, height=height)
                if bg_image_alternate_exists:
                    bg_image = ImageReader(background_image_alternate)

                # Generar las tarjetas en la página actual
                for row in range(4):
                    for col in range(2):
                        x = col * (cell_width + 1*cm) + 0.5*inch
                        y = height - top_margin - (row + 1) * (cell_height + vertical_spacing)

                        if bg_image_alternate_exists:
                            # Determinar la imagen de fondo de la tarjeta
                            c.drawImage(bg_image, x, y, width=cell_width, height=cell_height)
                        else:
                            x = col * (cell_width + 1*cm) + 0.5*inch
                            y = height - top_margin - (row + 1) * (cell_height + vertical_spacing)
                            c.setFont("Helvetica-Bold", 52)
                            c.drawCentredString(x + cell_width / 2, y + cell_height / 2 + 26, "Time'S")
                            c.drawCentredString(x + cell_width / 2, y + cell_height / 2 - 26, "UP!")
                        
                        # Dibujar la celda
                        c.roundRect(x, y, cell_width, cell_height, 20, stroke=1, fill=0)

            else:
                # c.drawImage(bg_image, 0, 0, width=width, height=height)
                if bg_image_exists:
                    bg_image = ImageReader(background_image)

            # Generar las tarjetas en la página actual
                for row in range(4):
                    for col in range(2):
                        x = col * (cell_width + 1*cm) + 0.5*inch
                        y = height - top_margin - (row + 1) * (cell_height + vertical_spacing)

                        if bg_image_exists:
                            # Determinar la imagen de fondo de la tarjeta
                            c.drawImage(bg_image, x, y, width=cell_width, height=cell_height)
                        else:
                            c.setFillColorRGB(1, 1, 0)  # Amarillo
                            c.rect(x, y + cell_height/2, cell_width, cell_height/2, stroke=0, fill=1)
                            c.setFillColorRGB(0, 0, 1)  # Azul
                            c.rect(x, y, cell_width, cell_height/2, stroke=0, fill=1)

                        # Dibujar la celda
                        c.roundRect(x, y, cell_width, cell_height, 20, stroke=1, fill=0)

                        # Seleccionar dos palabras aleatorias
                        if words_remaining:
                            word1 = words_remaining.pop().capitalize()
                        else:
                            word1 = ""

                        if words_remaining:
                            word2 = words_remaining.pop().capitalize()
                        else:
                            word2 = ""

                        # Escribir la primera palabra centrada en la parte superior de la celda
                        c.setFont("Helvetica-Bold", 16)  # Usar la fuente Helvetica-Bold
                        c.setFillColorRGB(0, 0, 0)  # Color de la letra negro
                        c.drawCentredString(x + cell_width/2 - 40, y + cell_height*2/3, word1)

                        # Escribir la segunda palabra volteada 180 grados en la parte inferior de la celda
                        c.saveState()
                        c.translate(x + cell_width/2 - 15, y + cell_height/3)
                        c.rotate(180)
                        if not bg_image_exists:
                            c.setFillColorRGB(9, 9, 9)  # Color de la letra negro
                        c.drawCentredString(-65, 0, word2)
                        c.restoreState()

            # Agregar una nueva página si quedan palabras
            if words_remaining or page_count % 2 == 1:
                c.showPage()
                page_count += 1

        # Guardar el PDF
        c.save()
        print(f"PDF generado correctamente.")
        print("El archivo se ha guardado como:", filename)

    except Exception as e:
        print("Error al generar el PDF:", e)

# Ruta del archivo de palabras y de las imágenes de fondo
words_file_path = './palabras.txt'
background_image_path = './FondoTarjeta_A.jpg'
background_image_alternate_path = './FondoTarjeta_B.jpg'

# Leer las palabras del archivo
words = read_words(words_file_path)

# Generar el PDF
generate_pdf(words, background_image_path, background_image_alternate_path)