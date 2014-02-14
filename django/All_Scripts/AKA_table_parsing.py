import csv
import tmdb
import string

tmdb.set_key("632e13506ef012eb41a058393cf20976")
    
def allPunctuation(title):
    exclude = set(string.punctuation)
    exclude.add('_')
    exclude.add(' ')
    exclude.add('0123456789')
    s = ''.join(ch for ch in title if ch not in exclude)
    if s == "":
        return True
    else:
        return False

import csv 
with open('Lilly DVD Assets.csv', 'rb') as f:
    reader = csv.DictReader(f)
    delim = '|'
    for row in reader:
        processStatus = row["Process Status Desc"]
        material = row["Material Type Desc"]
        if ((processStatus != "Withdrawn" and processStatus != "Suppressed" and processStatus != "Canceled") and (material == "Video Cassette" or material == "DVD" or material == "A-V")):
             alt_titles = row["Desc11"]
             if(alt_titles != ""):
                   mediaID = row["Bib Doc Number"]
                   for title in alt_titles.split('|'):
                        if (title != "") and (allPunctuation(title) == False):
                            title = title.replace("|", " - ");
                            if title[len(title)-1] in string.punctuation:
                                title = title[:len(title)-1]
                            newRow = str(int(mediaID)) + delim + title
                            newRow = mediaID + delim + title.strip()
                            print newRow.decode('iso-8859-1').encode('utf8')