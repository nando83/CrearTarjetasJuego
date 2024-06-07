from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
import random
from datetime import datetime

# Lista de palabras
words = [
    "Gato", "Perro", "Casa", "Jardín", "Escuela", "Maestro", "Libro", "Lápiz", "Mesa", "Silla",
    "Ventana", "Puerta", "Coche", "Bicicleta", "Avión", "Tren", "Amigo", "Familia", "Comida", "Agua",
    "Leche", "Juguete", "Pelota", "Música", "Canción", "Baile", "Pintura", "Dibujo", "Televisión", "Computadora",
    "Teléfono", "Árbol", "Flor", "Sol", "Luna", "Estrella", "Mar", "Playa", "Montaña", "Río",
    "Parque", "Animal", "Gallo", "Vaca", "León", "Tigre", "Elefante", "Mono", "Pingüino", "Oso",
    "Ratón", "Tortuga", "Serpiente", "Pez", "Tiburón", "Delfín", "Roca", "Tierra", "Fuego", "Aire",
    "Viento", "Nube", "Lluvia", "Nieve", "Rayo", "Trueno", "Zapato", "Camisa", "Pantalón", "Sombrero",
    "Abrigo", "Calcetín", "Reloj", "Gafas", "Anillo", "Collar", "Bolsa", "Mochila", "Banco", "Dinero",
    "Moneda", "Billete", "Tienda", "Mercado", "Panadería", "Supermercado", "Médico", "Enfermera", "Hospital", "Farmacia",
    "Policía", "Bombero", "Universidad", "Biblioteca", "Cine", "Teatro", "Jardín", "Plaza", "Calle", "Carretera",
    "Puente", "Túnel", "Edificio", "Iglesia", "Torre", "Castillo", "Palacio", "Estatua", "Fuente", "Zoológico",
    "Acuario", "Parque", "Estadio", "Gimnasio", "Piscina", "Playa", "Valle", "Desierto", "Cueva", "Isla",
    "Océano", "Lago", "Cascada", "Árbol", "Planta", "Fruto", "Semilla", "Raíz", "Hoja", "Tallo",
    "Ramo", "Campo", "Granja", "Tractor", "Vaca", "Oveja", "Caballo", "Cerdo", "Gallina", "Pato",
    "Ganso", "Pavo", "Conejo", "Ratón", "Hormiga", "Abeja", "Mariposa", "Caracol", "Araña", "Cangrejo",
    "Pez", "Medusa", "Estrella de mar", "Pulpo", "Tiburón", "Ballena", "Delfín", "Silla", "Mesa", "Cama",
    "Sofá", "Armario", "Estante", "Lámpara", "Radio", "Teléfono", "Teclado", "Ratón", "Pantalla", "Impresora",
    "Cámara", "Reloj", "Juguete", "Pelota", "Bicicleta", "Patinete", "Monopatín", "Coche", "Autobús", "Tren",
    "Avión", "Barco", "Submarino", "Cohete", "Platillo volador", "Helado", "Pastel", "Chocolate", "Galleta", "Caramelo",
    "Tarta", "Bizcocho", "Cereza", "Fresa", "Sandía", "Melón", "Kiwi", "Mango", "Papaya", "Guayaba",
    "Limón", "Lima", "Pomelo", "Mandarina", "Coco", "Higo", "Chirimoya", "Granadilla", "Aceituna", "Alcaparra"
]
# Función para generar el PDF
def generate_pdf(words):
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
        cell_height = (height - 1.6*inch) / 4

        # Configuración del borde
        c.setStrokeColorRGB(0, 0, 0)
        c.setLineWidth(1)

        page_count = 1
        words_remaining = list(words)  # Hacemos una copia de la lista para no modificar la original

        while words_remaining:
            print(f"Generando página {page_count}...")

            # Generar las tarjetas en la página actual
            for row in range(4):
                for col in range(2):
                    x = col * (cell_width + 0.25*inch) + 0.5*inch
                    y = height - (row + 1) * (cell_height + 0.25*inch) - 0.25*inch

                    # Dibujar la celda
                    c.roundRect(x, y, cell_width, cell_height, 5, stroke=1, fill=0)

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
                    c.setFont("Helvetica", 16)
                    c.drawRightString(x + cell_width/2 - 20, y + cell_height*2/3, word1)

                    # Escribir la segunda palabra volteada 180 grados en la parte inferior de la celda
                    c.saveState()
                    c.translate(x + cell_width/2 - 15, y + cell_height/3)
                    c.rotate(180)
                    c.drawCentredString( - 60, 0, word2)
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

generate_pdf(words)