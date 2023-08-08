import sys; args = sys.argv[1:]
idx = int(args[0])-50
myRegexLst = [
    r"/(\w)+\w*\1\w*/i", #50
    r"/\b(\w)+(\w*\1\w*){3}\b/i", #51
    r"/^([01])([01]*\1)?$/", #52
    r"/\b(?=\w*cat)\w{6}\b/i", #53
    r"/\b(?=\w*bri)(?=\w*ing)\w{5,9}\b/i", #54
    r"/\b((?!cat)\w){6}\b/i", #55
    r'/\b((\w)(?!\w*\2))+\b/i', #56
    r"/^((?!(10011))[01])*$/", #57
    r'/\w*(a[eiou]|e[aiou]|i[aeou]|o[aeiu]|u[aeio])\w*/i', #58
    r"/^((?!1[01]1)[01])*$/", #59
]
    

if idx < len(myRegexLst):  
    print(myRegexLst[idx])

#Pranav Elavarthi, 2024, 5