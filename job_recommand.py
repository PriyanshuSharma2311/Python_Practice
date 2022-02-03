name = input('Enter your name :')
yes = ['Yes', 'y', 'yes', 'ya']
no = ['No', 'no', 'nothing', 'Nothing']
                  #    *******************langauges**************************
learnpy = ['A.W.S or Amazon web service', 'Django', "API's or application programing interface",
    'Docker', 'Linux', 'Cloud computing', 'Machine learning', 'Javascript', 'Java']
learnjv = ['A.W.S or Amazon web service', 'Django', "API's or application programing interface",
    'Docker', 'Linux', 'Cloud computing', 'Machine learning', 'Javascript', 'Python']
learnhtml = ['A.W.S or Amazon web service', 'Django', "API's or application programing interface",
    'Docker', 'Linux', 'Cloud computing', 'CSS', 'java', 'Machine learning', 'Javascript', 'Python']
learncss = ['A.W.S or Amazon web service', 'Django', "API's or application programing interface",
    'Docker', 'Linux', 'Cloud computing', 'HTML', 'Machine learning', 'Javascript', 'Python']
learnjs = ['Flutter', 'A.W.S or Amazon web service', 'Django', "API's or application programing interface",
    'Docker', 'Linux', 'Cloud computing', 'CSS', 'HTML', 'Machine learning', 'Javascript', 'Python']
learnsql = ['A.W.S or Amazon web service', 'Django', "API's or application programing interface",
    'Docker', 'Linux', 'Cloud computing', 'CSS', 'HTML', 'Machine learning', 'Javascript', 'Python']
learnflutter = ['A.W.S or Amazon web service', 'Django', "API's or application programing interface", 'Docker',
    'Linux', 'Cloud computing', 'Machine learning', 'Javascript', 'Python', 'HTML', 'CSS', 'Python', 'Java']
learnc = ['A.W.S or Amazon web service', 'Django', "API's or application programing interface", 'Docker',
    'Linux', 'Cloud computing', 'Machine learning', 'Javascript', 'Python', 'HTML', 'CSS', 'Python', 'Java']
                # ******************jobs******************************
java = ['Java Developer software Engineer', 'Mobile Application Developer Manager', 'Junior Java Developer', 'Senior Java Web Developer', 'Core Java Developer', 'Mobile Lead Software Engineer', 'Senior Software Engineer C',
    'SOA Analyst Developer', 'Senior Java Developer', 'Lead Java Developer', 'Java Application Developer', 'Senior Java Developer', 'Senior Java Developer', 'Free Training and Placement', 'Java', 'Java Developer']
Python = ['Software engineer', 'Educator', 'Python developer', 'DevOps engineer', 'Front-end software or web developer',
    'Data Analyst/JournalistProduct manager', 'Research Analyst', 'Data Scientist', 'Financial Advisor']
java_script = ['Full stack developer', 'Web Application Developer', 'UX Designer', 'Web Designer',
                       ' UI Designer', 'DevOps Engineer']
css = ['front_end developer', 'UI designer', 'Web developer']
html = ['front_end developer', 'UI designer', 'Web developer']
Flutter = ['Android developer', 'IOS Developer', 'Dart programming']
SQL = ['Business Analyst', 'Data Scientist', 'Software Engineer', 'Database Administrator',
                  'Quality Assurance Tester', 'Researcher / Educator']
C = ['Low-level programming', 'Desktop applications', 'Rendering engines', 'Game engines',
              'Network programming', 'Acceleration of computational intensive code parts', 'Virtual Reality applications']
jobs = {'Python': Python, 'python': Python, 'Java': java, 'java': java, 'java_script': java_script, 'Javascript': java_script, 'javascript': 'java_script',
    'html': html, 'Html': html, 'css': css, 'Css': css, 'Flutter': Flutter, 'flutter': Flutter, 'SQL': SQL, 'sql': SQL, 'c': C, 'C': C, 'C++': C, 'c++': C}
            # *********user Welcome*******************
wel = (f'Welcome {name}\n\n').center(85, ' ')
print(wel)
            # *************recomendation starts from here **************************
lanc = int(input('Enter the number of languages you knowns: '))
for i in range(1, lanc+1):
    lang = input('Enter languages names you knows : ')
    py = ('The jobs are there for your language\n').center(85, ' ')
    print(py)
    if lang == 'Python' or lang == 'python':
        for j in range(0, len(jobs['Python'])):
            print(j+1, ':', jobs['python'][j])
        ln = ('You need to learn these languages \n').center(85, ' ')
        print(ln)
        for k in range(0, len(learnpy)):
            print(k+1, ':', learnpy[k])
    elif lang == 'java' or lang == 'Java':
        for j in range(0, len(jobs['java'])):
            print(j+1, ':', jobs['java'][j])
        ln = ('You need to learn these languages \n').center(85, ' ')
        print(ln)
        for k in range(0, len(learnjv)):
            print(k+1, ':', learnjv[k])
    elif lang == 'html' or lang == 'Html' :
        for j in range (0,len(jobs['html'])) :    
            print(j+1,':',jobs['html'][j])
        ln  = ('You need to learn these languages \n').center(85,' ')
        print(ln)
        for k in range(0,len(learnhtml)) :
            print(k+1,':',learnhtml[k])   
         
    elif lang == 'Css' or lang == 'css' :
        for j in range (0,len(jobs['html'])) :    
            print(j+1,':',jobs['html'][j])
        ln  = ('You need to learn these languages \n').center(85,' ')
        print(ln)
        for k in range(0,len(learnhtml)) :
            print(k+1,':',learnhtml[k])   
    elif lang == 'c' or lang == 'C' or lang == 'c++' or lang == 'C++' :
        for j in range (0,len(jobs['C'])) :    
            print(j+1,':',jobs['c'][j])
        ln  = ('You need to learn these languages \n').center(85,' ')
        print(ln)
        for k in range(0,len(learnc)) :
            print(k+1,':',learnc[k])   
    elif lang == 'sql' or lang == 'Sql' :
        for j in range (0,len(jobs['SQL'])) :    
            print(j+1,':',jobs['SQL'][j])
        ln  = ('You need to learn this language \n').center(85,' ')
        print(ln)
        for k in range(0,len(learnsql)) :
            print(k+1,':',learnsql[k])   
    elif lang == 'Flutter' or lang == 'flutter' :
        for j in range (0,len(jobs['flutter'])) :    
            print(j+1,':',jobs['flutter'][j])
        ln  = ('You need to learn this language \n').center(85,' ')
        print(ln)
        for k in range(0,len(learnflutter)) :
            print(k+1,':',learnflutter[k])   
    elif lang == 'javascript' or lang == 'js' or lang == 'JS' or lang == 'Javascript' :
        for j in range (0,len(jobs['javascript'])) :    
            print(j+1,':',jobs['javascript'][j])
        ln  = ('You need to learn this language \n').center(85,' ')
        print(ln)
        for k in range(0,len(learnjs)) :
            print(k+1,':',learnjs[k])   
thnk = (f'THANKS {name} FOR USING OUR PROGRAM\n').center(85,' ')
print(thnk)
                    #  ****************************END*****************************