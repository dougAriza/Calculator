class Client:
    def __init__(self, product:str, company:str, startCycle:int, finalCycle:int, fails:int, stepBlisters:int) -> None:
        self.__product = product
        self.__company = company
        self.__startCycle = startCycle
        self.__finalCycle = finalCycle
        self.__fails = fails
        self.__stepBlisters = stepBlisters

    def setProduct(self, product:str):
        self.__product = product

    def getProduct(self):
        return self.__product

    def setCompany(self,company:str):
        self.__company = company

    def getCompany(self):
        return self.__company

    def efficiency(self) -> float:
        totalBlisters = self.__stepBlisters * (self.__finalCycle - self.__startCycle)
        return (totalBlisters - self.__fails) / totalBlisters * 100

