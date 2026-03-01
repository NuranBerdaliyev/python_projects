class LogEntry:
    def __init__(self, date, time, level, message):
        self._date=date
        self._time=time
        self._level=level
        self._message=message
    
    def __repr__(self):
        return f'{self._date} {self._time} | {self._level} | {self._message}'
