import csv
import unicodedata
import tmdb

tmdb.set_key('632e13506ef012eb41a058393cf20976')
num_th = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth", "thirteenth", "fourteenth", "sixteenth", "seventeenth", "eighteenth", "nineteenth", "twentieth"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
num_spell = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
                  
def getPrimaryTitle(primary_title):
    if (primary_title.lower().find('[videorecording]') != -1):
        primary_title = primary_title[:primary_title.lower().find('[videorecording]')]            
    for i in num_th:
         if (primary_title.lower().find(('the complete ' + i + ' season on DVD')) != -1):
              primary_title = primary_title[:primary_title.lower().find(('complete ' + i + ' season on DVD'))]
         elif (primary_title.lower().find(('the complete ' + i + ' season')) != -1):
              primary_title = primary_title[:primary_title.lower().find(('complete ' + i + ' season'))]
    for i in numbers:
         if (primary_title.lower().find(('season ' + i)) != -1):
              primary_title = primary_title[:primary_title.lower().find(('season ' + i))]
    for i in num_spell:
         if (primary_title.lower().find(('season ' + i)) != -1):
              primary_title = primary_title[:primary_title.lower().find(('season ' + i))]

    primary_title = primary_title.strip()
    if (primary_title.endswith(":") or primary_title.endswith("/") or primary_title.endswith(",") or primary_title.endswith("=")):
        primary_title = primary_title[:-1]
    if (primary_title.endswith(".") and primary_title[-2:-1] != '.'):
        primary_title = primary_title[:-1]
    primary_title = primary_title.strip()
    return primary_title

def getTitleSort(primary_title):
    title_sort = ""
    if (primary_title.lower().startswith('a ')):
         title_sort = primary_title[1:]
    elif (primary_title.lower().startswith('the ')):
         title_sort = primary_title[3:]
    elif (primary_title.lower().startswith('an ')):
         title_sort = primary_title[2:]
    else:
         title_sort = primary_title
    return title_sort.strip()

def getFilmOrTV(title):
    try:
        for i in num_th:
            if (title.lower().find(('complete ' + i + ' season')) != -1):
                return "TV"
        for i in numbers:
            if (title.lower().find(('season ' + i)) != -1):
                return "TV"
        for i in num_spell:
            if (title.lower().find(('season ' + i)) != -1):
                return "TV"
        return "Film"
    except UnicodeEncodeError as e:
        return "Film"

def getTmdbIdForFilm(primary_title):
    res = tmdb.searchMovie(primary_title)
    if res:
        return res[0].id
    return "NONE"

def getCountry(movie):
    allCountries = movie.countries
    if not allCountries:
        return "NONE"
    return allCountries[0].name

def getTagline(movie):
    tagline = movie.tagline
    if not tagline:
        return "NONE"
    return tagline
    
def getRating(movie):
    code = 'US'
    if code in movie.releases:
        rating = movie.releases[code].certification
        if rating:
            return rating
    return "No US rating"
 
with open('Lilly DVD Assets.csv', 'rb') as f:
    dict_file = open('media_dict','w')
    mDict = {}
    reader = csv.DictReader(f)
    delim = '|'
    for row in reader:
        try:
            processStatus = row["Process Status Desc"]
            itemID = row["Barcode"]
            material = row["Material Type Desc"]
            mediaID = row["Bib Doc Number"]
            if ((itemID[:1] != "B") and (processStatus != "Withdrawn" and processStatus != "Suppressed" and processStatus != "Canceled") and (material == "Video Cassette" or material == "DVD" or material == "A-V") and (mediaID not in mDict)):
                if (row["Collection ID"] == "PLAV"): 
                    tryMatching = False
                else:
                    tryMatching = True
                mDict[mediaID] = True
                formatMedia = "NONE"
                if (row["Material Type Desc"] == "DVD"):
                     formatMedia = "DVD"
                elif (row["Material Type Desc"] == "Video Cassette"):
                     formatMedia = "VHS"
                else:
                     if (mediaID.find("DVD") != -1):
                         formatMedia = "DVD"
                     elif (mediaID.find("VC") != -1):
                         formatMedia = "VHS"
                primaryTitle = getPrimaryTitle(row["Title"])
                if primaryTitle == "#NAME?":
                    continue
                titleSort = getTitleSort(primaryTitle)
                filmOrTV = getFilmOrTV(row["Desc8"])
                tmdbID = "NONE"
                country = "NONE"
                tagline = "NONE"
                rating = "NONE"
                releaseYear = -1
                if tryMatching:
                    if filmOrTV == "Film":
                        tmdbID = getTmdbIdForFilm(primaryTitle)
                    if tmdbID != "NONE":
                        dict_file.write(str(mediaID) + '|' + str(tmdbID) + '\n')
                        movie = tmdb.Movie(tmdbID)
                        country = getCountry(movie)
                        tagline = getTagline(movie)
                        releaseYear = str(movie.releasedate)
                        if not releaseYear:
                            releaseYear = -1
                        else:
                            releaseYear = releaseYear[:4]
                        if country != "NONE":
                            rating = getRating(movie)
                newRow = mediaID + delim + primaryTitle + delim + releaseYear + delim + country + delim + formatMedia + delim + filmOrTV + delim + titleSort + delim + rating + delim + str(tmdbID) + delim + tagline
                print newRow.decode('iso-8859-1').encode('utf8')
        except Exception as e:
            pass
    dict_file.close()