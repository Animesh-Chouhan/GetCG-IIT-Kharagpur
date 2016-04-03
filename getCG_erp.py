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
sem=[]
cgpa=[]
temp = 1

for i in range(0,len(p)):
	if(p[i].string==' CGPA'):
		temp+=1

print("CGPA of %s is as follows:"%(p[6].string))
for j in range(0,len(p)):
	if(p[j].string==' CGPA'):
		if(p[j+1].string==None):
			print ''
		else:
			print("\n\t %s at the end of Semester %s"%(p[j+1].string,temp-1))
		temp-=1
# print ("%s"%(time.time()-start_time))