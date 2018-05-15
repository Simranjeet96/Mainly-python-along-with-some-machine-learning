import re

regex = r"o(?=bar)"

test_str = "foobar"

matches = re.finditer(regex, test_str)

for match in matches:
  numOfgrps=len(match.groups())
  print("it belongs to BIG grp:",match.group(0),"and its start and end is:",match.start(0),"to",match.end(0),"respectively")
  for i in range(numOfgrps):
    print(i+1,"subgrp:",match.group(i+1),"and its start and end is:",match.start(i+1),"to",match.end(i+1),"respectively")
  print("-"*20)