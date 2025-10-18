print("\n=== PRACTICAL APPLICATIONS ===")

# Password strength checker
def is_strong_password(password):
    return (len(password) >= 8 and 
            any(c.isupper() for c in password) and
            any(c.islower() for c in password) and
            any(c.isdigit() for c in password))

print(f"Strong password 'Pass1234': {is_strong_password('Pass1234')}")  # True
print(f"Strong password 'weak': {is_strong_password('weak')}")          # False

# Grade calculator
def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

print(f"Score 85 gets: {get_grade(85)}")  # B

# Number classification
def classify_number(n):
    is_positive = n > 0
    is_even = n % 2 == 0
    is_multiple_of_5 = n % 5 == 0
    
    return f"Positive: {is_positive}, Even: {is_even}, Multiple of 5: {is_multiple_of_5}"

print(f"Number 10: {classify_number(10)}")