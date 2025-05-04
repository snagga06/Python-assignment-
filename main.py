from temperature_toolkit.record import TemperatureRecord
from temperature_toolkit.analytics import *

# Create sample temperature records
day1 = TemperatureRecord('2025-04-27', [14.2, 15.0, 13.8, 14.5, 15.1, 14.0], 'celsius')
day2 = TemperatureRecord('2025-04-28', [17.1, 18.5, 16.4, 17.0, 18.0, 16.8], 'celsius')
day3 = TemperatureRecord('2025-04-29', [11.0, 9.5, 12.2, 10.0, 11.3, 10.7], 'celsius')

records = [day1, day2, day3]

# Convert day1 to Fahrenheit
day1.convert_to('fahrenheit')

# Display summaries
for r in records:
    print(r.get_summary())

print("\nAverage temperature across all days:", average_temperature_across_days(records))
print("Hottest day:", hottest_day(records))
print("Extreme days above 17.5°C:", detect_extreme_days(records, 17.5))
print("Daily temperature ranges:", temperature_range_for_each_day(records))

print("\nTemperature trend for day2:", temperature_trend(day2.readings))
print("Spike detected in day3:", detect_spike(day3.readings, threshold=2.5))
