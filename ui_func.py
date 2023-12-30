import re
from datetime import datetime as dt


def validate_int_params(account_number, account_pin_code):
    if isinstance(account_number, int) and isinstance(account_pin_code, int):
        return True
    return False


def validate_params(account_holder_name, account_email, account_address, account_phone_number,
                    account_birth_date):
    if (isinstance(account_holder_name, str) and isinstance(account_address, str)
            and is_valid_email(account_email) and is_valid_birth_date(account_birth_date)
            and is_valid_phone_number(account_phone_number)):
        return True
    return False


def is_valid_email(email):
    """ Checks if email is a valid email.
        Args:
            email: A string representing an email account.
        Returns:
            True if the email is valid , False otherwise.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Use re.match to check if the email matches the pattern
    try:
        # Use re.match to check if the phone_number matches the pattern
        match = re.match(pattern, email)
        if match is not None:
            return email
        else:
            raise ValueError("Invalid email format. Please enter a valid email account.")
    except ValueError as ve:
        # Handle any other ValueError raised in the try block
        print(ve)
        return False


def is_valid_phone_number(phone_number):
    """ Checks if a phone number is a valid mobile phone number.
        Args:
            phone_number: A string representing a phone number.
        Returns:
            True if the phone number is a valid mobile phone number, False otherwise.
    """

    pattern = r'^05\d{8}$'

    # Use re.match to check if the phone_number matches the pattern

    try:
        # Use re.match to check if the phone_number matches the pattern
        match = re.match(pattern, phone_number)
        if match is not None:
            return phone_number
        else:
            raise ValueError("Invalid phone number format. Please enter a phone number starts with '05'.")
    except ValueError as ve:
        # Handle any other ValueError raised in the try block
        print(ve)
        return False


def is_valid_birth_date(birthdate):
    try:
        birth_date = dt.strptime(birthdate, '%Y-%m-%d')
        current_date = dt.now()

        # Additional validation to check if the birthdate is within a reasonable range
        if birth_date > current_date or birth_date.year < 1900 or birth_date.year > (current_date.year - 17):
            print("Invalid birth date. Please enter a realistic birth date.")
            return False
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
        if not validate_input_to_get and prompt_type in (0, 1, 2):
            print("Invalid input. Please try again")
    return validate_input_to_get
