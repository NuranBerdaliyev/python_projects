import re
from models import LogEntry

pattern = r"(.*?) (.*?) \| (.*?) \| (.*)"

def parse_line(line):
    matched = re.search(pattern, line)
    if not matched:
        return None
    
    date=matched.group(1)
    time=matched.group(2)
    level=matched.group(3)
    message=matched.group(4)

    return LogEntry(date, time, level, message)