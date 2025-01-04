from datetime import datetime, timezone

from loading_meteo_data import combined_all_meteo_data
from loading_valve_data import valve_data_list

meteo_data = combined_all_meteo_data('B00300S', '352200375', './Meteo')
valve_data = valve_data_list("Valve/export-TA-Smart-TA-Smart 50 532290B7.csv")

print(meteo_data[0])
print(valve_data[0])

#combining_data_by_time

