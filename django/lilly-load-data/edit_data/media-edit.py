with open('Media.dat') as f:
   delim = '|'
   for line in f:
       mediaid = line.split('|')[0]
       primary_title = line.split('|')[1]
       year = line.split('|')[2]
       country = line.split('|')[3]
       format = line.split('|')[4]
       film_or_tv = line.split('|')[5]
       title_sort = line.split('|')[6]
       rating = line.split('|')[7]
       tmdb_id = line.split('|')[8]
       tagline = line.split('|')[9].strip()

       if (primary_title.lower().strip().split()[0] == title_sort.lower()):
          primary_title = primary_title.split()[0].strip()

       if (tagline == ""):
          tagline = 'NONE'

       newRow = mediaid + delim + primary_title + delim + year + delim + country + delim + format + delim + film_or_tv + delim + title_sort + delim + rating + delim + tmdb_id + delim + tagline
       print newRow
