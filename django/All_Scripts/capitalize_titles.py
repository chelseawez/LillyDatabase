import string

def checkForDash(word):
    if word.find('-') > -1:
        parts = word.split('-')
        return parts[0] + '-' + parts[1].capitalize()
    else:
        return word
        
def capitalize(word):
    if len(word) < 2:
        return word.capitalize()
    else:
        return word[0].upper() + word[1:]
    

media_file = open("Media.dat", "r")
no_caps = ['a', 'an', 'to', 'the', 'for', 'and', 'nor', 'but', 'or', 'yet', 'so', 'at', 'around', 'by', 'after', 'along', 'from', 'of', 'on', 'with', 'without', 'in']
for line in media_file:
    fields = line.split('|')
    title = fields[1]
    words = title.split(' ')
    updated_title = checkForDash(capitalize(words[0])) + ' '
    if updated_title[0] in string.punctuation:
        updated_title = updated_title[:1] + updated_title[1:].capitalize()
    for i in range(1, len(words)-1):
        word = words[i]
        if word not in no_caps:
            word = capitalize(word)
            word = checkForDash(word)
        updated_title += word + ' '
    last_word = words[len(words)-1]
    updated_title += checkForDash(capitalize(words[len(words)-1]))
    fields[1] = updated_title
    new_line = "|".join(fields)
    print new_line,
media_file.close()