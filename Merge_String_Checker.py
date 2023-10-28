"""
This algorithm checks if a given string, s, can be formed from two other strings, part1 and part2.
"""
def is_merge(s, part1, part2):
    
    
    
    s = list(s)
    
    extra_chars = []
    added_chars = []

    
    for i in range (len(part1)):
        if part1[i] in s:
            added_chars.append(f"{part1[i]}")
            s.remove(f"{part1[i]}")
        else:
            extra_chars.append(part1[i])

    for i in range (len(part2)):
        if part2[i] in s:
            added_chars.append(f"{part2[i]}")
            s.remove(f"{part2[i]}")
        else:
            extra_chars.append(part2[i])
            
            
    if len(s) == 0 and (len(extra_chars) == 0):
        return True
    else:
        return False


