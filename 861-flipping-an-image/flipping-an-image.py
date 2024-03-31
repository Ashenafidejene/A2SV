class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        r, l = len(image[0]) - 1, 0
        for i in range(len(image)):
            while r >= l:
                if r == l:
                    image[i][r] = self.valueChanger(image[i][r])
                else:
                    value1 = self.valueChanger(image[i][r])
                    value2 = self.valueChanger(image[i][l])
                    image[i][l] = value1
                    image[i][r] = value2
                r -= 1
                l += 1
            l = 0
            r = len(image[i]) - 1
        return image

    def valueChanger(self, k: int) -> int:
        if k == 0:
            return 1
        return 0