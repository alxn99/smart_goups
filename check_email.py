import re

def validate_email(nume_mail):
    pattern = r'^[a-z]+(\.[a-z]+)+@[a-z0-9-]+(\.[a-z0-9-]+)+$'
    return bool(re.fullmatch(pattern, nume_mail))