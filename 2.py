import copy

def get_code(start_pos, keypad_list):
  keypad = copy.deepcopy(keypad_list)

  size = len(keypad_list)
  row, col = start_pos
  code = ''

  for line in open('./2.in').read().strip().split('\n'):
    for char in line:
      next_row, next_col = row, col

      if char is 'U':
        next_row = row - 1
      elif char is 'D':
        next_row = row + 1
      elif char is 'L':
        next_col = col - 1
      elif char is 'R':
        next_col = col + 1

      if next_col < 0 or next_row < 0 or next_col > size - 1 or next_row > size - 1 or keypad[next_row][next_col] is 0:
        continue

      row, col = next_row, next_col

    code += str(keypad[row][col])

  return code

keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
code = get_code((1, 1), keypad)
print('part 1', code)

keypad = [[0, 0, 1, 0, 0], [0, 2, 3, 4, 0], [5, 6, 7, 8, 9], [0, 'A', 'B', 'C', 0], [0, 0, 'D', 0, 0]]
code = get_code((2, 0), keypad)
print('part 2', code)
