print("==========  Mortagage Analysis using Break and Continue =============\n")
print("Welcome to Mortgage Pre-Qualification")
print("=" * 40)

while True:
    print("\n1. Check Eligibility")
    print("2. Calculate Monthly Payment")
    print("3. Exit")
    
    choice = input("Choose an option (1-3): ")
    
    if choice == '1':
        # Eligibility check
        salary = int(input("Enter annual salary: $"))
        credit_score = int(input("Enter credit score: "))
        debt = float(input("Enter monthly debt payments: $"))
        
        debt_to_income = (debt * 12) / salary if salary > 0 else 1
        
        if salary >= 30000 and credit_score >= 680 and debt_to_income <= 0.43:
            print("✓ PRE-QUALIFIED! You can proceed with full application.")
        else:
            print("✗ Not pre-qualified at this time.")
            continue  # Skip to next iteration without calculating payment
            
        # Only calculate if pre-qualified
        home_price = int(input("Enter desired home price: $"))
        if home_price <= salary * 4:  # 4x salary rule
            print(f"✓ Home price ${home_price:,} is within recommended range")
        else:
            print(f"⚠️  Home price may be too high (recommended: <= ${salary * 4:,})")
            
    elif choice == '2':
        # Payment calculator
        loan_amount = int(input("Enter loan amount: $"))
        interest_rate = float(input("Enter annual interest rate (%): "))
        loan_term = int(input("Enter loan term (years): "))
        
        monthly_rate = interest_rate / 100 / 12
        months = loan_term * 12
        monthly_payment = loan_amount * monthly_rate * (1 + monthly_rate)**months / ((1 + monthly_rate)**months - 1)
        
        print(f"Estimated monthly payment: ${monthly_payment:,.2f}")
        
    elif choice == '3':
        print("Thank you for using Mortgage Calculator!")
        break  # Exit the loop
        
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
        continue  # Skip invalid input