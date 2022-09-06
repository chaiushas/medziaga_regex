import re

text = '''Workshop & Tutorial proposals: November 21, 2019
Notification of acceptance: December 1, 2019
Workshop & Tutorial websites online: December 18, 2019
Workshop papers: February 28, 2020
Workshop paper notifications: March 27, 2020
Workshop paper camera-ready versions: April 10, 2020
Tutorial material due (online): April 10, 2020'''

def take_dates(text):
    pattern = re.compile(r'[A-Z]\w+\s\d+\,\s\d+')
    result = pattern.findall(text)
    return result

def print_event(text):
    pattern = re.compile(r'(.+)\:')
    result = pattern.findall(text)
    for i in range(len(result)):
        print(f'{i + 1}.\nEvent: {result[i]}\nDate: {take_dates(text)[i]}\n')

print_event(text)