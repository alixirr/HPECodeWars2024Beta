import math

# read in data
with open(r"input.txt", "r") as f:
    tests = []

    for line in f:
        tests.append(line.rstrip())

tests.pop() # remove the last input number which is 0

nums = ["5", "4", "3", "2", "1"] # these are the numbers that we need to give the frequency of

freq = [] # create a list that corresponds to frequency of each number in nums

ae_num = 0 # numerator of the average efficiency value, multiply frequency by number
ae_den = 0 # denominator of average efficiency value, add frequencies up
avg_eff = 0 # average efficiency

for i in range(0, len(nums)):
    freq.append(tests.count(nums[i])) # for every number, we find how many times it appears in the tests list and we store that number in the freq list
    ae_num += int(nums[i]) * freq[i]
    ae_den += freq[i]


spaces = 1 # for printing purposes, the default width we need to display the frequency is 1
for num in freq:
    if num >= 10: # but... if ANY of the frequencies are two digits, we need to make the width to display the frequency 2
        spaces = 2


for i in range(0, len(nums)):
    print(f"{nums[i]} ({freq[i]: >{spaces}}) |", end = "") # some formatting magic
    for j in range(0, freq[i]):
        print("=", end = "")
    print("") # go to next line

# calculating average efficiency
avg_eff = float(ae_num) / ae_den
avg_eff = math.trunc(avg_eff * 100) / 100

print(f"Average efficiency: {avg_eff:.2f}")