processed_lines = []

for line in open('9.in'):
  if line:
    processing_pattern = False
    new_line = ''
    for idx, char in enumerate(line):
      pattern_found = False

      if line[idx] == '(' and line[idx+1].isnumeric() and line[idx+2] == 'x' and line[idx+3].isnumeric() and line[idx + 4] == ')':
        pattern_found = True
        num_chars = int(line[idx+1])
        repeat_times = int(line[idx+3])
      else:
        new_line += char

    processed_lines.append(new_line)

