import sys
import csv
import cs50

if len(sys.argv) != 2:
    print("Usage: Need csv file")
    exit(1)

if sys.argv[1].endswith('.csv') == False:
    print("Usage: Need csv file")
    exit(2)



open(f"students.db","a").close()
db = cs50.SQL("sqlite:///students.db")

## open a CSV file and for each row copy it into the table of students.db

with open(sys.argv[1], newline='') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        first_name = ""
        middle_name = ""
        last_name = ""
        house = row["house"]
        birth = row["birth"]

        sep_names = row["name"].split(" ")
        first_name = sep_names[0]
        last_name = sep_names[len(sep_names)-1]

        if (len(sep_names) == 2):
            middle_name = None
        else:
            middle_name = sep_names[1]

        exist = db.execute("SELECT first FROM students WHERE first=? AND last=?", first_name, last_name)

        if exist == []:
            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                first_name, middle_name, last_name, house, int(birth))
        ##db.execute("DELETE FROM students")






