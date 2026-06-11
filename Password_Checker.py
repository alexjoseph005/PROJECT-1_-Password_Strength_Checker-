import string
import hmac
import gc


common_passwords = {
    "123456", "password", "admin", "qwerty", "welcome", "abc123", "DecodeLab@123"
}

raw_input = input("Enter password: ")


if len(raw_input) < 8:
    print("\n FAIL: Password is too short.")
    print("Reason: Passwords under 8 characters face exponential brute force risks.")
    strength = "Weak"


elif raw_input.lower() in common_passwords:
    print("\n FAIL: Extremely weak password.")
    print("Reason: This is a known leaked or common dictionary word.")
    strength = "Weak"

else:
    
    has_digit = any(char.isdigit() for char in raw_input)
    has_upper = any(char.isupper() for char in raw_input)
    has_lower = any(char.islower() for char in raw_input)
    has_symbol = any(char in string.punctuation for char in raw_input)


    score = 1 + sum([has_digit, has_upper, has_lower, has_symbol])

    
    if score == 5:
        strength = "Strong"
        print(f"\n PASS: Password strength is {strength}.")
    elif score >= 3:
        strength = "Medium"
        print(f"\n WARNING: Password strength is {strength}. Consider adding more character variety.")
    else:
        strength = "Weak"
        print(f"\n FAIL: Password strength is {strength}. It lacks structural complexity.")





official_password = "CodeDecode@43567"


if hmac.compare_digest(raw_input, official_password):
    print("\n[SECURITY]: Official password identity confirmed.")
else:
    print("\n[SECURITY]: Official password mismatch.")






del raw_input
gc.collect()