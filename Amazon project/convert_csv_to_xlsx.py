import csv
from openpyxl import Workbook
import os

csv_file = 'test_cases.csv'
xlsx_file = 'test_cases.xlsx'

if not os.path.exists(csv_file):
    print(f'CSV not found: {csv_file}')
    raise SystemExit(1)

wb = Workbook()
ws = wb.active

with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        ws.append(row)

wb.save(xlsx_file)
print('Saved', xlsx_file)
