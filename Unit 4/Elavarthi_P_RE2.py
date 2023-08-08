import sys; args = sys.argv[1:]
idx = int(args[0])-40
myRegexLst = [
    "/^[.ox]{64}$/i",
    '/^[xo]*\.[xo]*$/i',
    "/^(x+o*)?\.|\.(o*x+)?$/i",
    "/^(..)*.$/s",
    "/^(0|1[01])([01]{2})*$/",
    "/\w*(a[eiou]|e[aiou]|i[aeou]|o[aeiu]|u[aeio])\w*/i",
    "/^(1?0)*1*$/",
    "/^[bc]+$|^[bc]*a[bc]*$/",
    "/^(a[bc]*a|[bc])+$/",
    "/^((2|1[02]*1)[02]*)+$/"]

if idx < len(myRegexLst):
    print(myRegexLst[idx])

#Pranav Elavarthi, 2024, 5