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
    sorted_chords = []
    
    my_dict = {str(i): [] for i in range(1, length  + 1)}
    
    for i in range(0, len(values)):
        num = values[i][1]
        char = values[i][0]
        if char == 's':
            my_dict[num].insert(0, chords[i])
        else:
            my_dict[num].append(chords[i])
            
    for key, value in my_dict.items():
        sorted_chords.append(value)
    
    # print(result)
    
    return count_intersections(sorted_chords)
