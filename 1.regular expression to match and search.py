import re

# Example text
text = "Hello, my email addresses are john@example.com and jane123@gmail.com. Feel free to contact me."

# Pattern to match email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# Using re.findall() to find all email addresses in the text
matches = re.findall(email_pattern, text)

# Printing the matches
print("Email Addresses found:")
for match in matches:
    print(match)
