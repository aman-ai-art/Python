# This code implements a simple emoji converter that replaces certain text-based emoticons with their corresponding emoji characters. The user is prompted to enter a message, and the program outputs the message with the emoticons converted to emojis.
emoji = { ":)": "😀", ":(": "🙁", ":|": "😐", ":D": "😃", ":P": "😛", ":/": "😕" }
message = input("Enter your message: ")
words = message.split(" ")
output = ""
for word in words:
    output += emoji.get(word, word) + " "
print(output)