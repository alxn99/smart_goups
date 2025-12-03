from input import get_name_email
from check_email import validate_email

nume, email = get_name_email()
print("nume")
print("email")
print(validate_email(email))