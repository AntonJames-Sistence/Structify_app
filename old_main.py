def count_intersections(chords):
    intersections = 0
    length = int(len(chords[0]) / 2)
    
    chords = chords[0]
    # print(chords)
        
    p1 = 0
    p2 = 1
    while p1 < length - 1:
        start1 = chords[p1]
        end1 = chords[length + p1]
        start2 = chords[p2]
        end2 = chords[length + p2]
        
        # print("p1:", p1, "p2:", p2)
        
        if start2 > start1 and start2 < end1 or end2 > start1 and end2 < end1:
            intersections += 1
        
        if p2 < length - 1:
            p2 += 1
        else:
            p1 += 1
            p2 = p1+1
       
    return intersections
    
    
# chords = [(0.78, 1.47, 1.77, 3.92, 4, 4.1, 7.2, 8, 9, 10), ('s1', 's2', 's3', 's4', 'e1', 'e2', 'e3', 'e4')]
# chords = [(1, 3.2, 6, 3, 5, 9), ('s1', 's2', 's3', 'e1', 'e2', 'e3')]
# chords = [(1, 4, 5, 3, 6, 7), ('s1', 's2', 's3', 'e1', 'e2', 'e3')]
chords = [(0.78, 1.47, 1.77, 3.92), ('s1', 's2', 'e1', 'e2')]
try:
    # Calculate the result
    result = count_intersections(chords)
    print(f"Number of intersections: {result}")

except Exception as e:
    print(f"Error: {e}")
    result = None
