'''Module: read_mod_aerosol_and_list_sds.py==========================================================================================Disclaimer: The code is for demonstration purposes only. Users are responsible to check for accuracy and revise to fit their objective.Author: Justin Roberts-Pierel, 2015 Organization: NASA ARSETPurpose: To print all SDS from an HDF4 fileSee the README associated with this module for more information.=========================================================================================='''#import necessary modulesfrom pyhdf import SDimport numpy as np#This uses the file "fileList.txt", containing the list of files, in order to read the filestry:	fileList=open('fileList.txt','r')except:	print('Did not find a text file containing file names (perhaps name does not match)')	sys.exit()#loops through all files listed in the text filefor FILE_NAME in fileList:	FILE_NAME=FILE_NAME.strip()	user_input=input('Would you like to process\n' + FILE_NAME + '\n\n(Y/N)')	if(user_input == 'N' or user_input == 'n'):		continue	else:		if '3K' in FILE_NAME: #then this is a 3km MODIS file			print('\nThis is a MODIS 3km file. Here is a list of SDS in your file:\n')		elif 'L2' in FILE_NAME:			print('\nThis is a MODIS 10km file. Here is a list of SDS in your file:\n')		else:			print('The file named :',FILE_NAME, ' is not a valid MODIS file (Or is named incorrectly). \n')			continue		try:			# open the hdf file for reading			hdf=SD.SD(FILE_NAME)		except:			print('Unable to open file: \n' + FILE_NAME + '\n Skipping...')			continue		#extract the list of SDS in the hdf4 file		datasets=hdf.datasets()		#Print the list		for i,v in enumerate(datasets):			print('{0}. {1}'.format(i+1,v))		print ('')		#asks if the user would like to continue to the next file, exits if notprint('\nAll valid files given have been processed')