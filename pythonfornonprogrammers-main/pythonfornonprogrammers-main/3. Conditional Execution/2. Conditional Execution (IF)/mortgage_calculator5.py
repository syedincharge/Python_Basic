print("===  Mortgage Analysis Decision with comprehensive matrix ===\n")
print("Welcome to Comprehensive Mortgage Advisor")
print("=" * 45)

# Multiple condition checks
salary = int(input("Annual salary: $"))
credit_score = int(input("Credit score: "))
employment = int(input("Years at current job: "))
down_payment = float(input("Down payment amount: $"))
home_price = float(input("Home price: $"))

print(f"\nMortgage Decision Matrix:")
print("-" * 30)

# Complex decision logic
if (salary >= 50000 and credit_score >= 750 and 
    employment >= 2 and down_payment >= home_price * 0.2):
    decision = "EXCELLENT - Lowest rates available"
    max_loan = salary * 5
    
elif (salary >= 40000 and credit_score >= 700 and 
      employment >= 1 and down_payment >= home_price * 0.1):
    decision = "GOOD - Competitive rates"
    max_loan = salary * 4.5
    
elif (salary >= 30000 and credit_score >= 650 and 
      employment >= 0.5):
    decision = "FAIR - Higher rates, conditions apply"
    max_loan = salary * 4
    
else:
    decision = "REVIEW NEEDED - Manual underwriting required"
    max_loan = 0

print(f"Decision: {decision}")
if max_loan > 0:
    print(f"Maximum recommended loan: ${max_loan:,.0f}")
    
    # Final approval check
    requested_loan = home_price - down_payment
    if requested_loan <= max_loan:
        print("✓ Loan amount is within approved limits")
    else:
        print(f"⚠️  Loan amount (${requested_loan:,.0f}) exceeds recommended maximum")