income = int(input('Enter your income: '))
credit = int(input('Enter your credit score: '))
loan_amount = int(input('Enter loan amount: '))
if income*12 + credit >= loan_amount:
    print('You are eligible for the loan.')
else:
    print('You are not eligible for the loan.')
print('Thank you for using our loan eligibility checker.')
print("Logical operators are 'and', 'or', 'not'")