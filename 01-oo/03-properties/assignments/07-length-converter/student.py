class LengthConverter:
    def __init__(self):
        self.__distance_in_meters = 0
    
    @property
    def meter(self):
        return self.__distance_in_meters
    
    @meter.setter
    def meter(self, value):
        self.__distance_in_meters = value
    
    @property
    def feet(self):
        return round(self.__distance_in_meters * 3.28084,3)
    
    @feet.setter
    def feet(self, value):
        self.__distance_in_meters = value / 3.28084
    
    @property
    def inch(self):
        return round(self.__distance_in_meters * 39.3700787,2)
    
    @inch.setter
    def inch(self, value):
        self.__distance_in_meters = value / 39.3700787

# convertor = LengthConverter()

# convertor.inch = 100

# print(convertor.meter)
# print(convertor.feet)
# print(convertor.inch)