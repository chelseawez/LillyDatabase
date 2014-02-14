#in Actor, line 8958 has media id but didnt have performer
#in Production, uses a quote that doesn't have an end quote - freakout

import string

def getDict():
    ins = open("Media.dat", "r")
    mediaDict = {}
    for line in ins:
        parts = line.split('|')
        mediaDict[parts[0]] = True
        
    return mediaDict;

media_file = open("Language.dat", "r")
# key media id
#mediaDict = getDict()
tvDict = {}
for line in media_file:
     fields = line.split('|')
     id_season = fields[0] + fields[1]
     if id_season in tvDict:
         pass
     else:
         print line,
         tvDict[id_season] = True
     
media_file.close()
