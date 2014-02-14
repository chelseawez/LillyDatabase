# This class relies on the Media table, thus, before generating an updated
# version of the Poster table, media_table_parsing.py must be executed first.

import csv
import tmdb
import general_functions as gen

tmdb.set_key('632e13506ef012eb41a058393cf20976')
    
# mediaDict has key as TMDB ID and value as Lilly media ID
# Store a table of media IDs and the absolute URL to the poster image
base_URL = tmdb.Configuration.images['base_url']
image_size = tmdb.Configuration.images['poster_sizes'][3] + '/'
mediaDict = gen.getDict()
delim = '|'
for tmdbID in mediaDict:
    poster = tmdb.Movie(int(tmdbID)).poster
    if poster:
        newRow = str(int(mediaDict[tmdbID])) + delim + base_URL + image_size + poster.filename
        print newRow.encode('utf-8')