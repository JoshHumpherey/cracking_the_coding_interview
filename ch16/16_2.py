# Cracking the Coding Interview: 16.2
# Written by Josh Humphrey

def read_book(file_name):
    bad_chars = {',','.',';',':','"','\''}
    book_array = []
    with open(file_name,'r') as f:
        for line in f:
            for word in line.split():
                for special in bad_chars:
                    new_word = word.replace(special,"")
                book_array.append(new_word)

    return book_array

def analyze_book(book_arr):
    bookmap = dict()
    for word in book_arr:
        if word not in bookmap:
            bookmap[word] = 1
        else:
            bookmap[word] += 1
    return bookmap

shakespeare_arr = read_book('Shakespeare.txt')
result = analyze_book(shakespeare_arr)
print(result)
