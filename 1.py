def find_last_position(quit_on_duplicate=False):
  cur_dir = 0

  # up, right, down, left
  dr = [-1, 0, 1, 0]
  dc = [0, 1, 0, -1]

  row, col = 0, 0

  instructions = open('./1.in').read().strip().split(',')
  coords = []

  for instruction in instructions:
    instruction = instruction.strip()
    direction, blocks = instruction[0], int(instruction[1:])

    if direction is 'L':
      cur_dir = (cur_dir + 3) % 4
    else:
      cur_dir = (cur_dir + 1) % 4

    for _ in range(blocks):
      row = row + dr[cur_dir]
      col = col + dc[cur_dir]

      if (row, col) in coords and quit_on_duplicate:
        return (row, col)

      coords.append((row, col))

  return (row, col)

def get_distance(source, destination):
  return abs(source[0] - destination[0]) + abs(source[1] - destination[1])

last_position = find_last_position()
print('part 1', get_distance((0, 0), last_position))

first_repeated = find_last_position(quit_on_duplicate = True)
print('part 2', get_distance((0, 0), first_repeated))
