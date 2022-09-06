import re


def convert_data(data):
    pattern = re.compile(r'(\d{2})\.(\d{2})\.(\d{4})')
    result = pattern.search(data)
    print(f"{result.group(3)} {result.group(2)} {result.group(1)}")

convert_data("14.05.2001")
