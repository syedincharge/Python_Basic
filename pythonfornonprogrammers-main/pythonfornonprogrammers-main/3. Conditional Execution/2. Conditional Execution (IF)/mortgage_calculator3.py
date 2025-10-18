print("========  Mortgage Analysis using For Loop ========= ")
print("Welcome to Advanced Mortgage Calculator")
print("=" * 45)

# Property price ranges
property_prices = [150000, 300000, 500000, 750000]
down_payment_percent = 20

salary = int(input("Enter your annual salary: $"))
credit_score = int(input("Enter your credit score: "))

print(f"\nProperty Affordability Analysis:")
print("-" * 35)

# For loop through different property prices
for price in property_prices:
    down_payment = price * (down_payment_percent / 100)
    loan_amount = price - down_payment
    
    # Complex condition checking
    if salary >= 50000 and credit_score >= 750 and price <= 500000:
        approval_status = "✅ APPROVED - Best Rates"
    elif salary >= 40000 and credit_score >= 700 and price <= 400000:
        approval_status = "✅ APPROVED - Good Rates"
    elif salary >= 30000 and credit_score >= 650 and price <= 300000:
        approval_status = "⚠️  CONDITIONAL APPROVAL"
    else:
        approval_status = "❌ NOT APPROVED"
    
    print(f"${price:,}: Down Payment ${down_payment:,.0f} | {approval_status}")