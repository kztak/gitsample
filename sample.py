import pandas as
from arcgis import GIS

gis = GIS('https://ej.maps.arcgis.com', 'kazunari_takaki', 'rock0001')

item_list = gis.content.search('sample')

