class Solution:
    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s)) + ">" + s
        return ans
    

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != ">":
                j += 1
            #current length
            length = int(s[i:j])
           
            #actual string
            #4#neet where j+1 is n and j+1+length = 3 or the next interger dilimeter for the next word
            ans.append(s[j+1 : j+1+length])
            
            #update next pointer to word
            i = j+1+length
        return ans