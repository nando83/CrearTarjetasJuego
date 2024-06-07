from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch, cm
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.utils import ImageReader
import random
from datetime import datetime

# Leer palabras desde el archivo palabras.txt
def read_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.read().splitlines()
    return words

# Función para generar el PDF
def generate_pdf(words, background_image):
    try:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"tarjetas_{timestamp}.pdf"
        print("Comenzando la generación del PDF...")

        c = canvas.Canvas(filename, pagesize=A4)
        print("Canvas creado correctamente.")

        # Tamaño de la página A4 en puntos
        width, height = A4

        # Tamaño de cada celda
        cell_width = (width - 1*inch - 0.25*inch) / 2
        cell_height = (height - 1.5 * inch - 0.5 * cm) / 4 

        # Configuración del borde
        c.setStrokeColorRGB(0, 0, 0)
        c.setLineWidth(1)

        # Usar fuente Arial
        c.setFont("Helvetica-Bold", 16)  # Arial y Helvetica son muy similares

        # Cargar la imagen de fondo
        bg_image = ImageReader(background_image)

        page_count = 1
        words_remaining = list(words)  # Hacemos una copia de la lista para no modificar la original

        while words_remaining:
            print(f"Generando página {page_count}...")

            # Dibujar la imagen de fondo en toda la página
            c.drawImage(bg_image, 0, 0, width=width, height=height)

            # Generar las tarjetas en la página actual
            for row in range(4):
                for col in range(2):
                    x = col * (cell_width + 1*cm) + 0.5*inch 
                    y = height - (row + 1) * (cell_height + 1*cm) + 0.5*cm

                    # Dibujar la celda
                    #c.roundRect(x, y, cell_width, cell_height, 5, stroke=1, fill=0)

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
                    c.setFont("Helvetica-Bold", 16)  # Aumentar el tamaño de la fuente a 16 puntos
                    c.drawRightString(x + cell_width/2 - 25, y + cell_height*2/4, word1)

                    # Escribir la segunda palabra volteada 180 grados en la parte inferior de la celda
                    c.saveState()
                    c.translate(x + cell_width/2 - 15, y + cell_height/4)
                    c.rotate(180)
                    c.drawCentredString(-55, 10, word2)
                    c.restoreState()

            # Agregar una nueva página si quedan palabras
            if words_remaining:
                c.showPage()
                page_count += 1

        # Guardar el PDF
        c.save()
        print(f"PDF generado correctamente.")
        print("El archivo se ha guardado como:", filename)

    except Exception as e:
        print("Error al generar el PDF:", e)

# Ruta del archivo de palabras y de la imagen de fondo
words_file_path = './palabras.txt'
background_image_path = './fondoTimesUp_A.jpg'

# Leer las palabras del archivo
words = read_words(words_file_path)

# Generar el PDF
generate_pdf(words, background_image_path)