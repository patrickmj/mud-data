import csv
from urllib.parse import urlparse


with open('../data/mudf14q3pub.csv', newline='') as f:
    reader = csv.DictReader(f)
    columns = reader.fieldnames
    fixed = csv.DictWriter(open('../data/fixed.csv', 'w'), columns)
    for row in reader:
        print(row['MID'])
        url = row['WEBURL']
        if url:
            url = url.lower()
            if not url.startswith(('http://', 'https://')):
                url = 'http://' + url
            row['WEBURL'] = url
        fixed.writerow(row)
