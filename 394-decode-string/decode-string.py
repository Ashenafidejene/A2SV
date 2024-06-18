class Solution:
    def decodeString(self, s: str) -> str:
        def calculator(index: int) -> tuple:
            answer = ""
            while index < len(s) and s[index] != ']':
                if s[index].isdigit():
                    num = 0
                    while index < len(s) and s[index].isdigit():
                        num = num * 10 + int(s[index])
                        index += 1
                    index += 1  # skip the '['
                    decoded_string, index = calculator(index)
                    index += 1  # skip the ']'
                    answer += num * decoded_string
                else:
                    answer += s[index]
                    index += 1
            return answer, index
        

        decoded_string, _ = calculator(0)
        return decoded_string