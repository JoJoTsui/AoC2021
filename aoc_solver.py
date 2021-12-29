# %% day0
import pandas as pd
import os
os.chdir("/home/joey/test/AoC2021")
# %% day1
day1_input = "day1/day1.txt"
d1_df = pd.read_csv(day1_input, header=None)
depths = d1_df[0].to_list()
# puzzle d1


def d1p1_solve(depths) -> int:
    count = 0
    for i in range(len(depths) - 1):
        if depths[i] < depths[i + 1]:
            count += 1
    return count


def d1p2_solve(depths) -> int:
    count = 0
    for i in range(len(depths) - 3):
        tri1 = depths[i] + depths[i+1] + depths[i+2]
        tri2 = depths[i+1] + depths[i+2] + depths[i+3]
        if tri1 < tri2:
            count += 1
    return count


d1p1_answer = d1p1_solve(depths)
d1p2_answer = d1p2_solve(depths)
print("Day1 Puzzle1: {}\nDay1 Puzzle2: {}".format(d1p1_answer, d1p2_answer))
# %% day2
day2_input = "day2/day2.txt"
d2_df = pd.read_csv(day2_input, sep=" ", header=None)
# puzzle d2
def d2p1_solve(df) -> int:
    h = sum(df[df[0] == "forward"][1])
    v = sum(df[df[0] == "down"][1]) - sum(df[df[0] == "up"][1])
    return h * v
def d2p2_solve(df) -> int:
    h = 0
    v = 0
    a = 0
    for t, val in list(zip(df[0], df[1])):
        if t == "down":
            a += val
        elif t == "up":
            a -= val
        elif t == "forward":
            h += val
            v += (a * val)
    return h * v


d2p1_answer = d2p1_solve(d2_df)
d2p2_answer = d2p2_solve(d2_df)
print("Day2 Puzzle1: {}\nDay2 Puzzle2: {}".format(d2p1_answer, d2p2_answer))
# %% day3
day3_input = "day3/day3.txt"
def d3p1_solve(input) -> int:
    with open(input) as f:
        submarine = f.read().splitlines()
    cols = []
    nrow = len(submarine)
    for i in range(len(submarine[0])):
        l = [int(j[i]) for j in submarine]
        if sum(l) > (nrow / 2):
            most, least = "1", "0"
        else:
            most, least = "0", "1"
        cols.append((most, least))
    gamma = int("".join([i[0] for i in cols]), 2)
    epsilon = int("".join([i[1] for i in cols]), 2)
    return gamma * epsilon
def d3p2_solve(input) -> int:
    with open(input) as f:
        submarine = f.read().splitlines()
    cols = []
    nrow = len(submarine)
    def find_oxygen(submarine, idx) -> int:
        zero, one = [], []
        for i in submarine:
            if i[idx] == "0":
                zero.append(i)
            else:
                one.append(i)
        if len(one) >= len(zero):
            if len(one) > 1:
                return find_oxygen(one, idx + 1)
            else:
                return int(one[0], 2)
        else:
            if len(zero) > 1:
                return find_oxygen(zero, idx + 1)
            else:
                return int(zero[0], 2)
    def find_co2(submarine, idx) -> int:
        zero, one = [], []
        for i in submarine:
            if i[idx] == "0":
                zero.append(i)
            else:
                one.append(i)
        if len(one) >= len(zero):
            if len(zero) > 1:
                return find_co2(zero, idx + 1)
            else:
                return int(zero[0], 2)
        else:
            if len(one) > 1:
                return find_co2(one, idx + 1)
            else:
                return int(one[0], 2)
    oxygen = find_oxygen(submarine, 0)
    co2 = find_co2(submarine, 0)
    print(oxygen, co2)
    return oxygen * co2 
d3p1_answer = d3p1_solve(day3_input)
d3p2_answer = d3p2_solve(day3_input)
# %% day4
