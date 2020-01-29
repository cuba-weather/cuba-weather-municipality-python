def curateMunicipality(municipality : str) -> str :
  municipality = municipality.lower()
  municipality = municipality.replace('á', 'a')
  municipality = municipality.replace('é', 'e')
  municipality = municipality.replace('í', 'i')
  municipality = municipality.replace('ó', 'o')
  municipality = municipality.replace('ú', 'u')
  municipality = municipality.replace('ü', 'u')
  municipality = municipality.replace('ñ', 'n')
  municipality = municipality.replace('-', '')

  return municipality