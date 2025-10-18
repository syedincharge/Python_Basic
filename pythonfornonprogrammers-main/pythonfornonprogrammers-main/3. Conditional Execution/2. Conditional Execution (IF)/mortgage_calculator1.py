print("=======   Mortgage Analysis using Control statements ========")
print("Welcome to Mortgage Calculator\n")
print("=" * 40)

salary = int(input("What is your salary? $\n"))
credit_score = int(input("What is your credit score? (300-850)\n"))
employment_years = int(input("How many years have you been employed? \n"))

# Tier system using if-elif-else
if salary >= 5000 and credit_score >= 750 and employment_years >= 2:
    print("🎉 Premium Tier: Eligible for up to $500,000 at 3.5% interest")
    print("  Benefits: Low down payment, no PMI required")
    
elif salary >= 3000 and credit_score >= 700 and employment_years >= 1:
    print("✅ Standard Tier: Eligible for up to $300,000 at 4.5% interest")
    print("  Benefits: Competitive rates, flexible terms")
    
elif salary >= 2000 and credit_score >= 650:
    print("⚠️  Basic Tier: Eligible for up to $150,000 at 5.5% interest")
    print("  Requirements: 20% down payment, PMI required")
    
else:
    print("❌ Not Eligible for Mortgage")
    if salary < 2000:
        print(f"  - Increase salary from ${salary} to at least $2000")
    if credit_score < 650:
        print(f"  - Improve credit score from {credit_score} to at least 650")
    if employment_years < 1 and salary >= 3000:
        print("  - Need at least 1 year of employment history")