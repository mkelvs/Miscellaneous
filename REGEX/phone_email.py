#! python3
# phone_email.py - This will find any phone numbers and email addresses on a certain file

import pyperclip, re

with open('names.txt', 'r') as file:
    filename = file.read()


def phoneExtractor(filename):
    phoneRegex = re.compile(r'''
(?P<phone>\(?\d{3}\)?\s?.?-?\d{3}\s?-?.?\d{4}) #Phone
''', re.X|re.M)

    list_phones = []
    for match in phoneRegex.finditer(filename):
        list_phones.append(match.group('phone'))

    print(list_phones)
    return list_phones

def emailExtractor(filename):
    emailRegex = re.compile(r'''
(?P<email>[-\w\d.+]+@[\w\d.-]+.[\w]+) #email
''', re.X|re.M)

    list_emails = []
    for match in emailRegex.finditer(filename):
        list_emails.append(match.group('email'))

    print(list_emails)
    return(list_emails)

phoneExtractor(filename)
emailExtractor(filename)