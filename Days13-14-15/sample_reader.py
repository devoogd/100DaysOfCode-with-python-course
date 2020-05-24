import csv


def read_rolls():
    with open('battle-table.csv') as fin:
        reader = csv.DictReader(fin)
        n = 1
        for row in reader:
            print(row)
            read_roll(row)



def read_roll(row: dict):
    name = row['Attacker']
    del row['Attacker']
    del row[name]

    print("Roll: {}".format(name))
    for k in row.keys():
        can_defeat = row[k].strip().lower() == 'win'
        print(" * {} will defeat {}? {}".format(name, k, can_defeat))

    print()


read_rolls()
