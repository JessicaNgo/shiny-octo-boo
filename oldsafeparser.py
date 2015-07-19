
with open("gutbugs.txt", "r") as data:
	tsamples = []
	ttax = []
	lsamples = []
	count = 1
	for line in data:
		sample = line
		enumerate(sample, start = 0)
		 
#________________________________________________________________________________________
#			Get sample names
#________________________________________________________________________________________		

		flag = False 
		#flag is True when it runs into an underscore
		flag2 = False
		#flag2 is True when it runs into a second underscore
		i = 0
		j = 0
		samplename = []
		while flag == False:
			if sample[i] == "_":
				j = i + 1			
				while flag2 == False:
					if sample[j] == "_":
						secondstartpoint = j
						flag2 = True 
					else: 
						samplename.append(sample[j])
						j = j + 1
				flag = True 
			else:
				i = i + 1
		print "the sample name is: ",''.join(samplename)
		completename = ''.join(samplename)
		emptylist = []
		information = [0, 0]
		if completename not in tsamples:
			#adding a new sample 
			tsamples.append(completename)
			lsamples.append(emptylist)
			index = lsamples.index(emptylist)
			if ttax != "[]":
				for item in ttax:
					information[0] = item
					information[1] = 0
					lsamples[index].append(information)
				

			#print "added ", completename, "to table"

#________________________________________________________________________________________
#		get taxonomical stuff
#________________________________________________________________________________________
		# str.isspace() returns true if string given is only containing whitespace		
		i = secondstartpoint
		tax = []	#temp holder for tax info 
		

		#format not standard, need another way to navigate besides white space
		while sample[i].isspace() != True: 
			i = i + 1
				
		while sample[i].isspace() == True:
			i = i + 1
		exc = True 
		tcount = 0
		print len(sample)
		while sample[i].isspace() != True:
			tax.append(sample[i])
			if tcount >= 1:
				if tax[0] != "N" and tax[1] != "A":
					if (i+2) < len(sample):
						if sample[i+1].isspace() == True:
							if sample[i+2].isspace() == False:	
								tax.append(" ")
								i = i + 1

			i = i + 1
			tcount = tcount + 1

			
		completetax = ''.join(tax)
		information = []		
		index = tsamples.index(completename)	
		if completetax not in ttax:		
			ttax.append(completetax)
			information.append(completetax)
			information.append(0)
			for oitem in lsamples:
				oitem.append(information) 	
			ii = len(lsamples[index]) - 1		
			lsamples[index][ii] = [completetax, 1]	
		elif completetax in ttax:
			ii = ttax.index(completetax)
			lsamples[index][ii][1] = lsamples[index][ii][1] + 1 
	#making the table at the end of the file
	#obtain # of rows, aka samples
	tsamplelen = len(tsamples)
	#obtain # of columns, aka taxes
	ttaxlen = len(ttax)
	table = []
	for ooitem in lsamples:
		for iiitem in ooitem:
			table.append(iiitem[1])		

	import numpy as np
	
	table = np.asarray(table)
	table = np.reshape(table, (tsamplelen, ttaxlen))
	#ttax = np.asarray(ttax)	
	#tsamples = np.asarray(tsamples)
	myfile = open("output.txt", "w")
	myfile1 = open("outputrn.txt", "w")
	myfile2 = open("outputcn.txt", "w")	
	np.savetxt("output.txt", table, delimiter=",")
	#np.savetxt("outputrn.txt", tsamples, delimiter=",")
	#np.savetxt("outputcn.txt", ttax, delimiter=",")
	enumerate(tsamples)
	enumerate(ttax)
	i = 0	
	while i < tsamplelen: 
		myfile1.write("%s" %tsamples[i])
		if i != (tsamplelen - 1):
			myfile1.write(",")
		else:
			myfile1.write("\n")
		i = i+1
	i = 0
	while i < ttaxlen: 
		myfile2.write("%s" %ttax[i])
		if i != (ttaxlen - 1):
			myfile2.write(",")
		else:
			myfile2.write("\n")
		i = i+1
	myfile.close()
	myfile1.close()
	myfile2.close()
		
		
			
			







	
			





