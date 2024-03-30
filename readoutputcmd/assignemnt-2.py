from tabulate import tabulate

def analyze_log(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    count_file = 0
    count_keyboard = 0
    count_pipe = 0

    term_file = ' read('
    term_keyboard = ' read('
    term_tty = 'tty'
    term_pipe = 'pipe'

    for line in lines:
        if term_file in line:
            count_file += 1
        if term_keyboard in line and term_tty in line:
            count_keyboard += 1
        if term_keyboard in line and term_tty not in line and term_pipe not in line:
            count_pipe += 1

    return count_file, count_keyboard, count_pipe

def main():
    file_path_A = 'LogA.strace'
    file_path_B = 'LogB.strace'

    result_A = analyze_log(file_path_A)
    result_B = analyze_log(file_path_B)

    # Create a list of tuples for tabular data
    data = [
        ("Read from file", result_A[0], result_B[0]),
        ("Read from keyboard", result_A[1], result_B[1]),
        ("Read from pipe", result_A[2], result_B[2])
    ]

    # Print the table using tabulate
    print("Output A:")
    print(tabulate(data, headers=["Event", "Log A Count", "Log B Count"], tablefmt="grid"))

if __name__ == "__main__":
    main()
