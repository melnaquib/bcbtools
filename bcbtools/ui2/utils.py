

def parse_amount_units(amount):
    a = amount.strip()
    a = a.replace(' ', '').lower()
    a = a.replace('bcb', '0' * 27)
    return a
