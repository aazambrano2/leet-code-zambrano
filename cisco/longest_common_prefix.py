# def longestCommonPrefix(strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         if len(strs) == 1 and len(strs[0]) != 0:
#             return strs[0][0]
#         if "" in strs:
#             return ''
#         #check if all words are the same
#         w = set()
#         for word in strs:
#             w.add(word)
#         if len(w) == 1: return strs[0]
        
#         prefixes = []
#         pf = ''
#         n= 1
#         i=0
#         while i < len(strs):
#             pf = strs[0][:n]
#             print(pf,i,n)
#             if pf not in strs[i]:
#                 break
#             #Restart
#             if i == len(strs)-1:
#                 prefixes.append(pf)
#                 n +=1
#                 i=0
#             i+=1

#         for word in strs[1:]:
#             if pf not in word and word == strs[-1]:
#                 pf = ''
#         return max(prefixes) if prefixes else pf

#######################SOLUTION#####################
def longestCommonPrefix(strs):
    
    #sort the string
    strs.sort()
            
#for loop comparing first and last element
    for i in range(len(strs[0])):
        if strs[0][i] != strs[-1][i]: #stop where the corresponding ith element is NOT the same and return evrything before that ith element
            return strs[0][:i]
        
    return strs[0] #if the first and last element are equal return the first element


print(longestCommonPrefix(["flower","flower","flower","flower"]))