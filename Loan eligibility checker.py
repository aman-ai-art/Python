# This code checks the eligibility of a user for a loan based on their income, credit score, and the desired loan amount. It calculates the total eligibility by combining the user's annual income and credit score, and then compares it to the requested loan amount to determine if the user is eligible, conditionally eligible, or not eligible for the loan. Finally, it thanks the user for using the loan eligibility checker.
income = int(input('Enter your income: '))
credit = int(input('Enter your credit score: '))
loan_amount = int(input('Enter loan amount: '))
if income*12 + credit >= loan_amount:
    print('You are eligible for the loan.')
elif income*12 + credit == loan_amount:
    print('You are conditionally eligible for the loan.')
else:
    print('You are not eligible for the loan.')
print('Thank you for using our loan eligibility checker.')