from django.core.exceptions import ValidationError



def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s is not an even number',
            params={"value": value},
        )

def validate_email(value):
    email = value
    if ".edu" in email:
        raise ValidationError("We do no accept edu emails")


CATEGORY = ['Mexican', 'Asian' , 'American' , 'Italian','Indian','Chinese','Chinese',
            'Japanese','Middle Eastern','Seafood','Thai'],
def validate_category(value):
    cat = value.capitalize()
    if not value in CATEGORY and not cat in CATEGORY:
        raise ValidationError(f"{value} not a valid category")
    value = cat
