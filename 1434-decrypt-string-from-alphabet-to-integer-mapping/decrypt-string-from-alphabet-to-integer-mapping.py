class Solution:
    def freqAlphabets(self, s: str) -> str:
        counter ={'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i',
       '10#': 'j', '11#': 'k', '12#': 'l', '13#': 'm', '14#': 'n', '15#': 'o', '16#': 'p', '17#': 'q',
        '18#': 'r', '19#': 's', '20#': 't', '21#': 'u', '22#': 'v', '23#': 'w', '24#': 'x', '25#': 'y',
       '26#': 'z'}
        i = len(s)-1
        answer = ""
        while i >= 0 :
            if s[i]!='#' :
                answer = counter[s[i]] + answer 
                i-=1
            else :
                hash=''
                hash+=s[i-2]  + s[i-1] + s[i]
                answer = counter[hash] + answer 
                i -=3 
        return answer 



        