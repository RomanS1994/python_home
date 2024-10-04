import re
message = 'Hello Roman, How was YOUR day, you has 30 years?'



def search_word(text):

    pattern = r"(?P<word>\b[A-Z]+\b).*(?P<number>\b\d+\b)"
    res = re.search(pattern, text)

    return res.groupdict()


obg_s_w = search_word(message)
print(obg_s_w["word"])