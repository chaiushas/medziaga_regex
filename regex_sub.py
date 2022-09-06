import re

card_number = "card1: 0452 6544 0004 4456, card2: 1234 4567 8910 1112"
pattern = re.compile(r'\b\d{4}\s\d{4}\s\d{4}\s(\d{4})\b')
res = pattern.sub('**** **** **** \g<1>', card_number)
print(res)