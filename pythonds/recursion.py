def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base,base) + convertString[n%base]
    
def reverse(s):
    if len(s) == 1:
        return s
    else:
        return reverse(s[1:]) + s[0]
    
def palindrome(s):
    
    if s.lower().replace(" ", "") == reverse(s).lower().replace(" ", ""):
        return True
    else:
        return False
    
print(palindrome('Kanakanak'))
print(palindrome('Live not on evil'))