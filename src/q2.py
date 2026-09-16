"""HW1 Question 2

Please implement the following function according to the provided documentation.
Tests are provided for this question in the file tests/test_q2.py."""

def validate_password(password: str) -> bool:
    """Determines whether a password meets the requirements.

    Requirements:
    1. Password must be at least 8 characters long
    2. Password must contain at least one uppercase letter
    3. Password must contain at least one lowercase letter
    4. Password must contain at least one digit
    5. Password must contain at least one special character (!@#$%^&*)

    
    Parameters
    ----------
    password : str
        The password to validate
    
    Returns
    -------
    bool
        True if the password is valid, and false otherwise
    """

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    # loop through each character and check what it is

    for c in password:
        if c.isupper():
            has_upper = True
        if c.islower():
            has_lower = True
        if c.isdigit():
            has_digit = True

         # this part checks if character is one of the required special characters
        if c in "!@#$%^&*":
            has_special = True

    # check all requirements and return False if any are not met
    if len(password) < 8:
        return False
    if not has_upper:
        return False
    if not has_lower:
        return False
    if not has_digit:
        return False
    if not has_special:
        return False
    return True


    