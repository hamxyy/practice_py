import re

match1 = re.match(r"(\d+)(\d+)", "123fdaiou321ejwadhoq")

if(match1):
    print match1.groups()