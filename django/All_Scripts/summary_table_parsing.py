# This class relies on the Media table, thus, before generating an updated
# version of the Summary table, media_table_parsing.py must be executed first.

import csv
import tmdb
import general_functions as gen

tmdb.set_key("632e13506ef012eb41a058393cf20976")
    
def summaryIsReal(summary):
    summary = summary.lower()
    if(summary.find('no overview') > -1):
        return False
    return True
    
# mediaDict has key as TMDB ID and value as Lilly media ID
mediaDict = gen.getDict()
delim = '|'
for tmdbID in mediaDict:
    movie = tmdb.Movie(int(tmdbID))
    summary = movie.overview
    if summary:
        ct = summary.count("\"")
        if (ct%2 != 0):
            summary = summary.replace("\"", "")
        if summaryIsReal(summary):
            summary = summary.replace("<CR>", "").strip()
            newRow = str(int(mediaDict[tmdbID])) + delim + summary
            print newRow.encode('utf-8')