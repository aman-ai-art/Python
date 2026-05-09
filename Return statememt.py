# This code defines a function called converter that takes a message as input and converts certain text-based emoticons into their corresponding emoji characters. It uses a dictionary to map emoticons to emojis and processes the input message by splitting it into words, replacing any recognized emoticons with their emoji equivalents, and then joining the words back together to produce the final output. The user is prompted to enter a message, which is then passed to the converter function, and the resulting string with emojis is printed.
emoji = { ":)": "😀", ":(": "🙁", ":|": "😐", ":D": "😃", ":P": "😛", ":/": "😕" }
def converter(message):
    words = message.split(" ")
    output = ""
    for word in words:
        output += emoji.get(word, word) + " "
    return output


message = input("Enter your message: ")
result = converter(message)
print(result)
