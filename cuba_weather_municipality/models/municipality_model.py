class MunicipalityModel:
  '''
    Class of represent a Municipality
  '''

  def __init__(self, name: str, lat: float, lon: float, nameCured: str):
    self.name = name
    self.lat = lat
    self.lon = lon
    self.nameCured = nameCured

  def __str__(self):
    return self.__repr__()

  def __repr__(self):
    result = '''
      Name: {name}\n
      Latitude: {lat}\n
      Longitude: {lon}\n
      Name Cured: {nameCured}
    '''

    return result.format(
      name=self.name,
      lat=self.lat,
      lon=self.lon,
      nameCured=self.nameCured
    )
