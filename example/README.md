# Cuba Weather Municipality Python Examples

Example of tool implemented in Python for the Cuba Weather project to work with the municipalities of Cuba.

```python
from cuba_weather_municipality import CubaWeatherMunicipality

input = input('Insert municipality: ')
cubaWeatherMunicipality = CubaWeatherMunicipality()
municipality = cubaWeatherMunicipality.get(input, suggestion=True)
print(municipality)
```
