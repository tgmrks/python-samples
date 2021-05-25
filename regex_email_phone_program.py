#!usr/bin/env python
import re, pyperclip

phoneRegex = re.compile(r'''
# 444-555-9999 555-999 (444) 555-9999 ext 12345 ext. 12345 x12345
(
((\d\d\d)|(\(\d\d\d\)))?	# area code
(\s|-) 			# separator
\d\d\d			# first 3 digits
-			# separator
\d\d\d\d		# last 4 digits
(((ext(\.)?\s)|x)	# ext text part
(\d{2,5}))?			# ext number part
)
''', re.VERBOSE)

emailRegex = re.compile(r'''
# some.+_thing@something.com
[a-zA-Z0-9_.+]+		# name
@			# symbol
[a-zA-Z0-9_.+]+ 	# domain
''', re.VERBOSE)

# getting the text from the clipboard
text = pyperclip.paste()

# extract phone and email
extractedPhones = phoneRegex.findall(text)
extractedEmails = emailRegex.findall(text)

allExtractedPhones = []
for phoneNumber in extractedPhones :
	allExtractedPhones.append(phoneNumber[0])

#print(extractedPhones)
print(allExtractedPhones)
print(extractedEmails)

# concatenate the results into clipbord
results = '\n'.join(allExtractedPhones) + '\n' + '\n'.join(extractedEmails)
pyperclip.copy(results)