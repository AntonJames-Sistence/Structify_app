def count_intersections(chords):
    intersections = 0
    length = len(chords)
        
    p1 = 0
    p2 = 1
    while p1 < length - 1:
        start1 = chords[p1][0]
        end1 = chords[p1][1]
        start2 = chords[p2][0]
        end2 = chords[p2][1]
        
        if start2 > start1 and start2 < end1 or end2 > start1 and end2 < end1:
            intersections += 1
        
        if p2 < length - 1:
            p2 += 1
        else:
            p1 += 1
            p2 = p1+1
       
    return f"Number of intersections: {intersections}"
    
def get_chords(input):
    chords = input[0]
    values = input[1]
    length = int(len(input[0]) / 2)
    result = []
    
    my_dict = {str(i): [] for i in range(1, length  + 1)}
    
    for i in range(0, len(values)):
        num = values[i][1]
        char = values[i][0]
        if char == 's':
            my_dict[num].insert(0, chords[i])
        else:
            my_dict[num].append(chords[i])
            
    for key, value in my_dict.items():
        result.append(value)
    
    # print(result)
    
    return result
    
# chords = [(0.78, 1.47, 1.77, 3.92, 4, 4.1, 7.2, 8, 9, 10), ('s1', 'e1', 's2', 'e2', 's3', 's4', 'e3', 'e4', 's5', 'e5')]
# chords = [(1, 3.2, 6, 3, 5, 9), ('s1', 's2', 's3', 'e1', 'e2', 'e3')]
# chords = [(1, 4, 5, 3, 6, 7), ('s1', 's2', 's3', 'e1', 'e2', 'e3')]
# chords = [(0.78, 1.47, 1.77, 3.92), ('s1', 's2', 'e1', 'e2')]
chords = [(0.9, 1.3, 1.70, 2.92), ('s1', 'e1', 's2', 'e2')]
try:
    # Calculate the result
    sort_chords = get_chords(chords)
    result = count_intersections(sort_chords)
    print(result)

except Exception as e:
    print(f"Error: {e}")
    result = None
