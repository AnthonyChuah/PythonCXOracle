INSTRUCTIONS FOR PYTHON CX_ORACLE PACKAGE


1. Install Python.

2. Add Python to your PATH environment variable. Edit your Environment Variables (START -> "Edit the system environment variables" -> Environment Variables -> Edit (System Variables: "PATH") -> Make sure one of the entries is your Python directory, e.g. C:/Program Files/Python35/.

3. If you have moved your installation directory to another one, e.g. from C:/Program Files/Python35/ to C:/Python35/, remember to change your PATH correspondingly. IMPORTANT: also edit your Registry Keys corresponding to your Python installation (google how to do this) to match the new directory.

4. Install Oracle Instant Client: http://www.oracle.com/technetwork/database/features/instant-client/index-097480.html. Choose a location for where you unzip the files: a good example is C:/instantclient/.

5. Install CX_Oracle: https://pypi.python.org/pypi/cx_Oracle/5.2.1

6. Add the path in step 4 to the PATH environment variable. Method is explained in step 2.

7. Find out where your ORACLE_HOME environment points to (it's a folder). Go there, then make subfolders network/admin/. Add a plain text file called tnsnames.ora to that directory. If ORACLE_HOME is C:/instantclient/, then the file should be in C:/instantclient/network/admin/tnsnames.ora

8. tnsnames.ora should be filled in with the database details: http://www.orafaq.com/wiki/Tnsnames.ora. You should have the necessary details for your / company's database. Our tnsnames.ora file:

ORA11 =
 (DESCRIPTION = 
   (ADDRESS_LIST =
     (ADDRESS = (PROTOCOL = TCP)(HOST = SERVERNAME)(PORT = PORTNUM))
   )
 (CONNECT_DATA =
   (SERVICE_NAME = SERVICENAME)
 )
)

9. Add TNS_ADMIN environment variable to your machine, pointing to ORACLE_HOME/network/admin/.

10. Connect using cx_Oracle inside Python, for example:

import cx_Oracle
con = cx_Oracle.connect('USERNAME/PASSWORD@SERVERNAME:PORTNUM/SERVICENAME')
cur = con.cursor()
cur.execute('SELECT * FROM TABLENAME')
row = cur.fetchone()
print(row)
cur.close()
con.close()