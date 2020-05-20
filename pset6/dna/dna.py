import cs50
import sys
import csv

def main():

    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    ##loading and unpacking database csv
    with open(sys.argv[1],newline='') as infile:
        reader = csv.DictReader(infile, delimiter=',')
        codis={}
        line_count=0
        for row in reader:
            codis[line_count] = row
            line_count += 1
    ##print(codis)
    ##print(codis[2])
    ##print(codis[0]["name"])

    ##load total sequence to analyze
    total_sequence = open(sys.argv[2], "r")
    content = total_sequence.read()

    #Defining the sequences and counters
    sequence_AGATC = ('A','G','A','T','C')
    sequence_AATG = ('A','A','T','G')
    sequence_TATC = ('T','A','T','C')

    count_AGATC = 0
    count_AATG = 0
    count_TATC = 0


    count_AGATC = counter_sequence(sequence_AGATC, content)
    count_AATG = counter_sequence(sequence_AATG, content)
    count_TATC = counter_sequence(sequence_TATC, content)
    sample_counters = [count_AGATC,count_AATG,count_TATC]
    ##print(count_AGATC,count_AATG,count_TATC)

    ##Find the match
    match = ""
    for person in codis:
        person_counters=[int(codis[person]["AGATC"]), int(codis[person]["AATG"]), int(codis[person]["TATC"])]
        if (sample_counters == person_counters):
            match = codis[person]["name"]
            break

    if match == "":
        print("No match")
    else:
        print(match)


##Loop for AGATC

def counter_sequence(sequence, content):
    count_sequence=0
    for i in range(0,len(content)-4,1):
        tmp = []
        for x in range(len(sequence)):
            tmp.append(content[i+x])
        tmp = tuple(tmp)
        if (tmp == sequence):
        ##if ((content[i],content[i+1],content[i+2],content[i+3],content[i+4]) == sequence_AGATC):
            streak_sequence=0
            for j in range(0,len(content)-i,len(sequence)):
                tmp = []
                for x in range(len(sequence)):
                    tmp.append(content[i+j+x])
                tmp = tuple(tmp)
                if (tmp == sequence):
                ##if ((content[i+j],content[i+j+1],content[i+j+2],content[i+j+3],content[i+j+4]) == sequence_AGATC):
                    streak_sequence += 1
                else:
                    break
            if streak_sequence > count_sequence:
                count_sequence = streak_sequence
            ##print (f"Streak Count: {streak_sequence}\t Max Count: {count_sequence}")

    ##print("Max Count Final:" + str(count_AGATC))
    return count_sequence

main()

## https://stackoverflow.com/questions/425604/best-way-to-determine-if-a-sequence-is-in-another-sequence-in-python
## https://www.ics.uci.edu/~eppstein/161/960227.html
## for Argv stuff https://www.tutorialspoint.com/python/python_command_line_arguments.htm