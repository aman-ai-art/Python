# This code demonstrates how to create formatted strings in Python using both string concatenation and f-strings. It constructs a full name from individual name components and creates personalized messages using the formatted strings.
first = 'Aman'
middle = 'Kumar'
last = 'Singh'
full_name = first + ' ' + middle + ' ' + last
print(full_name)
message = f'Hello, {first}. How are you?'
msg = f'[{full_name}] is a computer engineer.'
print(message)
print(msg)