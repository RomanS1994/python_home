from collections import defaultdict

text = "breakfast bread coffee work Python module laptop variables bug solution forum puzzle system team feedback video meeting internet project test presentation code function loop condition error input output data string integer list dictionary array server client network database cloud API design deploy algorithm result performance debug hardware software" 



def filtered_message(message):
    filtered_list = message.split(' ')
    
    filtered_obj = {}

    for word in filtered_list:
        ind = word[0]
        if ind not in filtered_obj:
            filtered_obj[ind] = [word]
        else:
            filtered_obj[ind].append(word) 
        
    return filtered_obj


res = filtered_message(text)

# print(res)


def get_word_list_dd(message):
    filtered_list = message.split(' ')
    
    filtered_obj = defaultdict(list)

    for i in filtered_list:
        filtered_obj[i[0]].append(i)
    return filtered_obj

res = get_word_list_dd(text)
print(res)
