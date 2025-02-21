class Duration:
    def __init__(self, seconds, minutes, hours):
        self.__seconds = seconds
        self.__minutes = minutes
        self.__hours = hours

    @property
    def seconds(self):
        return self.__seconds

    @property
    def minutes(self):
        return self.__minutes

    @property
    def hours(self):
        return self.__hours

    @staticmethod
    def from_seconds(duration):
        return Duration(duration, duration/60, (duration/60)/60 )
    
    @staticmethod
    def from_minutes(duration):
        return Duration(duration*60, duration, duration/60)
    
    @staticmethod
    def from_hours(duration):
        return Duration((duration*60)*60, duration*60, duration)
    
duration = Duration.from_seconds(60)

print(duration.seconds)
print(duration.minutes)
print(duration.hours, end="\n\n")

duration = Duration.from_minutes(60)

print(duration.seconds)
print(duration.minutes)
print(duration.hours, end="\n\n")

duration = Duration.from_hours(2)

print(duration.seconds)
print(duration.minutes)
print(duration.hours)
