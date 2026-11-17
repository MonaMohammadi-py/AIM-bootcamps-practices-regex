import re
#https://github.com/MonaMohammadi-py/AIM-bootcamps-practices-regex.git


def valid_ip(ip_address: str) -> bool:
    ip_validation = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip_address)

    if ip_validation:
        groups = ip_validation.groups()
        for group in groups:
            group_int = int(group)
            if not (0 <= group_int <= 255):
                return False
                
        return True
    else:
        return False



def main():
    ip_address = input()
    ip_address_valuation = valid_ip(ip_address)
    
    if ip_address_valuation:
        print("Valid IP")
    else:
        print("Invalid IP")


if __name__ == "__main__":
    main()
