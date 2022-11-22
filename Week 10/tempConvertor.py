class TempConvertor:
    KELVIN = 'K'
    FAHRENEIT = 'F'
    CELSIUS='C'

    @staticmethod
    def celsuisToFah(value):
        F = (value * (9/5)) + 32
        print(F)
  
    @staticmethod
    def FahToCelsius(value):
        C=(value-32)*(5/9)
        print(C)

    @staticmethod
    def celsiusToKelvin(value):
        K=(value + 273.15)
        print(K)

    @staticmethod
    def kelvinToCelsiuss(value):
        C=(value - 273.15)
        print(C)  
    @staticmethod
    def FahToKelvin(value):
        K=(value-32)*(5/9) + 273.15
        print(K)
    @staticmethod
    def kelvinToFah(value):
        F=(value-273.15)*(9/5)+32
        print(F)

#convertTemp = TempConvertor()
#value=float(input("Please enter the value :"))
TempConvertor.celsuisToFah(10)
TempConvertor.celsiusToKelvin(12)
TempConvertor.FahToCelsius(-40)
TempConvertor.FahToKelvin(100)
TempConvertor.kelvinToCelsiuss(222)
TempConvertor.kelvinToFah(232)

