class Time:
    def __init__(self):
        self._hours = 0
        self._minutes=0
        self._seconds=0               
        
    @property
    def hours_simple(self):
        if self._hours > 12:
            return self._hours -12
        else:
            return self._hours
      
    @property
    def period(self):
        if self._hours >= 12:
            return "PM"
        elif self._hours < 12:
            return "AM"
           
    def set_hours(self,value):
        if value > 23:
            self._hours = 23

        elif value < 0:
            self._hours = 0
        
        else:
            self._hours= value
    
    def set_minutes(self,value):
        if value > 59:
            self._minutes = 59

        elif value < 0:
            self._minutes = 0
        
        else:
            self._minutes= value

    def set_seconds(self,value):
        if value > 59:
            self._seconds = 59

        elif value < 0:
            self._seconds = 0
        
        else:
            self._seconds= value

    def get_hours(self):
        return self._hours
    
    def get_minutes(self):
        return self._minutes

    def get_seconds(self):
        return self._seconds
    
    
    
    hours = property(get_hours, set_hours)
    minutes = property(get_minutes, set_minutes)
    seconds = property(get_seconds, set_seconds)
    

    

    
def main():
    new = Time()
    hours = int(input("what hour:"))
    new.hours = hours
    minutes = int(input("what minute:"))
    new.minutes = minutes
    seconds = int(input("what second:"))
    new.seconds = seconds    
    
    print("militar {}:{}:{}".format(new.hours,new.minutes,new.seconds))
    print("12 horas {}:{}:{} {}".format(new.hours_simple,new.minutes,new.seconds,new.period))
    
    

if __name__ == "__main__":
    main()
