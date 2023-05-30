#!/usr/bin/python
import sys
import math

def get_hmm(filename):
    f_list = []
    d = {}
    with open(filename) as f:
        for line in f:
            v = line.rstrip().split()
            d.setdefault(v[0], []).append([float(v[1]), int(v[2]), v[0]])
        for ids in d.keys():
            d[ids].sort()
            f_list.append(d[ids][0])
        return f_list

def get_conf_mtrx(data, threshold):
    cm = [[0.0, 0.0], [0.0, 0.0]]
    for i in data:
        if i[0] < threshold and i[1] == 1:
            cm[0][0] += 1
        if i[0] >= threshold and i[1] == 1:
            cm[1][0] += 1
        if i[0] < threshold and i[1] == 0:
            cm[0][1] += 1
        if i[0] >= threshold and i[1] == 0:
            cm[1][1] += 1
    return cm

def accuracy(cm):
    total = sum(sum(row) for row in cm)
    if total == 0:
        return 0
    correct = cm[0][0] + cm[1][1]
    return correct / total

def matthew_cc(cm):
    d = (cm[0][0] + cm[1][0]) * (cm[0][0] + cm[0][1]) * (cm[1][1] + cm[1][0]) * (cm[1][1] + cm[0][1])
    if d == 0:
        d = 1
    return (cm[0][0] * cm[1][1] - cm[0][1] * cm[1][0]) / math.sqrt(d)

def tpr(cm):
    if cm[0][0] == 0:
        return 0
    return cm[0][0] / (cm[0][0] + cm[1][0])

def fpr(cm):
    if cm[0][1] == 0:
        return 0
    return cm[0][1] / (cm[0][1] + cm[1][1])

if __name__ == "__main__":
    filename = sys.argv[1]
    data = get_hmm(filename)
    tpr_list = []
    fpr_list = []
    for i in range(30):
        threshold = 10 ** -i
        cm = get_conf_mtrx(data, threshold)
        tpr_value = tpr(cm)
        fpr_value = fpr(cm)
        tpr_list.append(tpr_value)
        fpr_list.append(fpr_value)
    print("fpr_list:", fpr_list)
    print("tpr_list:", tpr_list)
