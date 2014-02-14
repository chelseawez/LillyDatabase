# This class relies on the Media table, thus, before generating an updated
# version of the Production table, media_table_parsing.py must be executed first.

import csv
import tmdb
import general_functions as gen

tmdb.set_key("632e13506ef012eb41a058393cf20976")
    
# mediaDict has key as TMDB ID and value as Lilly media ID
mediaDict = gen.getDict()
delim = '|'
for tmdbID in mediaDict:
    movie = tmdb.Movie(int(tmdbID))
    for s in movie.studios:
        name = s.name.replace("\"", "")
        newRow = str(int(mediaDict[tmdbID])) + delim + name
        print newRow.encode('utf-8')