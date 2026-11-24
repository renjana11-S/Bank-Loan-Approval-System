# Rule-based Bank Loan Approval System
# Uses CIBIL Score and Income to decide loan approval

def evaluate_loan(cibil_score, annual_income):
    # Rule 1: Low eligibility -> REJECT
    if annual_income < 300000 or cibil_score < 500:
        return "REJECT - The applicant does not satisfy all major financial requirements."
    # Rule 2: High eligibility -> APPROVED
    elif cibil_score > 700 and annual_income > 500000:
        return "APPROVED - The applicant satisfies all major financial requirements."
    # Rule 3: Moderate eligibility -> VERIFICATION
    else:
        return "The application requires further verification before final Approval."

def main():
    print("="*55)
    print(" BANK LOAN APPROVAL SYSTEM")
    print("="*55)

    name = input("\nEnter Applicant Name: ")

    while True:
        try:
            cibil_score = int(input("Enter Credit Score (300-900): "))
            if 300 <= cibil_score <= 900:
                break
            else:
                print("Please enter a valid credit score.")
        except ValueError:
            print("Invalid input. Enter numbers only.")

    while True:
        try:
            annual_income = float(input("Enter Annual Income: "))
            if annual_income >= 0:
                break
            else:
                print("Income cannot be negative.")
        except ValueError:
            print("Invalid input. Enter numbers only.")

    while True:
        try:
            loan_amount = float(input("Enter Loan Amount Required: "))
            if loan_amount >= 0:
                break
            else:
                print("Loan amount cannot be negative.")
        except ValueError:
            print("Invalid input. Enter numbers only.")

    print("\nProcessing application...")
    print("-"*50)

    decision = evaluate_loan(cibil_score, annual_income)

    print(f"\nApplicant Name : {name}")
    print(f"Credit Score : {cibil_score}")
    print(f"Annual Income : {annual_income}")
    print(f"Loan Amount : {loan_amount}")
    print("\nDecision:")
    print(decision)
    print("\nThank you for using the Loan Approval System.")

if __name__ == "__main__":
    main()
