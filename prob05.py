treble, mega_pitch = input().split(" ")
treble = float(treble)
mega_pitch = float(mega_pitch)

droptitude = round(mega_pitch / 3.43 * treble, 1)

print(f"{droptitude} ", end = "")

if droptitude >= 75.0 and droptitude <= 85.0:
    print("NOW")
else:
    print("WAIT FOR IIIIIT")