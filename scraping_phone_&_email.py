import re
phoneRegex = re.compile(r'''(
 (\d{3}|\(\d{3}\))? # area code
 (\s|-|\.)? # separator
 (\d{3}) # first 3 digits
 (\s|-|\.) # separator
 (\d{4}) # last 4 digits
 (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
 )''', re.VERBOSE)


# TODO: Create email regex.
emailRegex = re.compile(r'[a-z0-9_]+@[a-z0-9_]+.[a-z0-9_]+')

emailReg = re.compile(r'(\w+[.|\w])*@(\w+[.])*\w+')
#print(emailRegex)

# TODO: Find matches in text file.
file = open("text.txt", 'r')
f = open("output.txt", 'w')
f.write("Email\t\t Mobile\n")
for each_line in file:
    print(each_line)
    #for words in each_line.split(' '):
    #print("word-",words)
    email = emailRegex.search(each_line)
    if email :
        print("email--",email.group())
    phone = phoneRegex.search(each_line)
    if phone:
        mobile = phone.group()
        #print(type(mobile))
        print("Phone no--",mobile)
    else:
        print("Phone No Not Exists in This line")
    if email:
        email_id = email.group()
        #print(type(email_id))
        #print("Email-",email_id)
    else:
        print("Email No Not Exists in This line")
        
      
    line = email_id +"\t\t" +mobile
    
    #print(line)
    f.write(line +"\n")
    '''
    line = line + phone.group()
    
    print(line)
    #f.write(email +"\t\t"+ phone)
    '''