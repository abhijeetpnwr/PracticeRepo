
a= open(r"C:\Users\Dell 9\Desktop\correct\agpase_output.txt")
b = open(r"C:\Users\Dell 9\Desktop\blast_est_agpase-l.txt")
e = open("C:\Users\Dell 9\Desktop\est.txt", "w")


e.write("SNo.,Name of Gene,Sequences producing significant alignments,Position of nucleotide on reference gene, position corresponding to reference gene on EST, Original reference base,  Nucleotide corresponding to Query Sequence present on EST, \n")
count = 0
position_list = []



gene_id=""

for line in a:
    if count == 0:
        count = count + 1
    else:
        line = line.split("\t")

        gene_id = line[1]
        position = line[5]
        if not position in sorted(position_list):
            position_list.append(position)

count = 0

processbelow = False

toprocess = []

tocut = 0
elsecheck = False


gene_arr = []

totalcontent=""
firsttimecheck = False;
startforfirst = -1

seqno = 0

for line in b:

    # If starts with gi , create an array for these
    if line.startswith("  gi"):
        gene_arr.append(line)


    #if line starts with query 
    if line.startswith ("Query_"):


    		#############################################################################
        

            if firsttimecheck == True: #Don't execute very first time.Execute it for the other Query_lines.When first line Query_1  1     ATGTCATCGATGCAGTTCAGCAGCGTGCTGCCCCTGGAGGGCAAAGCGTGCATCTCCCCC  60 comes ,this part will not execute

                for items in toprocess: #Toprocess 
                    print "Processing :",items
                    item = int(items)
                    linearr = totalcontent.split("\n")
                    
                    tocutfrombehind = -1
                    for eachline in linearr:
                        if len(eachline.strip())>0:

                            spliterr = []
                            for elem in eachline.split(" "):
                                if len(elem.strip())>0:
                                    spliterr.append(elem)

                            print spliterr
                            tofetch = spliterr[0]


#towriteinfile = str(count)+","+gene_id+","+header+","+ items+","++"," +  +","+letter +"\n"
                            print spliterr



                            if tofetch.startswith("Query"):
                                print "this is line with query_no format , skipping it"
                                seq = spliterr[2]
                                #reference_letter = seq[item-startforfirst:item-startforfirst+1]
                                tocutfrombehind = len(seq)-(item-startforfirst)
                                #print "In if , Reference letter :",reference_letter
                                reference_letter = seq[len(seq)-tocutfrombehind:len(seq)-tocutfrombehind+1]
                                #print "In if ,should be same as refernce letter ",check


                            else:
                                seqno = seqno +1
                                header = gene_arr[int(tofetch)-1].strip().split("  ")[0]
                                estpos = item-startforfirst+int(spliterr[1])
                                seq = spliterr[2]
                                #letter = seq[item-startforfirst:item-startforfirst+1]

                                letter = seq[len(seq)-tocutfrombehind:len(seq)-tocutfrombehind+1]

                                if len(letter.strip())<=0:
                                    letter = seq[item-startforfirst:item-startforfirst+1]
                                if letter.strip() == "":
                                    pos = " "
                                else:
                                    pos = str(estpos)
                                towrite = str(seqno)+","+gene_id+","+header+","+str(items)+","+pos+","+reference_letter+","+letter+"\n"
                                print towrite
                                e.write(towrite)

            # This part only exectues only if this is not first Query_ part .Means in ex. file it will not execute for ---> Query_1  1     ATGTCATCGATGCAGTTCAGCAGCGTGCTGCCCCTGGAGGGCAAAGCGTGCATCTCCCCC  60

            ##########################################################################3


                            #print letter

            #Will execute everyttime. Even for the first one

            totalcontent="" #temp , which will have conatenated lines starting below Query_1 to next Query_ part.Means  part which should ebe processed

        

            totalcontent = totalcontent+line #Add it to content 


            # Supppose here reaches line : Query_1  1     ATGTCATCGATGCAGTTCAGCAGCGTGCTGCCCCTGGAGGGCAAAGCGTGCATCTCCCCC  60
        
            toprocess = []
            processbelow = True #Sets processbelwo flag to true.
            count = count + 1

            splitline = line.split()
            sequence_number = splitline[0] 
           
            start = int(splitline[1]) #fetches start from line. start = 1 for --> Query_1  1     ATGTCATCGATGCAGTTCAGCAGCGTGCTGCCCCTGGAGGGCAAAGCGTGCATCTCCCCC  60
            startforfirst = start
            end  = int(splitline[3]) #fetches end from line ,End = 60 for -->Query_1  1     ATGTCATCGATGCAGTTCAGCAGCGTGCTGCCCCTGGAGGGCAAAGCGTGCATCTCCCCC  60
            sequence = splitline[2] #fetches sequence pattern from it ,Sequence pattern ATGTCATCGATGCAGTTCAGCAGCGTGCTGCCCCTGGAGGGCAAAGCGTGCATCTCCCCC for -->ATGTCATCGATGCAGTTCAGCAGCGTGCTGCCCCTGGAGGGCAAAGCGTGCATCTCCCCC 

            queryline = line

            #------------------------------------------------------------ #

            for items in position_list:  # Iterating position list , contains all Polymorphic Nucleotide position on reference gene from a file
                item = int(items)
                if item in range(start,end):  # if  this ploy. Nucleotide pos. is in between start(In ex. : 0) and end position(In ex. 60 )  
                    toprocess.append(item) #Add it to toprocess array , 

             # So when this for loop will end , toprocess conatins all items between start (In ex. 0) and end (in ex. 60) which should be processed for : Query_1  1     ATGTCATCGATGCAGTTCAGCAGCGTGCTGCCCCTGGAGGGCAAAGCGTGCATCTCCCCC  60 to next query 


            # --------------------------------------------------------------#

    else:
    	#If line does's start with gi or query , means it is line between Query_ to next Query_ . So keep concatening them 

        firsttimecheck = True
        if processbelow==True  and len(toprocess)>0 and "." in line:
            totalcontent=totalcontent+line



print len(gene_arr)





