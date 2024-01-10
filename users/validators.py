from rest_framework.serializers import ValidationError
import re


def validator_username(username: str):
    if len(username) < 3:
        raise ValidationError("Username precisa de no minimo 4 caracteres")
    return username


def validator_email(email: str):
    email_regex = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(email_regex, email):
        raise ValidationError("O email não esta num formato valido")
    return email


def validator_password(password):
    if not re.search(r"[A-Z]", password):
        raise ValidationError("A senha precisa ter pelo menos uma letra maiuscula")

    if not re.search(r"[a-z]", password):
        raise ValidationError("A senha precisa ter pelo menos uma letra minuscula")

    if not re.search(r"\d", password):
        raise ValidationError("A senha precisa ter pelo menos um numero")

    if not re.search(r"[!@#$%^&*(),.?:{}|<>]", password):
        raise ValidationError("A senha deve conter carcateres especiais")

    if len(password) < 8:
        raise ValidationError("A senha deve ter no minimo 8 caracteres")

    return password
