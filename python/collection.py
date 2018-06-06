cats = {
"Sir Squish": 1877,
"Madame FuzzyWig": 1900,
"Lord Marcus P. Toebeans": 1932,
"Madame Zelda": 1844,
}
def organize_kitties(dicts):
    counter19 = 0
    counter20 = 0
    for name, year in dicts.items():
        if year >=1900:
            counter19+=1
        elif year <1900:
            counter20+=1
    print("There are " + str(counter19) + " 19th century cats and " + str(counter20) + " 20th century cats.")

organize_kitties(cats)
