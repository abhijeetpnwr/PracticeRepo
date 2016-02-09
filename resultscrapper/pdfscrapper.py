import os 

nameoffile = "result.pdf"

print " ################### Will convert pdf to txt file #######################"

#os.system("python pdfminer-20140328/tools/pdf2txt.py  -o myOutput.txt "+nameoffile)

print " ############## Text  conversion done, now willprocess text file ##########"

result_txt = open("myOutput.txt","r")

resultfile = open("output.txt","w")

def page2line(result_txt):
	filecontent = ""	
	#concating file as a single string
	pagecount = 0

	for line in result_txt:
		filecontent = filecontent+"\n"+line
	beg = 0
	tofindstring = "Delhi Technological University"
	ispresent = True
	initialindex = filecontent.find(tofindstring,beg,len(filecontent))
	
	pagecontentmap = {}

	while True:
		nextindex = filecontent.find(tofindstring,initialindex+len(tofindstring),len(filecontent))
		
		if nextindex == -1:
			pagecontent = filecontent[initialindex:]
			pagecount = pagecount+1

			pagecontentmap[pagecount]=pagecontent

			break

		else:
			pagecontent = filecontent[initialindex:nextindex]
			pagecount = pagecount+1
			pagecontentmap[pagecount]=pagecontent
			initialindex = nextindex
			
		
	return pagecontentmap		

####################################################333
pagemap = page2line(result_txt)

toparse_pageno= []

for i in range (1,len(pagemap)+1):
	contenttoparse = pagemap[i]

	Branch_index = contenttoparse.find("Computer Engineering")
	
	if Branch_index>=0:
		toparse_pageno.append(i)

###############################################################

for item in toparse_pageno:
	rollno = []
	percentage = []
	content = pagemap[item]
	start_index = content.find("Roll No.")
	last_index = content.find("Any discrepancy in the result in")
	tofinecontent = content[start_index:last_index]

	linearr = tofinecontent.split("\n")
	
	for line in linearr:
		if len(line)>0 and line!="":
			linespilt = line.split()
			if len(linespilt)>=2 and linespilt[0].isdigit():
				rollno.append(line)
			else:
				if line.find(".")>=0 and line.split(".")[0].isdigit():
					percentage.append(line.split()[0]) 

	for i in range (0,len(rollno),1):
		resultfile.write(rollno[i]+"\t"+percentage[i]+"\n")

resultfile.close()
result_txt.close()

			


	

	
	

