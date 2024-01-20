def count_intersections(chords):
    events = []
    
    # Create events for each chord start and end point
    for i in range(len(chords[0])):
        events.append((chords[0][i], 'start', chords[1][i]))
        events.append((chords[0][i], 'end', chords[1][i]))
    
    # Adjust sorting based on radian measure, considering the circular nature
    events.sort(key=lambda x: (x[0] + 2 * pi) % (2 * pi))

    intersections = 0
    active_chords = set()

    for event in events:
        radian, event_type, identifier = event
        
        if event_type == 'start':
            active_chords.add(identifier)
        else:
            if identifier in active_chords:
                active_chords.remove(identifier)
                intersections += len(active_chords)

    return intersections

# Assuming pi is available from the math module
from math import pi

# Example usage
chords = [(0.78, 1.47, 1.77, 3.92), ('s1', 's2', 'e1', 'e2')]
result = count_intersections(chords)
print("Number of intersections:", result)
