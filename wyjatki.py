log = open("logi.txt").readlines()

def too_long(linia):
    if not len(linia)>173:
        raise AssertionError("Zbyt dlugi log")
    return linia


for i in range(len(log)):

    try:
        #nasz caly kod, ktory ma byc niezawodny
        print(too_long(log[i]))
    except Exception as e:
        #czynnosci, ktore wykonujemy w razie awarii
        print(e)