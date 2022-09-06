import re

# re.IGNORECASE arba re.I - padaro jūsų užklausą case insensitive. t.y. nekreipia dėmesio, į didžiąsias - mažąsias raides.
# re.MULTILINE arba re.M - elgiasi su jūsų tekstu kaip su daug eilučių turinčia struktūra, o ne žiūri kaip į vieną eilutę.
# *re.VERBOSE arba re.X - leidžia jums suformuoti regex užklausą per kelias eilutes su komentarais. Prideda užklausoms skaitomumo.

# re.IGNORECASE, re.I
tekstas = '''Trumpas tekstas 
apie beleką'''
pattern = re.compile(r't\w+', re.I)
res = pattern.findall(tekstas)
print(res)

# re.MULTILINE, re.M
tekstas = '''Trumpas tekstas 
apie beleką'''

pattern = re.compile(r'^\w+')
res = pattern.findall(tekstas)

pattern2 = re.compile(r'^\w+', re.M)
res2 = pattern2.findall(tekstas)

print(res)
print(res2)

# re.VERBOSE, re.X
tekstas = 'Jonas Jonaitis +370 622 01234'
pattern = re.compile(r'''
                    [A-Z]\w+              # vardas
                    \s                    # tarpas
                    [a-z]\w+              # pavardė
                    \s                    # tarpas
                    \+370\s6\d{2}\s\d{5}  # telefono numeris
                    ''', re.X | re.I)
res = pattern.findall(tekstas)
print(res)
