# camelCase, PascalCase, snake_case
# convert string from camelCase to snake_case

text = "userIsAuthenticated"


# declaration
# function signature: def + name + list of params
def convert_camel_to_snake_case(text, is_pascal_case):
    # scope
    res = ""
    for char in text:
        if char.isupper():
            res += "_" + char.lower()
        else:
            res += char
    if is_pascal_case:
        res = res[1:]
    return res


# function call
# () -> call operator

converted_text = convert_camel_to_snake_case("dbPassword", False)


print(converted_text)  
converted_text = convert_camel_to_snake_case("dbPassword", True)
print(converted_text)
# loop, for-loop
# find capital letter
