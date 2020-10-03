import json, pprint


def main():
    # numPackages = ["50", "100", "250", "500"]
    numPackages = ["500"]
    results = dict()
    for num in numPackages:
        results = getEmails(num)

    output = open("output/packages-per-maintainer.json", "w")
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
            if email in totalUniqueEmails:
                totalUniqueEmails[email] = totalUniqueEmails[email] + 1
            else:
                totalUniqueEmails[email] = 1

            if email in cargoUniqueEmails:
                cargoUniqueEmails[email] = cargoUniqueEmails[email] + 1
            else:
                cargoUniqueEmails[email] = 1

    for package in npm:
        emails = package["leaks"].keys()
        for email in emails:
            if email in totalUniqueEmails:
                totalUniqueEmails[email] = totalUniqueEmails[email] + 1
            else:
                totalUniqueEmails[email] = 1

            if email in npmUniqueEmails:
                npmUniqueEmails[email] = npmUniqueEmails[email] + 1
            else:
                npmUniqueEmails[email] = 1

    for package in pypi:
        emails = package["leaks"].keys()
        for email in emails:
            if email in totalUniqueEmails:
                totalUniqueEmails[email] = totalUniqueEmails[email] + 1
            else:
                totalUniqueEmails[email] = 1

            if email in pypiUniqueEmails:
                pypiUniqueEmails[email] = pypiUniqueEmails[email] + 1
            else:
                pypiUniqueEmails[email] = 1

    sortedTotalEmails = {
        email: packages
        for email, packages in sorted(
            totalUniqueEmails.items(), key=lambda x: x[1], reverse=True
        )
    }
    sortedCargoEmails = {
        email: packages
        for email, packages in sorted(
            cargoUniqueEmails.items(), key=lambda x: x[1], reverse=True
        )
    }
    sortedNpmEmails = {
        email: packages
        for email, packages in sorted(
            npmUniqueEmails.items(), key=lambda x: x[1], reverse=True
        )
    }
    sortedPypiEmails = {
        email: packages
        for email, packages in sorted(
            pypiUniqueEmails.items(), key=lambda x: x[1], reverse=True
        )
    }

    cargoResult = sortedCargoEmails
    npmResult = sortedNpmEmails
    pypiResult = sortedPypiEmails
    totalResult = sortedTotalEmails

    print(totalResult)

    return {
        "cargo": cargoResult,
        "npm": npmResult,
        "pypi": pypiResult,
        "total": totalResult,
    }


def printResults(data):
    print(data)

main()
