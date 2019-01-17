'''
- 50 pixels wide and 6 pixels tall
- start off


- rect AxB turns on all of the pixels in a rectangle at the top-left of the screen which is A wide and B tall.
- rotate row y=A by B shifts all of the pixels in row A (0 is the top row) right by B pixels. Pixels that would fall off the right end appear at the left end of the row.
- rotate column x=A by B shifts all of the pixels in column A (0 is the left column) down by B pixels. Pixels that would fall off the bottom appear at the top of the column.
'''

screen = [['.'] * 6 for i in range(50)]


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
      break

show_screen()
