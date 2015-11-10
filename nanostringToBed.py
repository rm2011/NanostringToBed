import sys,os,string,math

print "Usage: python nanostringToBed.py miRBase21.gff3 NanoStringData.txt Out.Rep1.bed Out.Rep2.bed"

chrcoordfile = open(sys.argv[1])
nstringfile = open(sys.argv[2])

chrcoorddict = {}
for line in chrcoordfile:
	if line[0] == "#":
		continue
	splitz = line.strip().split("\t")
	temp = splitz[8].split("ID=")
	temp1 = temp[1].split(";")
	if temp1[0] in chrcoorddict.keys():
		chrcoorddict[temp1[0]].append([splitz[0], splitz[3], splitz[4], splitz[6]])
	else:
		chrcoorddict[temp1[0]] = [[splitz[0], splitz[3], splitz[4], splitz[6]]]
chrcoordfile.close()

outfile = open(sys.argv[3],'w')
outfile2 = open(sys.argv[4],'w')

count = 0
chrkeys = chrcoorddict.keys()
for line in nstringfile:
	if count == 0:
		count+=1
		continue
	splitz = line.strip().split("\t")
	gene = splitz[1]
	if gene in chrkeys:
		coord = chrcoorddict[gene]
		for coor in coord:
			outfile.write(coor[0]+"\t"+coor[1]+"\t"+coor[2]+"\t"+gene+"\t"+str(int(round(50*math.log(float(splitz[2]),2))))+"\t"+coor[3]+"\t"+splitz[0]+"\t"+splitz[2]+"\n")
			outfile2.write(coor[0]+"\t"+coor[1]+"\t"+coor[2]+"\t"+gene+"\t"+str(int(round(50*math.log(float(splitz[3]),2))))+"\t"+coor[3]+"\t"+splitz[0]+"\t"+splitz[3]+"\n")

outfile.close()
outfile2.close()
nstringfile.close()
print "Done"

