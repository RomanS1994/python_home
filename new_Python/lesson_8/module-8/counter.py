from collections import Counter

# Знайти скільки разув кожна літера зустрічається в цому тексті


text = "breakfast bread coffee work Python module laptop variables bug solution forum puzzle system team feedback video meeting internet project test presentation code function loop condition error input output data string integer list dictionary array server client network database cloud API design deploy algorithm result performance debug hardware software" 


def get_count_char(message):
    obj = {}

    for char in message:
        if not char in obj:
            obj[char] = 1
        else:
            obj[char] += 1
    return obj

res = get_count_char(text)
print(res)

print("****************")
counter = Counter(text)

print(counter)