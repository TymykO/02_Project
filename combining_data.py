from datetime import datetime, timezone

from loading_meteo_data import combined_all_meteo_data
from loading_valve_data import valve_data_list

meteo_data = combined_all_meteo_data('B00300S', '352200375', './Meteo')
valve_data = valve_data_list("Valve/export-TA-Smart-TA-Smart 50 532290B7.csv")

print(meteo_data[0])
print(valve_data[0])

data = []

for x in meteo_data:
    eu_time = datetime.strptime(x[1], '%Y-%m-%d %H:%M').replace(tzinfo=timezone.utc)
    for y in valve_data:
        #iso_time = datetime.fromisoformat(y[0])
        if y[0] == 'Full Date':
            data.append(y.append('Temperature outside [°C]'))
        elif datetime.fromisoformat(y[0]) == eu_time:
            data.append(y.append(x[2]))

print(data[0])
print(data[1])

#combining_data_by_time

