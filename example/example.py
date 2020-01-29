from cuba_weather_municipality import CubaWeatherMunicipality

input = input('Insert municipality: ')
cubaWeatherMunicipality = CubaWeatherMunicipality()
municipality = cubaWeatherMunicipality.get(input, suggestion=True)
print(municipality)
