
from loading_meteo_data import combined_all_meteo_data
from loading_valve_data import valve_data_list

meteo_data = combined_all_meteo_data('B00300S', '352200375', './Meteo')
valve_data = valve_data_list("Valve/export-TA-Smart-TA-Smart 50 532290B7.csv")

print(meteo_data[0])
print(valve_data[0])
print(valve_data[1])
print('\n\n\n--------------------\n\n\n')


from datetime import datetime, timezone

# Функція для перетворення дат у форматі meteo_data
def parse_meteo_date(date_str):
    try:
        return datetime.strptime(date_str, '%Y-%m-%d %H:%M').replace(tzinfo=timezone.utc)
    except ValueError:
        return False

# Функція для перетворення дат у форматі valve_data
def parse_valve_date(date_str):
    try:
        return datetime.fromisoformat(date_str).astimezone(timezone.utc)
    except ValueError:
        return False

def process_data(meteo_data, valve_data):
    data = []
    a = 0

    if valve_data[0][0] == 'Full Date':
        valve_data[0].append('Full Date meteo')
        valve_data[0].append('Temperature outside [°C]')
        data.append(valve_data[0])

    for i, x in enumerate(valve_data[1:], start=1):
        a += 1
        if a > 300:
            break
        valve_time = parse_valve_date(x[0])
        if valve_time is False:
            continue

        for j, y in enumerate(meteo_data):

            meteo_time = parse_meteo_date(y[1])
            if meteo_time is False:
                continue
            elif valve_time == meteo_time:
                x.append(meteo_time.isoformat())
                x.append(meteo_data.pop(j)[2])
                data.append(valve_data.pop(i))

    return data

result = process_data(meteo_data, valve_data)


print('\n--------------------\n')
print(f'\n\n---{len(result)}---\n\n')
print('\n--------------------\n')

print(result[0])
print(result[1])
print(result[2])
print(result[3])
print(result[4])
print(result[5])
print(result[6])
print(result[7])
print(result[8])