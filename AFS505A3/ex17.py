from sys import argv
from os.path import exists

script, from_file, to_file = argv
print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print(f"Ready, hit RETURN to continue, CTRL-C to abort.")

out_file = open(to_file, 'w')
outfile.write(data)

print("Alright, all done.")

out_file.close()
in_file.close()

#study to put it into one line
 print(f"The input file is {len(indata)} bytes long", "Does the output file exist? {exists(to_file)}", "Ready, hit RETURN ")

 man cat
