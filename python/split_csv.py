
import csv

def is_header(p):
    return (p[0] == 'time')

clean_file = "../data/clean.csv"

reader = csv.reader(open(clean_file ),delimiter=';')
filtered = filter(lambda p: ('_F' not in p[10]) | is_header(p), reader)
csv.writer(open(r"../data/clean_filtered.csv",'w'),delimiter=';').writerows(filtered)

# time filtering example
clean_file = "../data/clean_filtered.csv"

reader = csv.reader(open(clean_file ),delimiter=';')
filtered = filter(lambda p: ('2023-03-15T08:40:07.1943265Z' <= p[0] <= '2023-03-15T09:03:17.0056279Z') | is_header(p) , reader)
csv.writer(open(r"../data/time_filtered.csv",'w'),delimiter=';').writerows(filtered)

reader = csv.reader(open(clean_file ),delimiter=';')
filtered = filter(lambda p: ((p[1] >= '13') & ('_Val' in p[10])) | is_header(p)  , reader)
csv.writer(open(r"../data/clean13+.csv",'w'),delimiter=';').writerows(filtered)

reader = csv.reader(open(clean_file ),delimiter=';')
filtered = filter(lambda p: ('neue Zahn-Winkellage' in p[10]) | is_header(p), reader)
csv.writer(open(r"../data/winkellage.csv",'w'),delimiter=';').writerows(filtered)

reader = csv.reader(open(clean_file ),delimiter=';')
filtered = filter(lambda p: ('4.0' == p[9]) | is_header(p), reader)
csv.writer(open(r"../data/teammessung.csv",'w'),delimiter=';').writerows(filtered)

clean_file = "../data/clean1-12.csv"
reader = csv.reader(open(clean_file ),delimiter=';')
filtered = filter(lambda p: ('_F' not in p[10]) | is_header(p), reader)
csv.writer(open(r"../data/clean1-12_filtered.csv",'w'),delimiter=';').writerows(filtered)





