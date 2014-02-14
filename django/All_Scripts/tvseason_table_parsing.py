import csv
import general_functions as gen

num_th = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth", "thirteenth", "fourteenth", "sixteenth", "seventeenth", "eighteenth", "nineteenth", "twentieth"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
num_spell = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]

def getSeason(title):
    for i in num_th:
        if (title.lower().find(('the complete ' + i + ' season')) != -1):
            return str(int(num_th.index(i))+1)
    for i in numbers:
        if (title.lower().find(('season ' + i)) != -1):
            return str(int(numbers.index(i))+1)
    for i in num_spell:
        if (title.lower().find(('season ' + i)) != -1):
            return str(int(num_spell.index(i))+1)
    return None

with open('Lilly DVD Assets.csv', 'rb') as f:
    reader = csv.DictReader(f)
    delim = '|'
    # Key is TMDB id and value is media ID
    mediaDict = gen.getDict2()
    for row in reader:
        processStatus = row["Process Status Desc"]
        material = row["Material Type Desc"]
        itemID = row["Barcode"]
        mediaID = row["Bib Doc Number"]
        if (itemID[:1] == 'D' and (processStatus != "Withdrawn" and processStatus != "Suppressed" and processStatus != "Canceled") and (material == "Video Cassette" or material == "DVD") and mediaID in mediaDict):
            season = getSeason(row["Desc8"])
            if (season != None):
                 newRow = mediaID + delim + season
                 print newRow.encode('utf-8')