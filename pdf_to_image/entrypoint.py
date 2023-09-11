# pip install PyMuPDF
import fitz  # Importar la biblioteca PyMuPDF

# Ruta al archivo PDF de entrada
pdf_file = 'ContratoPrestacionServiciosFelipeGonzalez.pdf'

# Abre el archivo PDF
pdf_document = fitz.open(pdf_file)

# Itera sobre las páginas del PDF
for page_number in range(len(pdf_document)):
    # Obtiene la página
    page = pdf_document[page_number]

    # Convierte la página en una imagen (formato PIL)
    image = page.get_pixmap()

    # Guarda la imagen en formato PNG (o cualquier otro formato de imagen que desees)
    image.save(f'pagina_{page_number + 1}.png')

# Cierra el documento PDF
pdf_document.close()