import re
#https://github.com/MonaMohammadi-py/AIM-bootcamps-practices-regex.git

def youtube_link_changer(youtube_link: str) -> str:
    is_my_link_valid = re.search(r"(?:http|https)\://(?:www\.?)youtube\.com/embed/([0-9a-zA-z\-_]+)" , youtube_link)
    if is_my_link_valid:
        return f"https://youtu.be/{is_my_link_valid.group(1)}"

    return "None"



def main():
    youtube_link = input()
    new_link = youtube_link_changer(youtube_link)
    print(new_link)



if __name__ == "__main__":
    main()


