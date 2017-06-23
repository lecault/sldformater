#Transformer un style SLD issu de QGIS en un style GeoServer

import fileinput, glob

#Textes a remplacer issus du style QGis
se = 'se:'
SvgParameter = 'SvgParameter'
Description1 = '          <Description>\n'
Description2 = '          </Description>\n'
escapeChar = 'escapeChar='

#Textes SLD GeoServer
vide =  ''
CssParameter =  'CssParameter'
escape =  'escape='

#Entete du fichier a modifier
sldqgis= '<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.1.0/StyledLayerDescriptor.xsd" xmlns:se="http://www.opengis.net/se">'
slddef = '<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:sld="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:gml="http://www.opengis.net/gml" version="1.0.0">'

#On modifie les SLD du repertoire du script
slds = glob.glob('*.sld')

for sld in slds:
    # Read in the file
    with open(sld, 'r') as file :
      filedata = file.read()
    # Replace the target string
    filedata = filedata.replace(se, vide)
    filedata = filedata.replace(SvgParameter, CssParameter)
    filedata = filedata.replace(escapeChar, escape)
    filedata = filedata.replace(Description1, vide)
    filedata = filedata.replace(Description2, vide)
    filedata = filedata.replace(sldqgis, slddef)
    # Write the file out again
    with open(sld, 'w') as file:
        file.write(filedata)
