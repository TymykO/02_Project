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
            for x in data_csv[2:]:
                data.append(x)
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
            for x in data_csv[2:]:
                row = []
                for i, value in enumerate(keyword):
                    element = f'{value}: {x[i]}'
                    row.append(element)
                data.append(row)
    except:
        # to do except
        pass
    return data

if __name__ == "__main__":
    assert valve_data_dict("Valve/export-TA-Smart-TA-Smart 50 532290B7.csv")[0] == ['Full Date: 2023-02-07T09:45:45+00:00', 'Year: 2023', 'Month: 2', 'Day: 7', 'Hour: 9', 'Minute: 45', 'Second: 45', 'Error Status: ', 'Control Mode: Position control', 'Override Status: None', 'Current Change-Over Regime: Regime 1', 'Temperature Limitation Status: Deactivated', 'Target flow for temp limitation (vs setpoint) [%]: 0.0', 'Actuator Position [mm]: 15.70', 'Measured Flow [l/h]: 3147.9', 'Measured Delta Temp. [K]: 16.9', 'Measured local Temp. [°C]: 58.5', 'Measured remote Temp. [°C]: 41.6', 'Measured Power [kW]: 61.19', 'Energy Counter Regime 1 [kWh]: 24', 'Energy Counter Regime 2 [kWh]: 0', 'Analog Input Signal [V]: 0.0', 'Bus Relative Setpoint [%]: 0.0', 'Relative Actuator position [%]: 100.0', 'Relative Measured Flow [%]: 23.5', 'Relative Measured Power [%]: 7.9'], "OK"
    assert valve_data_list("Valve/export-TA-Smart-TA-Smart 50 532290B7.csv")[0] == ['Full Date', 'Year', 'Month', 'Day', 'Hour', 'Minute', 'Second', 'Error Status', 'Control Mode', 'Override Status', 'Current Change-Over Regime', 'Temperature Limitation Status', 'Target flow for temp limitation (vs setpoint) [%]', 'Actuator Position [mm]', 'Measured Flow [l/h]', 'Measured Delta Temp. [K]', 'Measured local Temp. [°C]', 'Measured remote Temp. [°C]', 'Measured Power [kW]', 'Energy Counter Regime 1 [kWh]', 'Energy Counter Regime 2 [kWh]', 'Analog Input Signal [V]', 'Bus Relative Setpoint [%]', 'Relative Actuator position [%]', 'Relative Measured Flow [%]', 'Relative Measured Power [%]'], "OK"
    assert valve_data_dict("Valve/test.csv")[0] == 'Incorrect valve data', "OK"
    assert valve_data_list("Valve/test.csv")[0] == 'Incorrect valve data', "OK"
