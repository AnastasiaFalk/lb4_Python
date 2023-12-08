from builtins import super, sum, len, max, range, input, float, print, map, int, ValueError

class WeatherForecast:
    def __init__(self, location, date):
        self.location = location
        self.date = date

class WaterForecast(WeatherForecast):
    def __init__(self, location, date, water_temperature, waves):
        super().__init__(location, date)
        self.water_temperature = water_temperature
        self.waves = waves

    def average_water_temperature(self):
        return sum(self.water_temperature) / len(self.water_temperature)

    def highest_wave_speed(self):
        max_index = self.waves.index(max(self.waves))
        return f"Найбільша швидкість хвилі {self.date[max_index]} зі значенням {self.waves[max_index]} м/с"

    def dates_above_temperature_threshold(self, threshold=20):
        above_threshold_dates = [self.date[i] for i in range(len(self.water_temperature)) if self.water_temperature[i] > threshold]
        return f"Дні, коли температура перевищувала 20°: {', '.join(above_threshold_dates)}"

def validate_date(date_str):
    try:
        day, month, year = map(int, date_str.split('/'))
        if 1 <= day <= 30 and 1 <= month <= 12 and 0 <= year <= 2024:
            return True
        else:
            return False
    except ValueError:
        return False

location = input("Введіть місце: ")
forecast_dates = input("Введіть три дати прогнозу (дд/мм/рррр дд/мм/рррр дд/мм/рррр): ").split()

for date in forecast_dates:
    while not validate_date(date):
        print("Будь ласка, введіть правильну дату.")
        date = input("Введіть дату заново: ")

water_temperature = []
for date in forecast_dates:
    temperature = float(input(f"Температура {date}: "))
    water_temperature.append(temperature)

waves = []
for date in forecast_dates:
    wave_speed = float(input(f"Введіть швидкість хвилі (м/с) для {date}: "))
    waves.append(wave_speed)

forecast_water = WaterForecast(location, forecast_dates, water_temperature, waves)

print(f"Середня температура води: {forecast_water.average_water_temperature():.1f}°.")
print(forecast_water.highest_wave_speed())
print(forecast_water.dates_above_temperature_threshold())