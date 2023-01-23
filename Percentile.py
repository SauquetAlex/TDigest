import json
from tdigest import TDigest

# open json file
with open("output.json", "r") as infile:
    data = json.load(infile)

# load data into TDigest
digest = TDigest()
digest.update_from_dict(data)

print("Do you want to find percentile, cdf, or a trimmed mean?")
type = input()
match type:
    case "percentile":
        print("Choose the percentile to find (0-100):")
        percentile = float(input())
        if percentile > 100 or percentile < 0:
            print("Invalid input")
            exit(1)
        print(f"Percentile: {digest.percentile(percentile)}")
    case "cdf":
        print("Choose the value to find cdf:")
        cdf = float(input())
        print(f"CDF: {digest.cdf(cdf)}")
    case "trimmed mean":
        print("Choose the lower percentile:")
        lower = float(input())
        if lower > 100 or lower < 0:
            print("Invalid input")
            exit(1)
        print("Choose the upper percentile:")
        upper = float(input())
        if upper > 100 or upper < 0:
            print("Invalid input")
            exit(1)
        print(f"Trimmed mean: {digest.trimmed_mean(lower, upper)}")
    case default:
        print("Invalid input")
        exit(1)


