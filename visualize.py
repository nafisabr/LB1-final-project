import sys
import matplotlib.pyplot as plt

def read_file(filename):
    lst = []
    with open(filename, 'r') as file:
        for line in file:
            lst.append(line.strip().split("["))
    fpr_list1 = lst[0][1].split(",")
    tpr_list1 = lst[1][1].split(",")
    fpr_list1.pop(-1)
    tpr_list1.pop(-1)
    fpr_list = [float(el) for el in fpr_list1]
    tpr_list = [float(el) for el in tpr_list1]
    return fpr_list, tpr_list

def plot_roc_curve(fpr_list, tpr_list):
    plt.title("Receiver Operating Characteristic - ROC Curve", fontsize=14)
    plt.plot(fpr_list, tpr_list, color='hotpink', linewidth=2, label='Model performance')
    plt.plot([0, 1e-4], [0, 1], linestyle='--', color='blue', label='Random classifier')
    plt.xlabel('False Positive Rate (FPR)')
    plt.ylabel('True Positive Rate (TPR)')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    fpr_list, tpr_list = read_file(filename)
    plot_roc_curve(fpr_list, tpr_list)
