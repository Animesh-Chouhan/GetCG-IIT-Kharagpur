This a script that gives you the CGPA of any student at IIT Kharagpur.
All you need to know is the person's Roll Number.
I have parsed the data from ERP's site and used it to show the desired results. Of course I could have shown many other things but what matters the most is CGPA right (not for me btw :-P).Even if you dont admit it, I know. How?? you say? Well, I just know.:)


<h1>How to use it:</h1>
Make sure that you have root access while running this script.<br>
To use it just type <b>python getCG_erp.py</b> and you will be prompted for the Roll Number. <br>
Enter it, and the CGPA for every semester along with the <b>person's name</b> and <b>Department</b> will be listed right away!!

Go ahead, use it, I know you want to test it.How??Again...I just know. ;-D

```python
def no_case_details():
		#Intializing Browser
		br = mechanize.Browser()

		#Opens url of the form page
		br.open('http://courtnic.nic.in/supremecourt/casestatus_new/caseno_new.asp')

		#Filling & Submitting the form
		br.select_form('caseno')
		br.form['seltype'] = ['2']
		br.form['txtnumber'] = '7575'
		br.form['selcyear'] = ['2016']
		br.submit(name='Submit')
```



