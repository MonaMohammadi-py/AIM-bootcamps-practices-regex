#https://github.com/MonaMohammadi-py/AIM-bootcamps-practices-regex.git
import re

def pattern_finder(text: str) -> list:
    pattern = r"(?<!\d)(\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4})(?!\d)"
    
    matches = list(re.finditer(pattern, text))
    
    if not matches:
        print("None")
        return

    return matches


def new_date(matches: list):
    extracted_dates = []
    for match in matches:
        date_str = match.group()
        if "-" in match:
            y, m, d = map(int, date_str.split("-"))
        else:
            d, m, y = map(int, date_str.split("/"))
        if (1 <= y <= 9999) and (1 <= m <= 12) and (1 <= d <= 31):
            formatted_date = f"{y:04d}-{m:02d}-{d:02d}"
            extracted_dates.append(formatted_date)
        else:
            return extracted_dates

    return extracted_dates



def main():    
    text = input()
    matches = pattern_finder(text)
    dates = new_date(matches)

    if not dates:
        print("None")
    else:
        for date in dates:
            print(date)



if __name__ == "__main__":
    main()
