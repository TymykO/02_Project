import zipfile
import os

def read_csv_from_zip(zip_path: str, parameter_code: str, station_code: str):
    try:
        with zipfile.ZipFile(zip_path, 'r') as z:

            for file_name in z.namelist():
                if file_name.endswith('.csv') and file_name.startswith(parameter_code):

                    with z.open(file_name, 'r') as csv_file:
                        csv_data = csv_file.readlines()

                        data_station = []

                        for x in csv_data:
                            line = x.decode('utf-8').strip().split(';')
                            if line[0] == station_code and line[1] == parameter_code:
                                value = line[3].replace(',','.')
                                data_station.append([line[0],line[2],value])
        return data_station
    except IndexError:
        print("Error Index")
        return []
    except FileNotFoundError:
        print("Error File")
        return []

def combined_all_meteo_data(parameter_code: str='B00300S', station_code: str='352200375', folder: str='./Meteo'):
    combined_data = []
    try:
        for file in os.listdir(folder):
            if file.endswith('.zip'):
                meteo_data = read_csv_from_zip(os.path.join(folder, file),parameter_code, station_code)
                for x in meteo_data:
                    combined_data.append(x)
    except FileNotFoundError:
        print("Error File")
        return []
    return combined_data


if __name__ == "__main__":

    assert read_csv_from_zip('Meteo/Meteo_2023-01.zip', 'B00300S', '352200375')[0] == '352200375;2023-01-01 00:00;13.9', print(" not OK1")
    print("OK1")
    assert read_csv_from_zip('Meteo/Meteo_2023-01.zip', 'B00702A', '352200375')[0] == '352200375;2023-01-01 00:00;2.7', print(" not OK2")
    print("OK2")