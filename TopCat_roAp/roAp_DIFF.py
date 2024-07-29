import csv

with open('15MON_A0_FOV.csv', 'r') as csv1:
    import1 = csv1.readlines()
with open('Possible_roAp.csv', 'r') as csv2:
    import2 = csv2.readlines()
with open('poss_roAp.csv', 'w') as outFile:
    for row in import2:
        if row not in import1:
            outFile.write(row)