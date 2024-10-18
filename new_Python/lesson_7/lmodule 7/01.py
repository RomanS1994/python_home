phone_numbers = [
    "0509993636",
    "0679993636",
    "0959993636",
    "0969993636",
    "0509993637",
    "0639993636",
    "0509993632",
    "0339993632",
]


phone_book = []
for number in phone_numbers:
    if number.startswith('050') or number.startswith('095'):
        if "Vodafone" in phone_book:
            phone_book['Vodafone'].append(number)
        else:
            phone_book['Vodafone'] = [number]
    if number.startswith('050') or number.startswith('095'):
        if "Vodafone" in phone_book:
            phone_book['Vodafone'].append(number)
        else:
            phone_book['Vodafone'] = [number]
    if number.startswith('050') or number.startswith('095'):
        if "Vodafone" in phone_book:
            phone_book['Vodafone'].append(number)
        else:
            phone_book['Vodafone'] = [number]




print(phone_book)
