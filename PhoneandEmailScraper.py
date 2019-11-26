import re,pyperclip

#Create regex object for phone numbers
phoneRegex = re.compile(r'''
#415-000-3231 | (414) 000-4322 | 000-4321 | 564-323 ext 12344 | 321-4234 ext. 12345 | x42343
(\((\d\d\d)\)?    #area-code
(\s|-)           #separator
\d\d\d           #first 3 digits
-                #separator
\d\d\d\d         #last 4 digits
(((ext(\.)?\s)|x)#extension word part
(\d{2,5}))?)      #extension number part
''',re.VERBOSE)

#Create regex for email
emailRegex = re.compile(r'''
someth._+\d@something.com

[a-zA-Z0-9._+]+    #name part
@    #@symbol part
[a-zA-Z0-9._+]+    #domain name part

''',re.VERBOSE)

#Get text off the clipboard
text = pyperclip.paste()

#Extract email and phone Number
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []

for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

#Copy the extracted email and phoneNumber to clipboard
result = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.paste(result)
