import re
from datetime import datetime as dt


# UI ELEMENTS
# TODO do I need them?
def validate_int_params(account_number, account_pin_code):
    if isinstance(account_number, int) and isinstance(account_pin_code, int):
        return True
    return False


def validate_float_params(amount):
    if isinstance(amount, float):
        return True
    else:
        raise ValueError("Invalid input. Amount should be float.")


def validate_params(account_holder_name, account_email, account_address, account_phone_number,
                    account_birth_date):
    if (isinstance(account_holder_name, str) and isinstance(account_address, str)
            and is_valid_email(account_email) and isinstance(account_birth_date, dt)
            and is_valid_phone_number(account_phone_number)):
        return True
    return False


# TODO complete the function

def is_valid_email(email):
    """ Checks if email is a valid email.
        Args:
            email: A string representing an email account.
        Returns:
            True if the email is valid , False otherwise.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Use re.match to check if the email matches the pattern
    match = re.match(pattern, email)
    if match is not None:
        return email
    return False


def is_valid_phone_number(phone_number):
    """ Checks if a phone number is a valid mobile phone number.
        Args:
            phone_number: A string representing a phone number.
        Returns:
            True if the phone number is a valid mobile phone number, False otherwise.
    """
    pattern = r'^\+?[1-9]\d{9,14}$'

    # Use re.match to check if the phone_number matches the pattern
    match = re.match(pattern, phone_number)
    if match is not None:
        return phone_number
    return False


def is_valid_birth_date(birthdate):
    try:
        birth_date = dt.strptime(birthdate, '%Y-%m-%d')
        current_date = dt.now()

        # Additional validation to check if the birthdate is within a reasonable range
        if birth_date > current_date or birth_date.year < 1900:
            print("Invalid birth date. Please enter a realistic birth date.")
        else:
            return birth_date

    except ValueError:
        print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")
        return False


def get_prompt_from_user(prompt, prompt_type):
    try:
        if prompt_type == 0:
            validate_input = int(input(prompt))
        elif prompt_type == 1:
            validate_input = float(input(prompt))
        elif prompt_type == 2:
            validate_input = str(input(prompt))
        elif prompt_type == 3:
            validate_input = is_valid_phone_number(input(prompt))
        elif prompt_type == 4:
            validate_input = is_valid_email(input(prompt))
        elif prompt_type == 5:
            validate_input = is_valid_birth_date(input(prompt))
    except ValueError:
        print("This is not a Valid input")
        return None
    else:
        return validate_input


def get_a_prompt_loop(prompt, prompt_type):
    validate_input_to_get = None
    while not validate_input_to_get:
        validate_input_to_get = get_prompt_from_user(prompt, prompt_type)
    return validate_input_to_get

