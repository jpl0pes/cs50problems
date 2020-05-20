import sys
import csv
import cs50

if len(sys.argv) != 2:
        print("Usage: Need input house")
        exit(1)

if sys.argv[1] not in ["Gryffindor","Slytherin","Ravenclaw","Hufflepuff"]:
    print("Usage: Need right house name (Gryffindor, Slytherin, Hufflepuff or Ravenclaw) after the program")
    exit(1)


open(f"students.db","a").close()
db = cs50.SQL("sqlite:///students.db")

inputhouse = sys.argv[1]

roster = db.execute("SELECT first, middle, last, birth FROM students WHERE house = ? ORDER BY last,first",inputhouse)

for row in roster:
    if (row['middle'] != None):
        print(row['first'], row['middle'], row['last'] + ", born in", row['birth'])
    else:
        print(row['first'], row['last'] + ", born in", row['birth'])
