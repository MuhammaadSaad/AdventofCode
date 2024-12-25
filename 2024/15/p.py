def parse_map_and_commands(map_data, commands):
    """Parses the map and commands from the input."""
    warehouse = []
    robot_pos = None
    boxes = []

    for y, line in enumerate(map_data.splitlines()):
        row = list(line)
        warehouse.append(row)
        if '@' in row:
            robot_pos = (y, row.index('@'))
        for x, cell in enumerate(row):
            if cell == 'O':
                boxes.append((y, x))
    print(robot_pos)
    command_sequence = ''.join(commands.split())
    return warehouse, robot_pos, boxes, command_sequence


def move_robot_and_boxes(warehouse, robot_pos, boxes, commands):
    """Simulates the robot and box movements based on the given commands."""
    directions = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }

    def is_within_bounds(y, x):
        return 0 <= y < len(warehouse) and 0 <= x < len(warehouse[0])

    def is_empty_space(y, x):
        return is_within_bounds(y, x) and warehouse[y][x] == '.'

    def can_push_box(box_pos, direction):
        box_y, box_x = box_pos
        new_y, new_x = box_y + direction[0], box_x + direction[1]
        return is_empty_space(new_y, new_x)

    for command in commands:
        direction = directions[command]
        new_robot_y, new_robot_x = robot_pos[0] + direction[0], robot_pos[1] + direction[1]

        if is_within_bounds(new_robot_y, new_robot_x):
            if warehouse[new_robot_y][new_robot_x] == 'O':
                # Attempt to push the box
                box_y, box_x = new_robot_y, new_robot_x
                new_box_y, new_box_x = box_y + direction[0], box_x + direction[1]

                if can_push_box((box_y, box_x), direction):
                    # Move the box
                    warehouse[box_y][box_x] = '.'
                    warehouse[new_box_y][new_box_x] = 'O'
                    boxes.remove((box_y, box_x))
                    boxes.append((new_box_y, new_box_x))

                    # Move the robot
                    warehouse[robot_pos[0]][robot_pos[1]] = '.'
                    warehouse[new_robot_y][new_robot_x] = '@'
                    robot_pos = (new_robot_y, new_robot_x)

            elif warehouse[new_robot_y][new_robot_x] == '.':
                # Move the robot
                warehouse[robot_pos[0]][robot_pos[1]] = '.'
                warehouse[new_robot_y][new_robot_x] = '@'
                robot_pos = (new_robot_y, new_robot_x)

    return warehouse, boxes


def calculate_gps_sum(boxes):
    """Calculates the sum of GPS coordinates for all boxes."""
    gps_sum = 0
    for y, x in boxes:
        gps_sum += 100 * y + x
    return gps_sum


def main():
    # Input data
    
    map_data="""##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########"""

    commands="""<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""
    #data=open("input.txt").read()
    #map_data ,commands =data.split("\n\n")

    # Parse the map and commands
    warehouse, robot_pos, boxes, command_sequence = parse_map_and_commands(map_data, commands)
    print("Initial Warehouse State:")
    for row in warehouse:
        print(''.join(row))
    # Simulate the robot and box movements
    warehouse, boxes = move_robot_and_boxes(warehouse, robot_pos, boxes, command_sequence)
    
    # Calculate the GPS sum of the boxes
    gps_sum = calculate_gps_sum(boxes)

    print("Final Warehouse State:")
    for row in warehouse:
        print(''.join(row))
    print("\nSum of GPS coordinates of boxes:", gps_sum)


if __name__ == "__main__":
    main()