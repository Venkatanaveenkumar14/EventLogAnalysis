
from tabulate import tabulate

def analyze_logs(log_file):
    last_occurrences = {}
    with open(log_file, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if "execve(" in line:
                parts = line.split('"')
                if len(parts) >= 2:
                    program_name = parts[1]
                    last_occurrences[program_name] = line_number
    return last_occurrences

def table(log_file_paths):
    last_occurrences_a = analyze_logs(log_file_paths[0])
    last_occurrences_b = analyze_logs(log_file_paths[1])

    all_programs = set(last_occurrences_a.keys()).union(set(last_occurrences_b.keys()))

    data = [
        [program, last_occurrences_a.get(program, "absent"), last_occurrences_b.get(program, "absent")]
        for program in all_programs
    ]

    headers = ["Program Name", "Last Occurrence Line Number in Log A", "Last Occurrence Line Number in Log B"]
    return tabulate(data, headers=headers, tablefmt="grid")

log_file_paths = ['LogA.strace', 'LogB.strace']
tableoutput = table(log_file_paths)

print(tableoutput)
