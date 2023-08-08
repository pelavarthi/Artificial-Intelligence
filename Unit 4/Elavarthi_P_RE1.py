import sys; args = sys.argv[1:]

idx = int(args[0])-30 # 30-39

myRegexList = [
"/^101$|^100$|^0$/",
"/^[01]*$/",
"/.*0$/",
"/\w*[aeiou]\w*[aeiou]\w*/i",
r"/^0$|^1[01]*0$/",
"/^[01]*110[01]*$/",
r"/^.{2,4}$/s",
r"/^\d{3} *-? *\d\d *-? *\d{4}$/",
r"/^.*?d\w*/mi",
r"/^[01]?$|^1[01]*1$|^0[01]*0$/"
]
print(myRegexList[idx])
'''
X means syntax error
E means script error
T means time out
M means missing
D means no trailing /
O means bad option
I means invalid regular expression
P means shouldn't be doing this
N means internal error
r'\ makes no \\
'''

# Pranav Elavarthi, 5, 2024
