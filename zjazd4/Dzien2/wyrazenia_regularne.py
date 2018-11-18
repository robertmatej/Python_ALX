import re

pattern  = re.compile("\d{3}-\d{3}-\d{3}")
text = "123-456-789 234-567-890 123-456-787-990 "

print(pattern.findall(text))