import csv
import os
from docx import Document
import re

# Contar instancias de los conceptos
def count_concepts_in_docx(docx_file):
    count_dict = {}
    doc = Document(docx_file)
    concepts_list = []
    for paragraph in doc.paragraphs:
        text = paragraph.text
        concepts_list.extend(re.findall(r"\*(.*?)\*", text))
    for concept in concepts_list:
        count_dict[concept] = count_dict.get(concept, 0) + 1
    return count_dict

# Carpeta donde están las entrevistas
folder_path = 'E:\\Histo_Internet\\Conteo_Entrevistas'

# Revisar si el archivo CSV existe
csv_filename = 'conteo_conceptos_archivo_v2.csv'
file_exists = os.path.exists(csv_filename)

# Escribir los datos al archivo CSV
with open(csv_filename, 'a', newline='') as csvfile:
    fieldnames = ['file', 'concept', 'count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Escribir header solo si el archivo no existe
    if not file_exists:
        writer.writeheader()

    # Iterar por todos los archivos DOCX en la carpeta
    for filename in os.listdir(folder_path):
        if filename.endswith('.docx') and not filename.startswith('~$'):
            docx_file = os.path.join(folder_path, filename)
            concept_counts = count_concepts_in_docx(docx_file)
            # Escribir los datos
            for concept, count in concept_counts.items():
                writer.writerow({'file': filename, 'concept': concept, 'count': count})