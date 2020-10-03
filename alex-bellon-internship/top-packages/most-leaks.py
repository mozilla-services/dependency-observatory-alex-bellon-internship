import json, pprint


def main():
    results = getEmails("500")
    output = open("output/most-leaks.json", "w")
    output.write(json.dumps(results))

def getEmails(numPackages):
    cargo = json.loads(
        open(
            "output/top-" + numPackages + "/cargo-top-" + numPackages + "-results.json",
            "r",
        ).read()
    )
    npm = json.loads(
        open(
            "output/top-" + numPackages + "/npm-top-" + numPackages + "-results.json",
            "r",
        ).read()
    )
    pypi = json.loads(
        open(
            "output/top-" + numPackages + "/pypi-top-" + numPackages + "-results.json",
            "r",
        ).read()
    )

    totalUniqueEmails = dict()
    cargoUniqueEmails = dict()
    npmUniqueEmails = dict()
    pypiUniqueEmails = dict()

    for package in cargo:
        emails = package["leaks"].keys()
        for email in emails:
            totalUniqueEmails[email] = package["leaks"][email]["leakNum"]
            cargoUniqueEmails[email] = package["leaks"][email]["leakNum"]

    for package in npm:
        emails = package["leaks"].keys()
        for email in emails:
            totalUniqueEmails[email] = package["leaks"][email]["leakNum"]
            npmUniqueEmails[email] = package["leaks"][email]["leakNum"]

    for package in pypi:
        emails = package["leaks"].keys()
        for email in emails:
            totalUniqueEmails[email] = package["leaks"][email]["leakNum"]
            pypiUniqueEmails[email] = package["leaks"][email]["leakNum"]

    sortedTotalEmails = {
        email: leaks
        for email, leaks in sorted(
            totalUniqueEmails.items(), key=lambda x: x[1], reverse=True
        )
    }
    sortedCargoEmails = {
        email: leaks
        for email, leaks in sorted(
            cargoUniqueEmails.items(), key=lambda x: x[1], reverse=True
        )
    }
    sortedNpmEmails = {
        email: leaks
        for email, leaks in sorted(
            npmUniqueEmails.items(), key=lambda x: x[1], reverse=True
        )
    }
    sortedPypiEmails = {
        email: leaks
        for email, leaks in sorted(
            pypiUniqueEmails.items(), key=lambda x: x[1], reverse=True
        )
    }

    cargoResult = sortedCargoEmails
    npmResult = sortedNpmEmails
    pypiResult = sortedPypiEmails
    totalResult = sortedTotalEmails

    return {
        "cargo": cargoResult,
        "npm": npmResult,
        "pypi": pypiResult,
        "total": totalResult,
    }

def categorizeEmails(dict):
    gmail = list()
    edu = list()
    gov = list()
    other = list()
    leaks = 0

    for email in dict.keys():
        if dict[email]:  # Has at least one leak
            if "gmail.com" in email:
                gmail.append(email)
            elif ".edu" in email:
                edu.append(email)
            elif ".gov" in email:
                gov.append(email)
            else:
                other.append(email)
            leaks += 1

    result = {
        "users": len(dict),
        "users-with-leaks": leaks,
        "gmail": gmail,
        "edu": edu,
        "gov": gov,
        "other": other,
    }

    return result

main()
