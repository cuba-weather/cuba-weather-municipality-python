from ..data_providers import municipalities
from ..models import MunicipalityModel
from ..utils import curateMunicipality, distance

class MunicipalityRepository:
  '''
  Class to provide the functionality of searching for a municipality
  '''

  def getMunicipality(self, municipalityQuery: str) -> MunicipalityModel:
    '''
      Method that returns the best match of the given municipality with the
      cuban municipalities. The best match is considered as the cuban
      municipality of shorter length that contains the given municipality.
    '''
    municipalityQuery = curateMunicipality(municipalityQuery)

    for m in municipalities:
      if (municipalityQuery in m.nameCured) or (m.nameCured in municipalityQuery):
        return m

    return None
  
  def getSuggestion(self, municipalityQuery : str) -> MunicipalityModel:
    '''
      Method that returns the best match of the given municipality with the
      cuban municipalities. The best match is calculated using the
      Damerau-Levenshtein distance.
    '''

    municipalityQuery = curateMunicipality(municipalityQuery);
    
    bestMunicipality : MunicipalityModel = municipalities[0];
    bestDistance : int = distance(municipalityQuery, bestMunicipality.nameCured);
    
    for i in range(1, len(municipalities)):
      tmpMunicipality = municipalities[i]
      tmpDistance = distance(municipalityQuery, tmpMunicipality.nameCured)

      if tmpDistance < bestDistance:
        bestMunicipality = tmpMunicipality
        bestDistance = tmpDistance

    return bestMunicipality
