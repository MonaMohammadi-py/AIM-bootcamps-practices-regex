#https://github.com/MonaMohammadi-py/AIM-bootcamps-practices-regex.git
import re

text = input()

matches = list(re.finditer(r"(?<!\d)(\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4})(?!\d)", text))

extracted_dates = []

for match in matches:
    date_str = match.group()
    
    if "-" in date_str:
        y, m, d = map(int, date_str.split("-"))
    else:
        d, m, y = map(int, date_str.split("/"))
        
    if 1 <= y <= 9999 and 1 <= m <= 12 and 1 <= d <= 31:
        formatted_date = f"{y:04d}-{m:02d}-{d:02d}"
        extracted_dates.append(formatted_date)

if not extracted_dates:
    print("None")
else:
    for date in extracted_dates:
        print(date)
