from rest_framework.serializers import ValidationError
import re

def validator_username(username:str):
    if len(username)<3:
        raise ValidationError("Username precisa de no minimo 4 caracteres")
    return username

def validator_email(email:str):
    email_regex = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        raise ValidationError("O email não esta num formato valido")
    return email