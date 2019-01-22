# Advent of Code 2016

My solutions to Advent of Code 2016.

## Get Started

```bash
# setup python environment
virtualenv -p python3 .py3env && source .py3env/bin/activate && pip install -r requirements.txt

# set some env vars
cat <<EOF >.env
COOKIE=your AoC cookie
YEAR=year of AoC
EOF

# get input for day 1 (or any other day)
python ./get_input.py 1 > 1.in
```
