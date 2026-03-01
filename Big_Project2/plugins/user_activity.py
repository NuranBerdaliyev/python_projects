import re
from utils import measure_time

@measure_time
def analyze(logs):
    users=dict()
    logged_in=0
    logged_out=0
    for log in logs:
        m=re.search(r"User (\d+)", log._message)
        if not m:
            continue
        
        if m.group(1) not in users:
            users[m.group(1)]={
                "actions":0,
                "Logged out":False
            }
        if "logged in" in log._message:
            logged_in+=1
            users[m.group(1)]["Logged_out"] = False
        elif "logged out" in log._message:
            logged_out+=1
            users[m.group(1)]["Logged out"]=True
        else:
            users[m.group(1)]["actions"]+=1
    active_sessions=logged_in-logged_out
        
    result=f"User's amount who used the server is {len(users)}\n" +\
        f"Amount of logging in general: {active_sessions}\n"+\
        f"Amount of users who logged in: {logged_in}\n" +\
        f"Amount of users who logged out: {logged_out}\n"
    not_logged_out = [
        user_id for user_id, data in users.items()
        if not data["Logged_out"]
    ]
    result+=f"Users who didn't log out until server shuts down: {not_logged_out}\n"
    for user in users.items():
        result+=f"User {user[0]} carried out {user[1]['actions']} actions\n"

    return result
