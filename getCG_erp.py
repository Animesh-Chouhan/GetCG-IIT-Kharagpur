from bs4 import BeautifulSoup
from lxml import html
import mechanize
import time


br = mechanize.Browser()
#get the ERP page
rollno = raw_input('Enter the rollno: ')
# start_time = time.time()
url = 'https://erp.iitkgp.ernet.in/StudentPerformance/view_performance.jsp?rollno='+ rollno.upper()
br.open(url)
soup = BeautifulSoup(br.response().read().replace('&nbsp','').replace('<b>','<td>'),'lxml')
p = soup.findAll('td')
temp = 1

for i in range(0,len(p)):
	if(p[i].string==' CGPA'):
		temp+=1 

# print("CGPA of %s from the Department of %s is as follows:"%(p[6].string,p[9].string))
print (" Name: %s \n Department: %s \n CGPA :\n"%(p[6].string,p[9].string))
for j in range(0,len(p)):
	if(p[j].string==' CGPA'):
		if(p[j+1].string==None):
			print ''
		else:
			print("\t Semester %s --> %s\n"%(temp-1,p[j+1].string))
		temp-=1
# print ("%s"%(time.time()-start_time))