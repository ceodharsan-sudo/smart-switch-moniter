switches = 0
switches = switches | 1
switches = switches | 2
switches = switches | 4
print("Switch 1:", "ON" if switches & 1 else "OFF")
print("Switch 2:", "ON" if switches & 2 else "OFF")
print("Switch 3:", "ON" if switches & 4 else "OFF")
print("Switch 4:", "ON" if switches & 8 else "OFF")
switches = switches & ~2
print("After turning OFF switch 2:")
print("Switch 2:", "ON" if switches & 2 else "OFF")
