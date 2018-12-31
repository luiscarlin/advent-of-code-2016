# Advent of Code 2016

## Get Started

```bash
# setup python environment
virtualenv -p python3 .py3env && source .py3env/bin/activate && pip install -r requirements.txt

# set some env vars
cat <<EOF >.env
COOKIE=your aoc cookie
YEAR=what year of aoc you want
EOF

# get day input for day 1 (or any other day)
python ./in.py 1 > 1.in
```
