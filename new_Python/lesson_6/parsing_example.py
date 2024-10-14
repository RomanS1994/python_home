import re
"""
Написати функцію яка буде діставати дату з рядків певного формату
"""


# 2024-10-12  16:25 | Привіт!
# yyyy-mm-dd  dd:mm | message

# \d{4}-\d{2}-\d{2}
# \d{2}:\d{2}
#[a-z]+

# 2024-10-12  16:25 | Привіт!
# (?<first>\w+)
# (?P<name>regex)

example_string = '2024-10-12  16:25 | Привіт!'
pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"

# patern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"

result = re.match(pattern, example_string)

print(result is True)