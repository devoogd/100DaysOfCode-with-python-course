import csv, random

rolls = "Rock Gun Lightning Devil Dragon Water Air Paper Sponge Wolf Tree Human Snake Scissors Fire".split()

def read_rolls():
    outcome_dict = {}
    with open('battle-table.csv') as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            name = row['Attacker']
            del row['Attacker']
            #del row[name]
            outcome_dict[name] = row
    return outcome_dict

my_dict = read_rolls()

my_roll =''
while my_roll != 'quit':
    my_roll = input('Your roll: ')
    their_roll = random.choice(rolls)
    if my_roll not in rolls:
        print('Invallid roll')
        continue
    outcome = my_dict[my_roll][their_roll]
    print(f'{my_roll} vs {their_roll}: you {outcome}')