import sys

def validate_email(line):
    line = line.strip().lower()
    if line.count('@')==1:
        return line

# argumenty to plik wejsciowy i nazwa pliku wjesciowego
if len(sys.argv)==3:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
else:
    print("Nieprawidsłowa iliość arg")

    with open(input_file) as f:
        for line in f:
            email= validate_email(line)
            print(line.lower())
            if email:
                email.add(email)

    with open (output_file, 'w') as f:
        f.write(clean)