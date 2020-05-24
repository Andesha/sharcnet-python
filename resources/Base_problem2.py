import sys
program = sys.argv[0]
threshold = sys.argv[1]
outfn = sys.argv[2]
welcome_msg = 'Welcome to {}. Your threshold is {} an the outputfile is {}'
print(welcome_msg.format(program, threshold, outfn))
with open('frequent_terms.csv') as infile:
      text = [line.strip().split(',') for line in infile]
with open(outfn, 'w') as outfile:
    for index, entry in enumerate(text):
        if index == 0:
            line = '{}\n'.format(','.join(entry))
            outfile.write(line)
        elif float(entry[1]) >= threshold:
            line = '{}\n'.format(','.join(entry))
            outfile.write(line)
