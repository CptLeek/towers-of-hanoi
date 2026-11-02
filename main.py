import time

move_count = 0

def move (n, Tower1, Tower2, Tower3):
    global move_count
    if n > 0:
        move(n-1, Tower1, Tower3, Tower2)
        print("Move disk", n, "from", Tower1, "to", Tower3)
        move_count += 1
        move(n-1, Tower2, Tower1, Tower3)


startTime = time.time_ns()
move(20, "Tower 1", "Tower 2", "Tower 3")
endTime = time.time_ns()
print("Moves taken:", move_count)
print ("Time taken: " + str((endTime - startTime)/1000000000) + " seconds")
