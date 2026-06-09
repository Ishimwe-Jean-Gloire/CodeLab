with open('speeding.in', 'r') as infile, open('speeding.out', 'w') as outfile:
    N,M = map(int, infile.readline().split())
    
    limit_at_mile=[]
    bessie_at_mile=[]

    for _ in range(N):
        length,limit = map(int, infile.readline().split())
        limit_at_mile.extend([limit]*length)

    for _ in range(M):
        length,speed = map(int, infile.readline().split())
        bessie_at_mile.extend([speed]*length)
    
    total_over_speed=0
    for i in range(100):
        infraction = bessie_at_mile[i] - limit_at_mile[i]
        if infraction > total_over_speed:
            total_over_speed = infraction

    outfile.write(str(total_over_speed) + "\n")