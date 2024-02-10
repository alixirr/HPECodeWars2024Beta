
with open(r"input.txt", "r") as f:
        files = []

        for line in f:
            files.append(line.rstrip())

key = files[0] # the thing we are searching for
files.pop(0) #remove the key from the list
files.pop() #remove END last line

# now files[] is just a list of files we need to search

found = False
i = 0;
while not found:
    file = files[i]
    if (file != "END"):
        with open(file, "r") as f:
            data = [i for i in f.read().strip().split('\n')]
        
        y = 0
        for line in data:
            x = 0
            for char in line:
                if (char == key):
                    location, _ = file.split(".")
                    print(f"Found the ring! It was {location} at ({x},{y})")
                    found = True
                x += 1
            y += 1
        i += 1
    else:
        break