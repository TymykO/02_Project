import csv

def read_data_valve(path_csv: str):
    try:
        with open(path_csv, 'r', encoding='utf-8') as file_csv:
            data_csv = list(csv.reader(file_csv))
            column_name = []
            data = []

            if len(data_csv[0]) == len(data_csv[1]):
                row = []
                for i in range(len(data_csv[0])):
                    key_1 = data_csv[0][i]
                    key_2 = data_csv[1][i]
                    if key_2 != 'N/A':
                        key_0 = f'{key_1} [{key_2}]'
                    else:
                        key_0 = str(data_csv[0][i])
                    row.append(key_0)
                column_name.append(row)

            print(column_name)



            a = 0

            for x in data_csv[2:]:
                data.append(x)



                a += 1
                print(x)
                if a > 10:
                    break
            print(data)
    except:
        # to do except
        pass
    return data

path = "Valve/export-TA-Smart-TA-Smart 50 532290B7.csv"

read_data_valve(path)