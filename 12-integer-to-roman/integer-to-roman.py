class Solution:
    def intToRoman(self, num: int) -> str:
        self.ans = ""
        def changer(n):
            if n == 0 :
                return 
            if n < 5 :
                if n == 4 :
                    self.ans +="IV"
                else:
                    for i in range(n):
                        self.ans +="I"
                return 
            elif n < 10 :
                if n%5 == 4 :
                    self.ans +="IX"
                    return 
                else:
                   n = n - 5 
                   self.ans +="V"
                changer(n)
            elif n < 50:
                k = n % 10 
                l = n//10
                if l == 4:
                    self.ans += "XL"
                else:
                    for i in range(l):
                        self.ans +="X"
                changer(k)
            elif n < 100 : 
                k = n % 10
                l = n // 10 
                if l == 9 :
                    self.ans += "XC"
                else:
                    self.ans +="L"
                    for i in range(0,l-5):
                       self.ans += "X"
                changer(k)
            elif n < 500 :
               k = n % 100
               l = n//100
               if l == 4:
                  self.ans += "CD"
               else :
                  for i in range (0,l):
                    self.ans += "C"
               changer(k)
            elif n < 1000:
                k = n % 100
                l = n//100
                if l == 9:
                    self.ans += "CM"
                else:
                    self.ans +="D"
                    for i in range(0,l-5):
                        self.ans += "C"
                changer(k)
            else:
                k = n % 1000
                l = n // 1000
                for i in range(l):
                    self.ans += "M"
                changer(k)
        changer(num)
        return self.ans
                 




                


                
                