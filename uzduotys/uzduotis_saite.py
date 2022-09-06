#https://regex101.com

# Buveinės adresas: Konstitucijos pr. 20A, 03502 Vilnius
# Telefonai:
# 1884 arba +370 5 268 4444 (Privatiems klientams)
# 1633 arba +370 5 268 4422 (Verslo klientams)
# Faksas: (8 5) 258 2700
# El. paštas: info@swedbank.lt
# Įmonės kodas: 112029651
# PVM mokėtojo kodas: LT120296515
# Banko sąskaita: LT55 7300 0100 0000 0036
# Banko kodas: 73000
# SWIFT kodas: HABALT22

# 1. [A-Z]\w+
# 2. [A-Z]+[A-Z]
# 3. 1\d{3}
# 4. \+370\s\d\s\d{3}\s\d{4}
# 5. \(\d\s\d\)\s\d{3}\s\d{4}
# 6. \+370\s\d\s\d{3}\s\d{4}|\(\d\s\d\)\s\d{3}\s\d{4}
# 7. [A-Z]{2}\d{2}\s\d{4}\s\d{4}\s\d{4}\s\d{4}
# 8. [A-Z]{2}\d{9}
# 9. .+\:
# 10. ([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6})
# 11. [a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}


# 1. Išrinkite visus žodžius, prasidedančius viena didžiąja raide.
# 2. Išrinkite visus žodžius, kurie yra iš visų didžiųjų raidžių (PVM, SWIFT, HABALT22)
# 3. Parašykite šabloną trumpąjam telefono numeriui (nereikia idealaus, tiesiog išrinkite 1884 ir 1663)
# 4. Parašykite šabloną ilgąjam telefono numeriui
# 5. Parašykite šabloną fakso numeriui
# 6. Parašykite šabloną, kuris tiktų ir ilgąjam telefono numeriui, ir faksui (naudokite '|' ir grupavimą)
# 7. Parašykite šabloną banko sąskaitos numeriui
# 8. Parašykite šabloną PVM mokėtojo kodui
# 9. Išrinkite visus žodžius prieš dvitaškį
# 10. Parašykite paprastą šabloną el. paštui
# 11. [a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6} - Tai yra nesudėtingas el. pašto šablonas. Išnagrinėkite, palyginkite su savo sukurtu.
# 12. https://digitalfortress.tech/tricks/top-15-commonly-used-regex/ - pasinagrinėkite.