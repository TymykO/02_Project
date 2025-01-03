import os
import loading_meteo_data

folder = './Meteo'
combined_data = []

for file in os.listdir(folder):
    if file.endswith('.zip'):
        meteo_data = loading_meteo_data.read_csv_from_zip(os.path.join(folder, file), 'B00300S', '352200375')
        for x in meteo_data:
            combined_data.append(x)

with open('oll_data.csv', 'w', encoding='utf-8') as data_file:
    for x in combined_data:
        data_file.write(f'{x}\n')

