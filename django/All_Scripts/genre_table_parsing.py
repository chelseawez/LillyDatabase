# This class relies on the Media table, thus, before generating an updated
# version of the Genre table, media_table_parsing.py must be executed first.

import csv
import tmdb
import general_functions as gen

tmdb.set_key("632e13506ef012eb41a058393cf20976")
    
#mediaDict has key as tmdb id and value as Lilly media id
mediaDict = gen.getDict()
delim = '|'
for tmdbID in mediaDict:
    movie = tmdb.Movie(int(tmdbID))
    for g in movie.genres:
        newRow = str(int(mediaDict[tmdbID])) + delim + g.name
        print newRow.encode('utf-8')