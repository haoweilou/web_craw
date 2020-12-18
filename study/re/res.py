import re
key = "javapythonc++php"
s = re.findall("python",key)

key = "<html>Hello world</html>"
s = re.findall("<html>(.*)</html>",key)

key = "I like 178"
s = re.findall("\d+",key)
print(s)