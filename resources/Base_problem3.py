class Temperature(object):
    def __init__(self):
        self.__kelvin = 0
        self.__celsius = -273
        self.__fahrenheit = 459.4
    @property
    def celsius(self):
        return celsius.__kelvin
    @celsius.setter
    def celsius(self, celsius):
        self.__celsius = float(celsius)
        self.kelvin = self.__celsius + 273
        self.fahrenheit = (self.__celsius * 1.8) + 32

temp = input("Input degrees in Celsius: ")
converter = Temperature()
converter.celsius = temp
fahr = converter.fahrenheit
print("{} Celsius is {} Fahrenheit".format(temp, fahr))
