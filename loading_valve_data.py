import csv

def read_data_valve(path_csv: str):
    try:
        with open(path_csv, 'r', encoding='utf-8') as file_csv:
            data_csv = list(csv.reader(file_csv))
    except:
        # to do except
        pass
    return data_csv

def valve_data_list(path_csv: str):
    data_csv = read_data_valve(path_csv)
    data = []
    try:
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
                data.append(row)
            else:
                data = 'Incorrect valve data'
                return data
            a = 0
            for x in data_csv[2:]:
                data.append(x)
                a += 1
                if a > 10:
                    break
    except:
        # to do except
        pass
    return data

def valve_data_dict(path_csv: str):
    data_csv = read_data_valve(path_csv)
    data = []
    try:
            if len(data_csv[0]) == len(data_csv[1]):
                keyword = []
                for i in range(len(data_csv[0])):
                    key_1 = data_csv[0][i]
                    key_2 = data_csv[1][i]
                    if key_2 != 'N/A':
                        key_0 = f'{key_1} [{key_2}]'
                    else:
                        key_0 = str(data_csv[0][i])
                    keyword.append(key_0)
            else:
                data = 'Incorrect valve data'
                return data
            a = 0
            for x in data_csv[2:]:
                row = []
                for i, value in enumerate(keyword):
                    element = f'{value}: {x[i]}'
                    print(element)
                    row.append(element)
                data.append(row)
                a += 1
                if a > 10:
                    break
    except:
        # to do except
        pass
    return data



path = "Valve/export-TA-Smart-TA-Smart 50 532290B7.csv"

print(valve_data_dict(path))
