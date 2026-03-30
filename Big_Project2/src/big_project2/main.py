import sys
import importlib
from big_project2.parser import parse_line
from big_project2.models import LogEntry
from big_project2.utils import LogIterator

def load_plugins():
    plugin_names=['big_project2.plugins.error_stats', 'big_project2.plugins.user_activity']
    plugins=[]
    for name in plugin_names:
        imported=importlib.import_module(name)
        plugins.append(imported)
    return plugins

def main():
    logs = []

    iterator = LogIterator('app.log')

    for line in iterator:
        entry = parse_line(line)
        if entry:
            logs.append(entry)
    
    if len(sys.argv)>1:
        level_filter=sys.argv[1]
        if level_filter in ["INFO", "WARNING", "ERROR"]:
            logs=list(filter(lambda x: isinstance(x, LogEntry) and x.get_level()==level_filter, logs))
        else:
            print("Wrong argument")
            return
        
    plugins = load_plugins()
    for plugin in plugins:
        result=plugin.analyze(logs)
        print(result)

if __name__=='__main__':
    main()
