def reverseString(self, s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    #NO SLICE OR EXTRA ARRAY
    
    if len(s) == 1:
        return s
    l = len(s)
    for i in range(l/2):
        if i < len(s)/2:
            s[i], s[l-i-1] = s[l-i-1], s[i]
            
    #[l-i-1]  meaning the lenght of the list - the current index of the list - 1 so your point of intrest of the list shrinks [[ [ [ ] ] ] ]


    return s