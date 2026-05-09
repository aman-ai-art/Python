# This file contains the main program for a currency converter. It imports the `Converters` module, which contains functions to convert between different currencies. The program prompts the user to enter an amount and choose a conversion type, then performs the conversion based on the user's choice and displays the result. Finally, it thanks the user for using the currency converter.
import Converters
print("Welcome to the currency converter!")
amount = float(input("Enter the amount you want to convert: "))
print("Choose the conversion type:")
print('''1. USD to NEP
2. NEP to USD  
3. NEP to INR  
4. INR to NEP''')
choice = int(input("Enter you choice (1-4): "))
if choice == 1:
    converted_amount = Converters.usd_to_nep(amount)
    print(f"{amount} USD is equal to {converted_amount} NEP.")
elif choice == 2:
    converted_amount = Converters.nep_to_usd(amount)
    print(f"{amount} NEP is equal to {converted_amount} USD.")
elif choice == 3:
    converted_amount = Converters.nep_to_inr(amount)
    print(f"{amount} NEP is equal to {converted_amount} INR.")
elif choice == 4:
    converted_amount = Converters.inr_to_nep(amount)
    print(f"{amount} INR is equal to {converted_amount} NEP.")
else:
    print("Invalid choice. Please select a valid conversion type.")

print("Thank you for using the currency converter!")