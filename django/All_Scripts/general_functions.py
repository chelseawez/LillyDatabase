# Returns a dictionary with all the media IDs in Lilly
# Key is TMDb id and value is media ID

def getDict():
    ins = open("Media.dat", "r")
    mediaDict = {}
    for line in ins:
        parts = line.split('|')
        if parts[0] != "NONE":
            mediaDict[parts[8]] = parts[0]
    ins.close()
    return mediaDict;
    
def getDict2():
    ins = open("Media.dat", "r")
    array = []
    for line in ins:
        array.append( line )
    ins.close()
    mediaDict = {}
    for line in array:
        parts = line.split('|')
        mediaDict[parts[0]] = True
    return mediaDict;