"""
Mailroom program to tidy up.

Mailroom Madness

A program to to be efficient in the mailroom.
"""


database = {
    "John Doe": [23.55, 244.04],
    "Tom Fitch": [324.22]
}


def choose_donor():
    while True:
        name = raw_input("Type in a donor's name or 'list' for list donors")
        if name == 'quit':
            return
        elif name == 'list':
            print("donor database\n")
            print database.keys()
        elif name in database:
            return name
        elif name not in database:
            database[name] = []
            return name


def donation_amount(donor_name):
    donation = 0.0
    while True:
        donation = raw_input("Donation amount? (number only)")
        if donation == 'quit':
            return
        else:
            for donor in database:
                if donor == database:
                    database[donor].append[donation]
                    pass
    if donor not in database:
        database[donor] = []
    database[donor].append(donation)

    print "Thank you %s for the donatio of %s" % (donor, donation)


def print_report():
    report = []
    for (donor, donation) in database.items():
        total_amount = sum(donation)
        num_donation = len(donation)
        avg_donation = total_amount / num_donation
        report.append((donor, total_amount, num_donation, avg_donation))
    print report

if __name__ == "__main__":
    while True:
        option = raw_input(" Press 1 for Send Thank You, 2 for Create Report, or 'quit' to quit anytime")
        if option is '1':
            donor = choose_donor()
            donation = donation_amount(donor)
        elif option is '2':
            print_report()
        elif option == 'quit':
            running = False
