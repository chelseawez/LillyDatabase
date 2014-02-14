with open('Production.dat') as f:
   delim = '|'
   for line in f:
       mediaid = line.split('|')[0].strip()
       name = line.split('|')[1].strip()

       if (name[0:0] == '#'):
           name = name[1:].strip()

       match = name

       if (match.lower().startswith('a ')):
           match = match[1:].strip()
       elif (match.lower().startswith('an ')):
           match = match[2:].strip()
       elif (match.lower().startswith('the ')):
           match = match[3:].strip()

       if (match.lower().endswith(', the')):
           match = match[:-5]

       slash = match.find('/')
       while (slash != -1):
          match = match[:slash] + ' ' + match[slash+1:]
          slash = match.find('/')

       if (match.find('(') != -1 and match.find(')') != -1):
          match = match[match.find('(')+1:match.find(')')].strip()
       elif (match == 'Metro Goldwyn Mayer' or match == 'Metro-Goldwyn-Mayer'):
          match = 'MGM'
       elif (match == 'Warner Bros. Pictures' or match == 'Warner Bros Pictures'):
          match = 'Warner Bros.'
       elif ((match == 'Twentieth Century Fox Film Corporation') or (match == '20th Century Fox Home Entertainment') or (match == 'Twentieth Century-Fox Film Corporation') or (match == 'Twentieth Century-Fox')):
          match = '20th Century Fox'
       elif (match == 'Band Apart'):
          match = 'BandApart'
       elif (match.lower() == 'ajym films' or match.lower() == 'ajym-films'):
          match = 'Ajym Films'
          name = match
       elif (name.lower() == 'arena films'):
          match = 'Arena Films'
          name = match
       elif (match.lower() == 'arte france cinéma' or match.lower() == 'arte france cinema'):
          match = 'arte France Cinéma'
       elif (match.lower() == 'ashutosh gowariker productions pvt. ltd.'):
          match = 'Ashutosh Gowariker Productions'
       elif (match.lower() == 'bac films'):
          match = 'Bac Films'
       elif (match.lower().find('warner brothers') != -1):
          match = 'Warner Bros.' + match[15:]

       newRow = mediaid + delim + name + delim + match
       print newRow
