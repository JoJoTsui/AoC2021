# %% day1
import pandas as pd

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
