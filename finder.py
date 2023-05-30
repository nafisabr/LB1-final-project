import sys

def get_mcc(line):
    # Find the MCC value in the line and return it as a float
    mcc_start = line.find('MCC: ') + 5
    mcc_end = line.find(' ', mcc_start)
    mcc_str = line[mcc_start:mcc_end].strip()
    try:
        return float(mcc_str)
    except ValueError:
        return None


def find_line_with_highest_mcc(filename):
    highest_mcc = float('-inf')
    highest_mcc_line = None

    with open(filename, 'r') as file:
        for line in file:
            line_mcc = get_mcc(line)
            if line_mcc is not None and line_mcc > highest_mcc:
                highest_mcc = line_mcc
                highest_mcc_line = line

    return highest_mcc_line

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide the filename as a command-line argument.")
        sys.exit(1)

    filename = sys.argv[1]
    line_with_highest_mcc = find_line_with_highest_mcc(filename)

    if line_with_highest_mcc:
        print("Line with the highest MCC:")
        print(line_with_highest_mcc)
    else:
        print("No valid MCC lines found in the file.")


