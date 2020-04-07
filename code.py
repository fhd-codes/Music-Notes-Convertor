
#   C:/Users/fhd11/Desktop/abc.txt

txtfile = input("Enter the file path: ")
file1 = open(txtfile, 'r')
Lines = file1.readlines()       # reading all the lines of the file
file2list = []                    # empty list that will have the lines stored later

#   stripping and storing the lines in the list
for line in Lines:
    file2list.append(line.strip())

print(file2list)
print(len(file2list))
#   Defining English and Classical versions of music notes
EngNotes=['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
Notes=['Sa', 'Re*', 'Re', 'Ga*', 'Ga', 'Ma', 'Pa*', 'Pa', 'Dha*', 'Dha', 'Ni*', 'Ni']

#   Asking to input the musical note to flute 'Sa'
FluteSa = input("Enter the note name: ")

#   finding its index from list EngNotes
n=EngNotes.index(FluteSa)
print("Index of Sa in EngNotes: " + str(n))

for i in range (len(file2list)):
    aa=EngNotes.index(file2list[i])
    # print(file2list[i])

    # this subtraction will map the Flute Sa note to Classical Notes list index 0 = 'Sa'
    mapindex = aa-n

    # the following algo will map all other notes
    if (mapindex < 0):
        mapped = Notes[len(EngNotes) + mapindex]
    else:
        mapped = Notes[mapindex]

    print(file2list[i] + "\t" + mapped)
