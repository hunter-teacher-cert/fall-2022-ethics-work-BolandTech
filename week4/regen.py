import re


def find_name(line):

		pattern = r"([A-Z][a-z]+ [A-Z][a-z]+(?: [A-Z][a-z]+)?)"
  	result = re.findall(pattern, line)

    # Names of the format Ms. Thomas
    pattern = r'(?:Mrs\.|M[rs]\.|Dr\.|Miss) [A-Z][a-z]+'
    result = result + re.findall(pattern, line)
		
    # pattern = r'(?:Ms\.|Miss|Mrs\.|Dr\.|Mr\.) [a-zA-Z]+'
    # result = result + re.findall(pattern,line)
    # return result

f = open("names.txt")
for line in f.readlines():
    #print(line)
    result = find_name(line)
    if (len(result)>0):
        print(result)



##############################Try Below #################

			# r"[A-Z][a-z]+ [A-Z][a-z]+"
   #  # pattern = r"([A-Z][a-z]+ ){1,2}[A-Z][a-z]+"
   #  pattern = r'a(bc)?d'
   #  result = re.findall(pattern, line)

   #  pattern = r'(?:Mrs\.|Mr\.|Dr\.) [A-Z][a-z]+'
   #  result = result + re.findall(pattern, line)

   #  pattern = r'(Dr\. [A-Z]\. [A-Z][a-z]+|[A-Z]\. [A-Z][a-z]+)'
   #  result = result + re.findall(pattern, line)

   #  # pattern = r"[A-Z][a-z]+ [A-Z][a-z]+ [A-Z][a-z]+"
   #  # result = result + re.findall(pattern,line)

   #  return result


f = open("names.txt")
for line in f.readlines():
    # print(line)
    result = find_name(line)
    if (len(result) > 0):
        print(result)