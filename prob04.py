with open(r"input.txt", "r") as f:
        lines = []

        for line in f:
            lines.append(line.rstrip())

lines.pop() #removes the 00000 ending line

key = {
    "A": 1,
    "B": 2,
    "G": 3, 
    "D": 4,
    "E": 5,
    "#": 6,
    "Z": 7,
    "Y": 8,
    "H": 9,
    "I": 10,
    "K": 20,
    "L": 30, 
    "M": 40,
    "N": 50,
    "X": 60,
    "O": 70,
    "P": 80,
    "Q": 90,
    "R": 100,
    "S": 200,
    "T": 300,
    "U": 400,
    "F": 500,
    "C": 600,
    "$": 700,
    "W": 800,
    "3": 900
}

for line in lines:
    sum = 0
    for char in line:
        sum += key[char]
    print(sum)
    