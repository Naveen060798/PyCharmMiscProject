def strong_pass(password):
    msg='Password must contain at least'
    if len(password) < 8:
        return False, msg + "8 characters"

    has_upper=any(c.isupper() for c in password)
    has_lower=any(c.islower() for c in password)
    has_number=any(c.isdigit() for c in password)
    special_chars=set("!@#$%^&*-_+=")
    has_special=any(c in special_chars for c in password)

    if not has_upper:
        return False, msg + "one uppercase letter."
    if not has_lower:
        return False, msg + "one lowercase letter."
    if not has_number:
        return False, msg + "one number."
    if not has_special:
        return False, msg + "one special character."

    return True, "Password strong"

password=input("Enter your password: ")
valid,message=strong_pass(password)
print(message)





