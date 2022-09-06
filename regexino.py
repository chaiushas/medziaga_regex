import re

pattern = re.compile(r'\+370\s\d{3}\s\d{5}')
tekstas = '''Pirmas telefono numeris yra +370 123 12321, antras +370 321 10101.'''
res = pattern.search(tekstas) # randa pirma reiksme, jeigu neranda igauna None reiksme
print(res) # reiksme <re.Match object; span=(28, 42), match='+370 123 12321'>
print(res.group())# reiksme +370 123 12321
res = pattern.findall(tekstas) # paduoda masyva ir suranda visas reiksmes
print(res)

def validate_email(input):
    email_regex = re.compile(r'^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$')
    result = email_regex.search(input)
    if result: #jeigu yra kazkas "result", tai result = True, jeigu nieko nera, False
        return True
    return False

print(validate_email('kazkoks@email.lt'))
print(validate_email('neteisingas@@email.lt'))

# \d skaičius
# \D neskaičius
# \s tuščias tarpas (whitespace) [ \t\n\r\f\v] (space, tab, newline, ir pan.)
# \S ne tuščias tarpas - viskas, kas ne tarpas.
# \w alphanumeric: [0-9a-zA-Z_] - skaičiai nuo 0 iki 9, didžiosios ir mažosios raidės A-Z, simbolis '_'. UTF simboliai nėra alphanumeric.
# \W viskas, kas nėra prieš tai išvardintame punkte.
# . bet koks simbolis išskyrus eilutės pabaigos simbolį

# + Vieną ar daugiau kartų
# {x} Lygiai x kartų
# {x,y} Nuo x iki y kartų
# {x,} x arba daugiau kartų
# * Nulį ar daugiau kartų
# ? kartą, arba nei karto (optional)

# ^ - ieško šablono tik iš eilutės pradžios (* Naudojamas laužtiniuose skliaustuose turi reikšmę NOT)
# $ - ieško šablono tik iš eilutės pabaigos
# \b - žodžio ribos simbolis

# | - loginis 'arba'
# () - grupavimas

# https://github.com/robotautas/kursas/wiki/Regex-I-užduotys
# https://github.com/robotautas/kursas/wiki/Regex-II-užduotys