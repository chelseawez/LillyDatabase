import csv
import urllib
import general_functions as gen
    
def getLanguagesDict():
	import xml.etree.ElementTree as ET
	LANG_CODE_URL = 'http://www.loc.gov/standards/codelists/languages.xml'

	str = '{info:lc/xmlns/codelist-v1}'
	url = LANG_CODE_URL
	root = ET.parse(urllib.urlopen(url)).getroot()
	dict = {}
	for element in root.iter(str+'language'):
	    code = element.find(str+'code').text
	    name = element.find(str+'name').text
	    dict[code] = name
	return dict
			
with open('Lilly DVD Assets.csv', 'rb') as f:
    reader = csv.DictReader(f)
    delim = '|'
    langDict = getLanguagesDict()
    mediaDict = gen.getDict2()
    for row in reader:
        processStatus = row["Process Status Desc"]
        material = row["Material Type Desc"]
        mediaID = row["Bib Doc Number"]
        if ((processStatus != "Withdrawn" and processStatus != "Suppressed" and processStatus != "Canceled") and (material == "Video Cassette" or material == "DVD") and mediaID in mediaDict):
            lang = row["Language ID"].lower()
            actualLang = ""
            if lang in langDict:
                actualLang = langDict[lang]
            else:
                actualLang = lang
            newRow = mediaID + delim + actualLang
            print newRow.encode('utf-8')
