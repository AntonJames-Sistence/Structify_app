def count_intersections(chords):
    lines = []
    result = 0
    length = int(len(chords[0]) / 2)
    
    for i in range(length):
        lines.append([chords[0][i], chords[0][length + i]])

    print(lines)
        
    p1 = 0
    p2 = 1
    while p1 < len(lines) - 1:
        s1 = lines[p1][0]
        e1 = lines[p1][1]
        s2 = lines[p2][0]
        e2 = lines[p2][1]
        
        print("p1:", p1, "p2:", p2)
        
        if s2 > s1 and s2 < e1 or e2 > s1 and e2 < e1:
            result += 1
        
        if p2 < len(lines) - 1:
            p2 += 1
        else:
            p1 += 1
            p2 = p1+1
       
        
    return result
    
    
# chords = [(0.78, 1.47, 1.77, 3.92, 4, 4.1, 7.2, 8, 9, 10), ('s1', 's2', 's3', 's4', 'e1', 'e2', 'e3', 'e4')]
# chords = [(1, 3.2, 6, 3, 5, 9), ('s1', 's2', 's3', 's4', 'e1', 'e2', 'e3', 'e4')]
# chords = [(1, 4, 5, 3, 6, 7), ('s1', 's2', 's3', 's4', 'e1', 'e2', 'e3', 'e4')]
# chords = [(0.78, 1.47, 1.77, 3.92), ('s1', 's2', 'e1', 'e2')]
result = count_intersections(chords)
print("Number of intersections:", result)
