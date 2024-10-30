import json
from pathlib import Path
contacts = {"name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}

filename = Path('./lesson_11/data.json')

def write_contacts_to_file(filename, contacts):
    with open(filename, "w",) as f:
        json.dump({"contacts": contacts}, f)
        
def read_contacts_from_file(filename):
    with open(filename, "r") as f:
        ret =  json.load(f)
        return ret["contacts"]
    
write_contacts_to_file(filename, contacts)

print(read_contacts_from_file(filename))