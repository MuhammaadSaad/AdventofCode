data=open("input.txt").read()
locks = [
    
]

keys = [
   
]
for line in data.split('\n\n'):
    k=line.split('\n')
    if "#####" in k[0]:
        locks.append(k)
    else:
        keys.append(k)
    #blocks.append(k)
    


def parse_heights(schematic, lock=True):
    """
    Converts a schematic into a list of heights.
    For locks: count from top down (# to .).
    For keys: count from bottom up (# to .).
    """
    num_columns = len(schematic[0])
    heights = [0] * num_columns
    max_height = len(schematic)
    
    for col in range(num_columns):
        if lock:
            # For locks, count '#' from the top
            heights[col] = sum(1 for row in schematic if row[col] == '#')
        else:
            # For keys, count '#' from the bottom
            heights[col] = sum(1 for row in reversed(schematic) if row[col] == '#')
    
    return heights

# Parse locks and keys
lock_heights = [parse_heights(lock, lock=True) for lock in locks]
key_heights = [parse_heights(key, lock=False) for key in keys]

# Define the schematic height (number of rows in each schematic)
schematic_height = len(locks[0])

# Function to check if a lock and key fit together
def fits(lock, key, max_height):
    return all(lock[i] + key[i] <= max_height for i in range(len(lock)))

# Count valid lock/key pairs
valid_pairs = 0
for lock in lock_heights:
    for key in key_heights:
        if fits(lock, key, schematic_height):
            valid_pairs += 1

print(valid_pairs)