import re

def split_names(name):
    pattern = re.compile(r'^([A-Z]\w{1,3}\.)\s([A-Z]\w+)\s([A-Z]\w+)$')
    result = pattern.search(name)
    if result:
        print(f'Visa eilutė: {result.group(0)}')
        print(f'Kreipinys: {result.group(1)}')
        print(f'Vardas: {result.group(2)}')
        print(f'Pavardė: {result.group(3)}')
        print('----------------------------------')
        print(result.group())
        print(result.groups()) #tuple
    else:
        print('Įvestis neatitinka šablono')

split_names('Mr. Clint Eastwood')

# pattern = re.compile(r'^(?P<kreipinys>[A-Z]\w{1,3}\.)\s([A-Z]\w+)\s([A-Z]\w+)$')
# print(f'Kreipinys: {result.group("kreipinys")}')