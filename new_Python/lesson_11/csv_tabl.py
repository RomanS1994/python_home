import csv

contactes = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Chaim Lewis",
        "email": "dui.in@egetlacus.ca",
        "phone": "(294) 840-6685",
        "favorite": False,
    },
    {
        "name": "Kennedy Lane",
        "email": "mattis.Cras@nonenimMauris.net",
        "phone": "(542) 451-7038",
        "favorite": True,
    },
    {
        "name": "Wylie Pope",
        "email": "est@utquamvel.net",
        "phone": "(692) 802-2949",
        "favorite": False,
    },
    {
        "name": "Cyrus Jackson",
        "email": "nibh@semsempererat.com",
        "phone": "(501) 472-5218",
        "favorite": True,
    },
]

filename = "test.csv"

def write_contacts_to_file(filename, contacts):
    with open(filename, "w", newline='') as f:
        field_names = ['name', 'email', 'phone', 'favorite']
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(contacts)

def read_contacts_from_file(filename):

    contacts = []
    with open(filename, "r") as f:  
        reader = csv.DictReader(f)
        for row in reader:
            contact = dict(row)
            if contact["favorite"] == "True":
                contact["favorite"] = True
            if contact["favorite"] == "False":
                contact["favorite"] = False
            contacts.append(contact)
    return contacts  

write_contacts_to_file(filename, contactes)    
print(read_contacts_from_file(filename)) 