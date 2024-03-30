def analyze_log(log_file):
    events = []
    with open(log_file, 'r') as file:
        for line in file:
            if "read(" in line and "/dev/tty" in line:
                keystrokes = line.split('"')[1] if '"' in line else "N/A"
                events.append(f"The user provides the following keystrokes to the console: {keystrokes}")
            if "write(" in line and "/dev/tty" in line:
                info = line.split('"')[1] if '"' in line else "N/A"
                events.append(f"The console shows the following message to the user: {info}")
    return events

def console_events(events):
    for event in events:
        print(event)

log_file_path = 'LogB.strace'
user_console = analyze_log(log_file_path)

console_events(user_console)
