from pathlib import Path
import os
import csv
File = "C:\\Users\\JDam\\Desktop\\testtask\\result.xls"
p = Path("C:\\Users\\JDam\\Desktop\\testtask")
isfile = os.path.isfile
join = os.path.join

directory = 'mydirpath'
number_of_files = sum(1 for item in os.listdir(p) if isfile(join(p, item)))

def counter():
    i = 1
    while (i <= number_of_files):
        yield i
        i += 1

def get_content():
    files = []
    for x in p.rglob("*"):
        if os.path.isfile(x):
            files.append({
                'ID': [i for i in counter()],
                'path': (x),
                'name': (x.name),
                'extension': (x.suffix)
            })
    return files

def save_file(p, path):
    with open(path, 'w+', encoding='utf8', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(['Number', 'File path', 'File name', 'File extension'])
        for item in p:
            writer.writerow([item['ID'], item['path'], item['name'], item['extension']])

def start():
    save_file(get_content(), File)
    os.startfile(File)

start()