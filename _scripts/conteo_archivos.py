import csv
import os
import re

# Contar instancias de los conceptos
def count_concepts_in_txt(txt_file):
    count_dict = {}
    with open(txt_file, 'r', encoding='utf-8') as file:
        for line in file:
            concepts_list = re.findall(r"\*(.*?)\*", line)
            for concept in concepts_list:
                count_dict[concept] = count_dict.get(concept, 0) + 1
    return count_dict

# Carpeta donde están las entrevistas
folder_path = 'E:\\Histo_Internet\\Conteo_Entrevistas\\TXT'

# Revisar si el archivo CSV existe
csv_filename = 'conteo_por_archivo.csv'
file_exists = os.path.exists(csv_filename)

# Escribir los datos al archivo CSV
with open(csv_filename, 'a', newline='') as csvfile:
    fieldnames = ['file', 'concept', 'count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Escribir header solo si el archivo no existe
    if not file_exists:
        writer.writeheader()

    # Iterar por todos los archivos TXT en la carpeta
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            txt_file = os.path.join(folder_path, filename)
            concept_counts = count_concepts_in_txt(txt_file)
            # Escribir los datos
            for concept, count in concept_counts.items():
                writer.writerow({'file': filename, 'concept': concept, 'count': count})