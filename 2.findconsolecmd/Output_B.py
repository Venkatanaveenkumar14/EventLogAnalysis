from tabulate import tabulate

def countingevents(log_file):
    c = {
        "Program Starts Running": 0,
        "Write Events": 0,
        "File Status Events": 0,
        "File Unlinking Events": 0,
        "Program Ends Executing": 0
    }
    with open(log_file, 'r') as file:
        for line in file:
            if "execve" in line:
                c["Program Starts Running"] += 1
            if "write(" in line:
                c["Write Events"] += 1
            if any(keyword in line for keyword in ["stat(", "lstat(", "fstat("]):
                c["File Status Events"] += 1
            if "unlink(" in line:
                c["File Unlinking Events"] += 1
            if "exit_group(" in line:
                c["Program Ends Executing"] += 1
    return c

def table(file_paths):
    output = countingevents(file_paths[0])
    outputs = countingevents(file_paths[1])

    results = [
        ["Program Starts Running", output["Program Starts Running"], outputs["Program Starts Running"]],
        ["Write Events", output["Write Events"], outputs["Write Events"]],
        ["File Status Events", output["File Status Events"], outputs["File Status Events"]],
        ["File Unlinking Events", output["File Unlinking Events"], outputs["File Unlinking Events"]],
        ["Program Ends Executing", output["Program Ends Executing"], outputs["Program Ends Executing"]]
    ]

    heading = ["Event", "Log File A", "Log File B"]

    return results, heading

file_paths = ['LogA.strace', 'LogB.strace']                     # Paths to the log files
results, heading = table(file_paths)                            # Generating the table for Output B
print(tabulate(results, headers=heading, tablefmt="grid"))      # Display the table
