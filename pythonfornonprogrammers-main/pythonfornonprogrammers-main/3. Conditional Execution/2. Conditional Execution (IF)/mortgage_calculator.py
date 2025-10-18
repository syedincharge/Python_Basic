print("======  Mortgage Analysis using  IF and Else  =======\n")

print("Welcome to Mortgage Calculator\n")

print("=" * 40)

# Basic eligibility check
salary = int(input("What is your salary? $\n"))
credit_score = int(input("What is your credit score? (300-850)\n"))
current_debt = float(input("What is your current total debt? $\n"))

if salary >= 2000 and credit_score >= 900 and current_debt < 10000:
    print("✓ You are eligible for mortgage!")
else:
    print("✗ Sorry, you are not eligible for mortgage!")
    if salary < 2000:
        print("  - Your salary is too low")
    if credit_score < 750:
        print("  - Your credit score is insufficient")
    if current_debt >= 10000:
        print("  - Your current debt is too high")