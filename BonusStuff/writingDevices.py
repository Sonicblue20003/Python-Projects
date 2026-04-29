contents = ["I am some stuff", "I am more stuff", "Who am I"]
filenames = ["doc.txt", "reportd.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f'../files/{filename}', 'w')
    file.write(content)

    filenames = ['file.txt']
    contents = ['snail']
    for content, filename in zip(contents, filenames):
        file = open(filename, 'w')
        file.write(content)
        file.close

        countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]
        filenames = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']

        for country, filename in zip(countries, filenames):
            file = open(filename, 'w')
            file.write(country)

