import re


def check_phone(string):
    phone = re.sub(r"\b\D", '', string)
    clear_phone = re.sub(r'[ \(]?', '', phone)
    if not re.findall(r'^[+7|8]*?\d{10}$', clear_phone) and not re.match(r'^\w+[.]?(\w+)*@(\w+\.)*\w{2,}$', string):
        return (False)
    else:
        return (bool(string))

