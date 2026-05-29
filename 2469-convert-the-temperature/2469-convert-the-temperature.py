class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        l=[]
        l+=[celsius+273.15]
        l+=[(celsius*1.80)+32.00]
        return l