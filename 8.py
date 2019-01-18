screen = [['.'] * 6 for i in range(50)]

def count_lit():
  count = 0
  for row in range(6):
    for col in range(50):
      if screen[col][row] == '#':
        count += 1
  return count

def rotate_col(col, offset):
  l = []
  for row in range(6):
    l.append(screen[col][row])

  new_l = rotate(l, offset)

  for row in range(6):
    screen[col][row] = new_l[row]

def rotate_row(row, offset):
  l = []
  for col in range(50):
    l.append(screen[col][row])

  new_l = rotate(l, offset)

  for col in range(50):
    screen[col][row] = new_l[col]

def rotate(l, n):
  n = n % len(l)
  return l[-n:] + l[:-n]

def show_screen():
  for row in range(6):
    for col in range(50):
      print(screen[col][row], end = '')
    print()

def rect(w, h):
  for col in range(w):
    for row in range(h):
      screen[col][row] = '#'

for line in open('8.in'):
  if line:
    if 'rect' in line:
      w,h = list(map(int, line.split()[1].split('x')))
      rect(w, h)

    if 'rotate column' in line:
      words = line.split()
      col = int(words[2].split('=')[1])
      offset = int(words[4])
      rotate_col(col, offset)

    if 'rotate row' in line:
      words = line.split()
      row = int(words[2].split('=')[1])
      offset = int(words[4])
      rotate_row(row, offset)

print('part 1',count_lit())
show_screen()
