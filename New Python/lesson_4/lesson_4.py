# find max vowels substring adn its length
import re
# def find_max_vowels_reg(text):
#     pattern = r'[aeiou]+'
#     chains = re.findall(pattern, text)
#     print(chains)

# text = 'aevsaefsdsade asds d asd sa  oleeeeeeeeh'
# res = find_max_vowels_reg(text)
# print(text)


# https://www.codewars.com/kata/56a24b309f3671608b00003a/python
# def dad_filter(string):
#     while ",," in string:
#         string = string.replace(",,", ",")
#     return string.strip(", ")

def dad_filter(message):
    return re.sub(',{2,}', ',', message).strip(',')

res = dad_filter("asdsad,d,as,dsa,dsa,das,d,,,asdsad ,,,asd,,")
print(res) 