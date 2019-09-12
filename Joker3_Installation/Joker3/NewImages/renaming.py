import os
cards = []
for x in range(2, 11):
    cards.append('n{}D'.format(x) + '.png')
    cards.append('n{}S'.format(x) + '.png')
    cards.append('n{}H'.format(x) + '.png')
    cards.append('n{}C'.format(x) + '.png')
for j in ['A', 'K', 'Q', 'J']:
    cards.append('n{}D'.format(j) + '.png')
    cards.append('n{}S'.format(j) + '.png')
    cards.append('n{}H'.format(j) + '.png')
    cards.append('n{}C'.format(j) + '.png')
for k in cards:
    print(k.lower())
    os.system('mv {} {}'.format(k[1:], k[1:].lower()))
