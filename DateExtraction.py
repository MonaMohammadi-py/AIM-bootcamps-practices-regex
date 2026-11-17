#https://github.com/MonaMohammadi-py/AIM-bootcamps-practices-regex.git
import re

def date_changer(raw_date):
    update_date1 = re.findall(r"\d{4}-\d{2}-\d{2})" , raw_date)
    update_date2 = re.findall(r"\d{2}/\d{2}/\d{4}" , raw_date)

    if update_date1:
        year = update_date1[0]
        month = update_date1[1]
        day = update_date1[2]
        return f"{year}-{month}-{day}"

    if update_date2:
        year = update_date1[2]
        month = update_date1[1]
        day = update_date1[0]
        return f"{year}-{month}-{day}"


def main():
    rew_date = input()
    print(date_changer)




if __name__ == "__main__":
    main()

