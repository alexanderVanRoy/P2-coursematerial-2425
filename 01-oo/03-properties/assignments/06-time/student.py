# Write your code here
class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    @property
    def hours(self):
        return self.__hours
    
    @hours.setter
    def hours(self, value):
        if isinstance(value, int):
            if value >= 0 and value <= 23:
                self.__hours = value
            else:
                raise ValueError

    @property 
    def minutes(self):
        return self.__minutes
    
    @minutes.setter
    def minutes(self, value):
        if isinstance(value, int):
            if value >= 0 and value <= 59:
                self.__minutes = value 
            else:
                raise ValueError

    @property
    def seconds(self):
        return self.__seconds
    
    @seconds.setter
    def seconds(self, value):
        if isinstance(value, int):
            if value >= 0 and value <= 59:
                self.__seconds = value
            else:
                raise ValueError


# time = Time(0,0,0)
# time.hours = 8
# time.hours = 24

# print(time.hours)
# print(time.minutes)
# print(time.seconds)
