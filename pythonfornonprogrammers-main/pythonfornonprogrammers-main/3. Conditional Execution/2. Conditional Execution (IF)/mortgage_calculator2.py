print("=====  Mortgage Analysis using  While loop =======")
print("Welcome to Mortgage Calculator")
print("=" * 40)

# Multiple applicants using while loop
max_applicants = 3
applicant_count = 0

while applicant_count < max_applicants:
    applicant_count += 1
    print(f"\n--- Applicant {applicant_count} ---")
    
    name = input("Enter applicant name: ")
    salary = int(input("Enter annual salary: $"))
    credit_score = int(input("Enter credit score: "))
    
    # Nested if statements
    if salary >= 2000:
        if credit_score >= 700:
            status = "APPROVED - Preferred Rates"
        elif credit_score >= 650:
            status = "APPROVED - Standard Rates"
        else:
            status = "DENIED - Credit score too low"
    else:
        status = "DENIED - Income insufficient"
    
    print(f"Result for {name}: {status}")
    
    # Continue with more applicants?
    if applicant_count < max_applicants:
        continue_input = input("Add another applicant? (y/n): ").lower()
        if continue_input != 'y':
            break

print(f"\nProcessed {applicant_count} applicant(s)")