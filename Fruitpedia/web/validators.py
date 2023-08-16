from django.core.exceptions import ValidationError


def validate_name_starts_with_letter(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")


def validate_fruit_name_letters_only(value):
    if not value.isalpha():
        raise ValidationError("Fruit name should contain only letters!")
