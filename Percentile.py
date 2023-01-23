import json
from tdigest import TDigest

# open json file
with open("output.json", "r") as infile:
    data = json.load(infile)

# load data into TDigest
digest = TDigest()
digest.update_from_dict(data)

print("Choose the percentile to find (0-100):")
percentile = int(input())
if percentile > 100 or percentile < 0:
    print("Invalid input")
    exit(1)
print(digest.percentile(percentile))
