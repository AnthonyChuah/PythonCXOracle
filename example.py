## Extracts data from database.
import cx_Oracle
import os
import pandas
import numpy
import time

cwd = os.getcwd()
datestamp = time.strftime("%Y%m%d")

connection = cx_Oracle.connect('USERNAME/PASSWORD@SERVERNAME:PORTNUM/SERVICENAME')
cursor = connection.cursor()
query = "SELECT USERNAME, FILENAME, FOLDERNAME, CREATED_AT, COMPANY, NAME FROM (SELECT * FROM EOSREPORTS.DOWNLOADEDFILES) WHERE USERNAME NOT LIKE \'%@AURORAER.COM\' ORDER BY CREATED_AT"
cursor.execute(query)
downloads_data = cursor.fetchall()
cursor.close()
connection.close()

# downloads_data is a list of tuples, each tuple is a tuple of strings.
# I want to unpack all of this into a Pandas data frame with column names of
# USERNAME, FILENAME, FOLDERNAME, CREATED_AT, COMPANY, NAME.

colnames = ("USERNAME","FILENAME","FOLDERNAME","CREATED_AT","COMPANY","NAME")
numrows = len(downloads_data)
numcols = len(downloads_data[0])
max_char_len = 200

chararray = numpy.chararray((numrows,numcols),itemsize=max_char_len)

row_iter = 0
for row in downloads_data:
    for col in range(numcols):
        chararray[row_iter,col] = row[col]
    row_iter += 1
del row_iter

output_dataframe = pandas.DataFrame(data=chararray,columns=colnames,dtype=str)
output_dataframe.to_excel(cwd+"\\EOS_File_Downloads_"+datestamp+".xlsx",sheet_name="EOSdownloads",header=colnames,index=False)
