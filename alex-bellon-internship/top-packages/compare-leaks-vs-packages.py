import pprint, json

leaks = json.loads(open("output/most-leaks.json", "r").read())
packages = json.loads(open("output/packages-per-maintainer.json").read())

totalLeaks = leaks["total"]
totalPackages = packages["total"]

num = 50

topLeaks = set(list(totalLeaks.keys())[:num])
topPackages = set(list(totalPackages.keys())[:num])

both = topLeaks.intersection(topPackages)
print(both)
