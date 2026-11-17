#https://github.com/MonaMohammadi-py/AIM-bootcamps-practices-regex.git
import re

def solve():
    text = input()    
    pattern = r"(\d{4}-\d{2}-\d{2})|(\d{2}/\d{2}/\d{4})"
    
    matches = re.finditer(pattern, text)
    
    for match in matches:         
        if match.group(1):
            print(match.group(1))

        date_str = match.group(2)
                
        if match.group(2):
            parts = date_str.split('/')
            print(f"{parts[2]}-{parts[1]}-{parts[0]}")

if __name__ == "__main__":
    solve()
