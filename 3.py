from collections import defaultdict

def is_triangle(side1, side2, side3):
  return not (side1 + side2 <= side3 or side1 + side3 <= side2 or side3 + side2 <= side1)

possible = 0

for line in open('3.in').read().split('\n'):
  if line:
    side1, side2, side3 = list(map(int, line.strip().split()))

    if is_triangle(side1, side2, side3):
      possible += 1
    else:
      continue

print('part 1', possible)

read_cols = [[], [], []]

for line in open('3.in').read().split('\n'):
  if line:
    col1, col2, col3 = list(map(int, line.strip().split()))
    read_cols[0].append(col1)
    read_cols[1].append(col2)
    read_cols[2].append(col3)

cols = read_cols[0] + read_cols[1] + read_cols[2]

possible = 0

for i in range(0, len(cols), 3):

  if i + 2 >= len(cols):
    break

  if is_triangle(cols[i], cols[i + 1], cols[i + 2]):
    possible += 1

print('part 2', possible)