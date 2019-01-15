'''
- 50 pixels wide and 6 pixels tall
- start off


- rect AxB turns on all of the pixels in a rectangle at the top-left of the screen which is A wide and B tall.
- rotate row y=A by B shifts all of the pixels in row A (0 is the top row) right by B pixels. Pixels that would fall off the right end appear at the left end of the row.
- rotate column x=A by B shifts all of the pixels in column A (0 is the left column) down by B pixels. Pixels that would fall off the bottom appear at the top of the column.
'''

for line in open('8.in'):
  if line:
    if 'rect' in line:
