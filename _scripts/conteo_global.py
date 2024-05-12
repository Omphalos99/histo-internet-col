import csv
import os
import re

# Contar instancias de concepto en archivos.txt
def contar_conceptos_en_txt(txt_file):
    conteo = {}
    with open(txt_file, 'r', encoding='utf-8') as file:
        text = file.read()
        lista = re.findall(r"\*(.*?)\*", text)
    for concept in lista:
        conteo[concept] = conteo.get(concept, 0) + 1
    return conteo

# Carpeta donde están las entrevistas
folder_path = 'E:\\Histo_Internet\\Conteo_Entrevistas\\TXT'

# Revisar si existe el csv
csv_filename = 'conteo global.csv'
file_exists = os.path.exists(csv_filename)

# Leer datos del csv si existe
concept_count = {}
if file_exists:
    with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            concept_count[row['concept']] = concept_count.get(row['concept'], 0) + int(row['count'])

# Escribir datos al csv
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['concept', 'count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Escribir header
    writer.writeheader()

    # Iterar por todos los txt en la carpeta
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt') and not filename.startswith('~$'):
            txt_file = os.path.join(folder_path, filename)
            conteo = contar_conceptos_en_txt(txt_file)
            # Actualizar conteo global
            for concept, count in conteo.items():
                concept_count[concept] = concept_count.get(concept, 0) + count

    # Escribir conteo final al CSV
    for concept, count in concept_count.items():
        writer.writerow({'concept': concept, 'count': count})
