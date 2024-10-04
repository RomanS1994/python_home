import re

text = "Bot activity detected: 32.16.4.162, 69.164.21.348 looks suspicios"

pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" 
ips = re.findall(pattern, text)
print(ips)    