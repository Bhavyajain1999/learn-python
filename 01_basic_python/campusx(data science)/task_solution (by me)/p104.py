# write code here
input_file = "sample.txt"
output_file = "sample_reversed.txt"

def reverse_lines(infilename, outfilename):
    with open(infilename, 'r') as infile, open(outfilename, "w") as outfile:
        for one_line in infile:
            outfile.write(one_line.rstrip()[::-1]+"\n")
reverse_lines(input_file, output_file)