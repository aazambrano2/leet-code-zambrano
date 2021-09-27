
def helper(s):
    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False
    else:
        return validPalindrome(s[1:-1])


def validPalindrome(s):
    #get rid of any unessesary characters
   s= s.lower()
   new_string = ""
   for i in range(len(s)):
       if ord(s[i]) >= 97 and ord(s[i]) <= 122: #or use isalpha()
           new_string  = new_string  + s[i]
   return helper(new_string)

print(validPalindrome("A man, a plan, a canal: Panama"))