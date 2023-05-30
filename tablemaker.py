import sys

def read_numbers_from_file(filename, keyword):
    with open(filename, 'r') as file:
        content = file.readlines()
        for line in content:
            if keyword in line:
                numbers = line.split(':')[1].split()[0]
                return int(numbers)
    return 0

def generate_table(file1, file2):
    true_positive = read_numbers_from_file(file1, 'Initial search space (Z):')
    true_negative = read_numbers_from_file(file2, 'Initial search space (Z):')
    detected_positive = read_numbers_from_file(file1, 'Domain search space  (domZ):')
    detected_negative = read_numbers_from_file(file2, 'Domain search space  (domZ):')

    table = [['True Positive', 'True Negative'],
             [str(true_positive), str(true_negative)],
             ['Detected Positive', 'Detected Negative'],
             [str(detected_positive), str(detected_negative)]]

    return table

if __name__ == '__main__':
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 3:
        print('Usage: python script.py file1.txt file2.txt')
    else:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        table = generate_table(file1, file2)

        # Display the table
        for row in table:
            print('\t'.join(row))

