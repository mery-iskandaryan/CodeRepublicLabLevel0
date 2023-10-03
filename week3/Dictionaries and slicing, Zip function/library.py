library = {}
keys = ['Orwell', 'Fitzgerald', 'Kafka']
values = [['1984', 'english'], ['The great Gatsby', 'english'], ['The Castle', 'german']]

for i in range(len(keys)):
    library[keys[i]] = values[i]

for key in library:
    print(key, library[key])
