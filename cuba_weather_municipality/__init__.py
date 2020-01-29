__version__ = '0.1.3'

from .models import MunicipalityModel
from .repositories import MunicipalityRepository

class CubaWeatherMunicipality:
  '''
    Main class to provide package functionality.
  '''
  def __init__(self):
    self._repository = MunicipalityRepository()

  def get(self, municipalityQuery : str, suggestion = False) -> MunicipalityModel :
    '''
      Method that given a municipality of the user searches the cuban
      municipalities to find the best match and returns the municipality. The
      best match is considered as the cuban municipality of shorter length
      that contains the given municipality.
    '''
    municipality = self._repository.getMunicipality(municipalityQuery)
    
    if suggestion and not municipality :
      municipality = self._repository.getSuggestion(municipalityQuery)
    
    return municipality

  def suggestion(self, municipality : str) -> MunicipalityModel :
    '''
      Method that returns the best match of the given municipality with the
      cuban municipalities. The best match is calculated using the
      Damerau-Levenshtein distance.
    '''
    return self._repository.getSuggestion(municipality)