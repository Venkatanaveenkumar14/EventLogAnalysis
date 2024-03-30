from tabulate import tabulate

log_file_paths = ['LogA.strace', 'LogB.strace']

headers = ["Event", "Log File A", "Log File B"]

data = []

for log_file in log_file_paths:
    counts = {"Read from a File": 0, "Read from Keyboard": 0, "Read from Pipe": 0}
    with open(log_file, 'r') as file:
        for line in file:
            if "read(" in line:
                if "/dev/tty" in line:
                    counts["Read from Keyboard"] += 1
                elif "pipe" in line:
                    counts["Read from Pipe"] += 1
                else:
                    counts["Read from a File"] += 1

    data.append(["Read from a File", counts["Read from a File"], 0])
    data.append(["Read from Keyboard", counts["Read from Keyboard"], 0])
    data.append(["Read from Pipe", counts["Read from Pipe"], 0])
    
formatted_data = [[event, data[i][1], data[i + 3][1]] for i, (event, _, _) in enumerate(data[:3])]

output_table = tabulate(formatted_data, headers=headers, tablefmt="grid", numalign="right")

print(output_table)
