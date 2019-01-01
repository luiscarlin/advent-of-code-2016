keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 5
row = 1
col = 1

digits = ''

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

    if next_col < 0 or next_row < 0 or next_col > 2 or next_row > 2:
      continue

    row, col = next_row, next_col

  digits += str(keypad[row][col])

print('part 1', digits)
