class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        f =( 9/5) *celsius + 32 
        k = celsius + 273.15 
        return [k,f]       