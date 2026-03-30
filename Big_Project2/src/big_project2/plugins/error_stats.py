from src.big_project2.utils import measure_time

@measure_time
def analyze(logs):
    messages_counts={}
    for log in logs:
        if log._level=="ERROR":
            messages_counts[log._message]=messages_counts.get(log._message, 0)+1
    result=f"Total ERROR logs: {sum(messages_counts.values())}\n"
        
    for message, count in messages_counts.items():
        result+=f"Total amount of ERROR message '{message}': {count}\n"
    return result
