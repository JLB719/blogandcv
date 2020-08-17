from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

class NewVisitorTest(unittest.TestCase) :
    def setUp(self) :
        self.browser = webdriver.Firefox()

    def tearDown(self) :
        self.browser.quit()
    def check_in_table(self, row_text, idtag) :
        table = self.browser.find_element_by_id(idtag)
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def check_ids(self, text, idtag) :
        outputs= self.browser.find_elements_by_id(idtag)
        self.assertIn(text, [output.text for output in outputs])

    def waitforelement(self, id) :
        try:
            waiter = WebDriverWait(driver, 10)
            waiter.until(EC.presence_of_element_located(By.ID, id))
        finally:
            self.fail('Timedout')

    def box(self, id) :
        return self.browser.find_element_by_id(id)

    def test_can_build_a_cv(self) :
        #goes to check out cv builder
        self.browser.get('http://127.0.0.1:8000/cv/')
        
        #notices title and header mention cv builder
        self.assertIn('CV Builder', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1')





        #invited to enter name
        inputboxname=self.browser.find_element_by_id('namequest')
        self.assertEqual(self.browser.find_element_by_id('namequestion').text, 'Enter your full name')
        #types James Bartlett into text box
        inputboxname.send_keys('James Bartlett')
        inputboxname.send_keys(Keys.ENTER)
        time.sleep(1)
        self.assertEqual(self.browser.find_element_by_id('namedis').text, 'Name: James Bartlett')


        #invited to enter email into text box
        inputboxemail = self.browser.find_element_by_id('email')
        self.assertEqual(self.browser.find_element_by_id('emailquestion').text, "Enter your email")
        # checks to see if a non email can be entered


        # enters james@gmail.com
        inputboxemail.send_keys('james@gmail.com')
        inputboxemail.send_keys(Keys.ENTER)
        time.sleep(1)
        # self.waitforelement('email')
        self.assertEqual(self.browser.find_element_by_id('emaildis').text, 'Email: james@gmail.com')
        inputboxemail = self.browser.find_element_by_id('email')
        inputboxemail.send_keys('jameslukebartlett@gmail.com')
        time.sleep(1)
        inputboxemail.send_keys(Keys.ENTER)
        time.sleep(1)
        self.assertEqual(self.browser.find_element_by_id('emaildis').text, 'Email: jameslukebartlett@gmail.com')

        #invited to enter mobile number into text box
        inputboxnumber=self.browser.find_element_by_id('number')
        self.assertEqual(self.browser.find_element_by_id('telquestion').text, 'Enter your telephone number')
        #checks a non number can't be entered


        inputboxnumber.send_keys('111111111')
        inputboxnumber.send_keys(Keys.ENTER)
        time.sleep(1)
        self.assertEqual(self.browser.find_element_by_id('numberdis').text, 'Number: 111111111')

        #types 07094534634 in
        inputboxnumber = self.browser.find_element_by_id('number')
        inputboxnumber.send_keys('07094534634')
        inputboxnumber.send_keys(Keys.ENTER)
        time.sleep(1)
        self.assertEqual(self.browser.find_element_by_id('numberdis').text, 'Number: 07094534634')

        # when hits enter name, email and number are displayed
        #will need to decide how i want it displayed
        #Personal profile

        #Invited towrite a personal profile
        inputboxprofile = self.browser.find_element_by_id('personalprof')
        self.assertEqual(self.browser.find_element_by_id('profquestion').text, 'Enter a personal profile')
        #Types looking for work have a computer sciecne degree and good teamwork skills
        inputboxprofile.send_keys('Looking for work have a computer science degree and good teamwork skills')
        submitprofile = self.browser.find_element_by_id('Profile')
        submitprofile.click()
        time.sleep(1)
        #Upon enter personal profile is displayed
        self.assertEqual(self.browser.find_element_by_id('profiledis').text, 'Looking for work have a computer science degree and good teamwork skills')

        inputboxprofile = self.browser.find_element_by_id('personalprof')
        inputboxprofile.send_keys('Looking to study a course to further improve my robotics. I am hard working and work well in a team')
        submitprofile = self.browser.find_element_by_id('Profile')
        submitprofile.click()
        time.sleep(1)
        #Upon enter personal profile is displayed
        self.assertEqual(self.browser.find_element_by_id('profiledis').text, 'Looking to study a course to further improve my robotics. I am hard working and work well in a team')


        #Skills
        inputboxskills=self.browser.find_element_by_id('skill')
        self.assertEqual(self.browser.find_element_by_id('Skillsquestion').text, 'Enter a skill')

        #Invited to enter a skill
        inputboxskills.send_keys('Java')
        inputboxskills.send_keys(Keys.ENTER)
        #Types Java
        time.sleep(1)

        # Upon enter java is displayed underskills
        self.check_in_table('Java', 'skillstable')
        # Invited to enter another skill


        # Types Teamwork
        inputboxskills = self.box('skill')
        inputboxskills.send_keys('Teamwork')
        inputboxskills.send_keys(Keys.ENTER)
        # Upon enter both skills entries are displayed
        time.sleep(1)
        # self.fail('Checking if it gets to this point')
        # self.check_in_table('Java', 'skillstable')
        self.check_in_table('Java', 'skillstable')
        self.check_in_table('Teamwork', 'skillstable')

        inputboxskills = self.box('skill')
        inputboxskills.send_keys('C')
        inputboxskills.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_in_table('Java', 'skillstable')
        self.check_in_table('Teamwork', 'skillstable')
        self.check_in_table('C', 'skillstable')

        inputboxskills = self.box('skill')
        inputboxskills.send_keys('Attention to detail')
        inputboxskills.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_in_table('Java', 'skillstable')
        self.check_in_table('Teamwork', 'skillstable')
        self.check_in_table('C', 'skillstable')
        self.check_in_table('Attention to detail', 'skillstable')

        inputboxskills = self.box('skill')
        inputboxskills.send_keys('Python')
        inputboxskills.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_in_table('Java', 'skillstable')
        self.check_in_table('Teamwork', 'skillstable')
        self.check_in_table('C', 'skillstable')
        self.check_in_table('Attention to detail', 'skillstable')
        self.check_in_table('Python', 'skillstable')



        #Invited to enter a qualification
        inputboxqualification = self.browser.find_element_by_id('qualification')
        self.assertEqual(self.browser.find_element_by_id('Qualificationquestion').text, 'Enter a proffessional qualification')

        #Types level 1 java
        inputboxqualification.send_keys('Level 1 Java')
        inputboxqualification.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_in_table('Level 1 Java', 'qualificationstable')

        inputboxqualification = self.box('qualification')
        inputboxqualification.send_keys('Level 2 Java')
        inputboxqualification.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_in_table('Level 1 Java', 'qualificationstable')
        self.check_in_table('Level 2 Java', 'qualificationstable')

        inputboxqualification = self.box('qualification')
        inputboxqualification.send_keys('BCS Essentials Certificate in Artificial Intelligence')
        inputboxqualification.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_in_table('Level 1 Java', 'qualificationstable')
        self.check_in_table('Level 2 Java', 'qualificationstable')
        self.check_in_table('BCS Essentials Certificate in Artificial Intelligence', 'qualificationstable')

        inputboxqualification = self.box('qualification')
        inputboxqualification.send_keys('BSC Computer Science')
        inputboxqualification.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_in_table('Level 1 Java', 'qualificationstable')
        self.check_in_table('Level 2 Java', 'qualificationstable')
        self.check_in_table('BCS Essentials Certificate in Artificial Intelligence', 'qualificationstable')
        self.check_in_table('BSC Computer Science', 'qualificationstable')

        inputboxqualification = self.box('qualification')
        inputboxqualification.send_keys('Level 1 Teamwork')
        inputboxqualification.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_in_table('Level 1 Java', 'qualificationstable')
        self.check_in_table('Level 2 Java', 'qualificationstable')
        self.check_in_table('BCS Essentials Certificate in Artificial Intelligence', 'qualificationstable')
        self.check_in_table('BSC Computer Science', 'qualificationstable')
        self.check_in_table('Level 1 Teamwork', 'qualificationstable')




        #Project
        inputboxprojecttitle = self.browser.find_element_by_id('projectover')
        self.assertEqual(self.browser.find_element_by_id('ProjectQuestion').text, 'Enter a project name')

        inputboxprojectdes = self.browser.find_element_by_id('projectdes')
        self.assertEqual(self.browser.find_element_by_id('ProjectDescription').text, 'Enter the description of the project')
        submitproject = self.browser.find_element_by_id('ProjectSub')

        inputboxprojecttitle.send_keys('Image filter in java')
        inputboxprojectdes.send_keys('Used matricies and arrays in java to create different ones by changing the rgb values')
        submitproject.click()
        time.sleep(1)

        self.check_ids('Image filter in java', 'projecttitle')
        self.check_ids('Used matricies and arrays in java to create different ones by changing the rgb values', 'projectdescribe')

        submitproject = self.box('ProjectSub')
        inputboxprojecttitle = self.box('projectover')
        inputboxprojectdes = self.box('projectdes')
        inputboxprojecttitle.send_keys('Moving robot')
        inputboxprojectdes.send_keys('Programmed a lego robot to follow a black line using color sensors and avoiding obstacles')
        submitproject.click()
        time.sleep(1)

        self.check_ids('Image filter in java', 'projecttitle')
        self.check_ids('Used matricies and arrays in java to create different ones by changing the rgb values', 'projectdescribe')
        self.check_ids('Moving robot', 'projecttitle')
        self.check_ids('Programmed a lego robot to follow a black line using color sensors and avoiding obstacles', 'projectdescribe')

        inputboxprojecttitle = self.box('projectover')
        inputboxprojectdes = self.box('projectdes')
        submitproject = self.box('ProjectSub')
        inputboxprojecttitle.send_keys('Maze game')
        inputboxprojectdes.send_keys('A game where players move through a maze trying to collect as many coins as possible while fighting other players')
        submitproject.click()
        time.sleep(1)

        self.check_ids('Image filter in java', 'projecttitle')
        self.check_ids('Used matricies and arrays in java to create different ones by changing the rgb values', 'projectdescribe')
        self.check_ids('Moving robot', 'projecttitle')
        self.check_ids('Programmed a lego robot to follow a black line using color sensors and avoiding obstacles', 'projectdescribe')
        self.check_ids('Maze game', 'projecttitle')
        self.check_ids('A game where players move through a maze trying to collect as many coins as possible while fighting other players', 'projectdescribe')

        #Achievments

        # Invited to enter an achievment
        inputboxachievments=self.browser.find_element_by_id('achievment')
        self.assertEqual(self.browser.find_element_by_id('Achievmentquestion').text, 'Enter an achievment')

        # Types 1st place in hackathon
        inputboxachievments.send_keys('1st place in hackathon')
        # Upon enter displays ahcivment
        inputboxachievments.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_in_table('1st place in hackathon', 'achtable')
        # Invited to enter another achievent

        #Types a levels
        inputboxachievments = self.box('achievment')
        inputboxachievments.send_keys('a levels')

        # upon enter displays both ahcivments
        inputboxachievments.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_in_table('1st place in hackathon', 'achtable')
        self.check_in_table('a levels', 'achtable')

        inputboxachievments = self.box('achievment')
        inputboxachievments.send_keys('Best in a level maths')
        inputboxachievments.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_in_table('1st place in hackathon', 'achtable')
        self.check_in_table('a levels', 'achtable')
        self.check_in_table('Best in a level maths', 'achtable')

        inputboxachievments = self.box('achievment')
        inputboxachievments.send_keys('1st Place in BAE systems CTF')
        inputboxachievments.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_in_table('1st place in hackathon', 'achtable')
        self.check_in_table('a levels', 'achtable')
        self.check_in_table('Best in a level maths', 'achtable')
        self.check_in_table('1st Place in BAE systems CTF', 'achtable')

        inputboxachievments = self.box('achievment')
        inputboxachievments.send_keys('Social Secretary for filmsoc between 2019 and 2020')
        inputboxachievments.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_in_table('1st place in hackathon', 'achtable')
        self.check_in_table('a levels', 'achtable')
        self.check_in_table('Best in a level maths', 'achtable')
        self.check_in_table('1st Place in BAE systems CTF', 'achtable')
        self.check_in_table('Social Secretary for filmsoc between 2019 and 2020', 'achtable')
        #Work experience

        # Invited to enter name of company
        inputboxcompany = self.browser.find_element_by_id('placeofwork')
        self.assertEqual(self.browser.find_element_by_id('placeofworkq').text, 'Enter the place of work')
        #Enters university of brimigham
        # Invited to enter job role
        inputboxjob = self.browser.find_element_by_id('role')
        self.assertEqual(self.browser.find_element_by_id('roleq').text, 'Enter the job role')
        #Types student ambassador
        #Invited to enter date started
        inputboxstartdatew=self.browser.find_element_by_id('startdatew')
        self.assertEqual(self.browser.find_element_by_id('startdatewq').text, 'Enter the start date of the job')

        #Types 01/2019
        #Invited to enter date finished or present
        self.assertEqual(self.browser.find_element_by_id('enddatewq').text, 'Enter the date you finished the role')
        #Types present
        #Invited to enter job description
        inputboxenddatew=self.browser.find_element_by_id('enddatew')
        self.assertEqual(self.browser.find_element_by_id('jobdesq').text, 'Enter the job description details')
        submitworkexp = self.browser.find_element_by_id('WorkExperience')
        inputboxjobdes=self.browser.find_element_by_id('description')

        #Types resonsiple to showing students round builidng makeing them feel welcome and setting up events
        inputboxcompany.send_keys("University of Birmingham")
        inputboxjob.send_keys("student ambassador")
        inputboxstartdatew.send_keys('01/01/2019')
        inputboxenddatew.send_keys('03/08/2020')
        inputboxjobdes.send_keys("Responsible for showing students round building making them feel welcome and setting up events")
        submitworkexp.click()
        time.sleep(1)
        #Upon enter company, role, dates and job description are displayed
        self.check_ids("Job Role: student ambassador", "jobtitled")
        self.check_ids("Company: University of Birmingham", "jobcompd")
        self.check_ids("Dates: 01/01/2019 - 03/08/2020", "jobdatesd")
        self.check_ids("Responsible for showing students round building making them feel welcome and setting up events", "jobdetailsd")


        inputboxcompany = self.box('placeofwork')
        inputboxjob = self.box('role')
        inputboxstartdatew = self.box('startdatew')
        inputboxenddatew = self.box('enddatew')
        inputboxjobdes = self.box('description')
        submitworkexp = self.box('WorkExperience')

        inputboxcompany.send_keys("PGL")
        inputboxjob.send_keys("Activity Instrustuctor / Group Leader")
        inputboxstartdatew.send_keys('01/07/2019')
        inputboxenddatew.send_keys('01/09/2019')
        inputboxjobdes.send_keys("Responsbile for supervising children with thier activitys and occasionally looking after thier needes while providing a high standard of outdoor education")
        submitworkexp.click()
        time.sleep(1)
        #Upon enter company, role, dates and job description are displayed
        self.check_ids("Job Role: student ambassador","jobtitled")
        self.check_ids("Company: University of Birmingham", "jobcompd")

        self.check_ids("Dates: 01/01/2019 - 03/08/2020", "jobdatesd")
        self.check_ids("Responsible for showing students round building making them feel welcome and setting up events", "jobdetailsd")

        self.check_ids("Job Role: Activity Instrustuctor / Group Leader", "jobtitled")
        self.check_ids("Company: PGL", "jobcompd")

        self.check_ids("Dates: 01/07/2019 - 01/09/2019", "jobdatesd")
        self.check_ids("Responsbile for supervising children with thier activitys and occasionally looking after thier needes while providing a high standard of outdoor education", "jobdetailsd")

        inputboxcompany = self.box('placeofwork')
        inputboxjob = self.box('role')
        inputboxstartdatew = self.box('startdatew')
        inputboxenddatew = self.box('enddatew')
        inputboxjobdes = self.box('description')
        submitworkexp = self.box('WorkExperience')

        inputboxcompany.send_keys("Coder Dojo")
        inputboxjob.send_keys("Mentor")
        inputboxstartdatew.send_keys('01/10/2017')
        inputboxenddatew.send_keys('01/07/2019')
        inputboxjobdes.send_keys("Mentored students while they learned to code. Also set up for events and attended various promotoional activities")
        submitworkexp.click()
        time.sleep(1)
        #Upon enter company, role, dates and job description are displayed
        self.check_ids("Job Role: student ambassador","jobtitled")
        self.check_ids("Company: University of Birmingham", "jobcompd")

        self.check_ids("Dates: 01/01/2019 - 03/08/2020", "jobdatesd")
        self.check_ids("Responsible for showing students round building making them feel welcome and setting up events", "jobdetailsd")

        self.check_ids("Job Role: Activity Instrustuctor / Group Leader", "jobtitled")
        self.check_ids("Company: PGL", "jobcompd")

        self.check_ids("Dates: 01/07/2019 - 01/09/2019", "jobdatesd")
        self.check_ids("Responsbile for supervising children with thier activitys and occasionally looking after thier needes while providing a high standard of outdoor education", "jobdetailsd")

        self.check_ids("Job Role: Mentor", "jobtitled")
        self.check_ids("Company: Coder Dojo", "jobcompd")

        self.check_ids("Dates: 01/10/2017 - 01/07/2019", "jobdatesd")
        self.check_ids("Mentored students while they learned to code. Also set up for events and attended various promotoional activities", "jobdetailsd")
        #Education

        #Invited to enter place of learning
        inputboxschool=self.browser.find_element_by_id('school')
        self.assertEqual(self.browser.find_element_by_id('schoolq').text, 'Enter the name of the school')

        #Enters woodhouse college
        # Invited to enter date started
        inputboxstartdates=self.browser.find_element_by_id('startdates')
        self.assertEqual(self.browser.find_element_by_id('startdatesq').text, 'Enter the date you started at the school')

        #Types 09/2016
        #Invited to enter date left
        inputboxenddates=self.browser.find_element_by_id('enddates')
        self.assertEqual(self.browser.find_element_by_id('enddatesq').text, 'Enter the date you finished at the school')

        #Types 07/2018
        #Invited to enter qualifications
        inputboxgrades = self.browser.find_element_by_id('grades')
        self.assertEqual(self.browser.find_element_by_id('gradesq').text, 'Enter the grades obtained')
        submiteducation=self.browser.find_element_by_id('EducationSubmit')

        #Types Maths A* FUther Maths B, Georgraphy A
        inputboxschool.send_keys('Woodhouse College')
        inputboxstartdates.send_keys('01/09/2016')
        inputboxenddates.send_keys('01/07/2018')
        inputboxgrades.send_keys('Maths A* Further Maths B Georgraphy A')
        # Upon enter school, dates and grades are displayed
        submiteducation.click()
        time.sleep(1)

        self.check_ids("School/College: Woodhouse College", 'schoold')
        self.check_ids("01/09/2016 - 01/07/2018", 'schooldatesd')
        self.check_ids("Maths A* Further Maths B Georgraphy A", 'schooldetailsd')

        inputboxschool = self.box('school')
        inputboxstartdates = self.box('startdates')
        inputboxenddates = self.box('enddates')
        inputboxgrades = self.box('grades')
        submiteducation = self.box('EducationSubmit')

        inputboxschool.send_keys('University of Birmingham')
        inputboxstartdates.send_keys('01/09/2018')
        inputboxenddates.send_keys('Present')
        inputboxgrades.send_keys('BSc Computer Science, predicted 2.1')
        # Upon enter school, dates and grades are displayed
        submiteducation.click()
        time.sleep(1)

        self.check_ids("School/College: Woodhouse College", 'schoold')
        self.check_ids("01/09/2016 - 01/07/2018", 'schooldatesd')
        self.check_ids("Maths A* Further Maths B Georgraphy A", 'schooldetailsd')

        self.check_ids("School/College: University of Birmingham", 'schoold')
        self.check_ids("01/09/2018 - Present", 'schooldatesd')
        self.check_ids("BSc Computer Science, predicted 2.1", 'schooldetailsd')

        #Notes
        inputboxnotes = self.browser.find_element_by_id('Notes')
        self.assertEqual(self.browser.find_element_by_id('PostQuestion').text, 'Enter any other notes')

        submitnotes = self.browser.find_element_by_id('NotesSubmit')

        inputboxnotes.send_keys('As a reward for my hard work at a charity I was selected for a trip to europe')
        submitnotes.click()
        time.sleep(1)

        self.check_ids('As a reward for my hard work at a charity I was selected for a trip to europe', 'notesdetails')

        inputboxnotes = self.box('Notes')
        submitnotes = self.box("NotesSubmit")
        inputboxnotes.send_keys('I am a very hard working and commited individual who has got a wide range of experience and would love to come and work for your company')
        submitnotes.click()
        time.sleep(1)

        self.check_ids('As a reward for my hard work at a charity I was selected for a trip to europe', 'notesdetails')
        self.check_ids('I am a very hard working and commited individual who has got a wide range of experience and would love to come and work for your company', 'notesdetails')

        inputboxnotes = self.box('Notes')
        submitnotes = self.box("NotesSubmit")
        inputboxnotes.send_keys('References from universities and previous employers are available upon request')
        submitnotes.click()
        time.sleep(1)

        self.check_ids('As a reward for my hard work at a charity I was selected for a trip to europe', 'notesdetails')
        self.check_ids('I am a very hard working and commited individual who has got a wide range of experience and would love to come and work for your company', 'notesdetails')
        self.check_ids('References from universities and previous employers are available upon request', 'notesdetails')




if __name__ == '__main__' :
    unittest.main(warnings='ignore')
