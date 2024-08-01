

import re  #re = regex
from helper import d
# Imports should always go at the top of any file

# Regex Methods and Functions


#-- re.findall(pattern, text) : retrieves all non-overlapping matches of the patternand returns a list of all the matches

# find how many times I used the word 'and' in a sentence
text = "Hi my name is Travis, and I like to go and do things and stuff"

ands = re.findall(r"and", text)
print(ands) # the lists of all matches returned from .findall()
print(len(ands)) # using the len() function to determine how many matches there were


# Find all the hashtags in my post
post = "I LOVE # learning #Python_is_lyfe and #Regex, this is so fun! #Code"

tags = re.findall(r"#\w+", post)
print(tags)


# Find all words that start with b and end with the letter e
sentence = "Abe asked to build a bridge but he was told 'beware of the beehives!'."

bes = re.findall(r'\bb\w*e\b', sentence)
print(bes)


# Finding email addresses
text = "You can contact me at t.p@gmail.com or travis-p2@codingtemple.com, traviscpeck@email.com"

# username can include letters a-z, digits, _, -, .
# domain can include a-z, digits, _, -
# domain extension needs to be only 2 or 3 characters a-z

# When making a pattern, break it up into pieces
emails = re.findall(r"[\w.-]+@[\w-]+\.[a-z]{2,3}", text)
print(emails)


# find all words containing capital letters
sentence = "tHIs is a Sentence with couple words Some of Them are capiTalized AND some are not."

all_cap_words = re.findall(r"\w*[A-Z]+\w*", sentence)
print(all_cap_words)

d()

#-- re.search(pattern, text) : Searches a string for a pattern match, and returns the first occurance as a match object
#- great for input validation

# email = input("Enter an email here: ")
email = "kareem33-34-28@gmail.com"
found = re.search(r"[\w.-]+@[\w-]+\.[a-z]{2,3}", email)
print(found) #print out the match object
print(found.group()) # use .group() to unpack the match that was found

if found:
    print(f"{found.group()} Is a valid email! Please click continue!")
else:
    print("Invalid email")


#  Validating phone numbers

# I want to accept a variety of phone number formats
# 000-000-0000
# 000 000 0000
# 0000000000
# (000) 000-0000

number = "My phone number is: (770)-888-1180"

phone = re.search(r"[(]?\d{3}[)]?[\s-]?\d{3}[\s-]?\d{4}", number)
print(phone)

d()

#-- re.match(pattern, text) : Will return a match object if there is a pattern match at the beginning of the text

text = "Hello, world!"

obj = re.match(r"Hello", text)
print(obj)

# seems useless?
# what if we wanna check if a website link is secure?

url = "https://something.com"
secure = re.match(r"https", url)
if secure:
    print("This link goes to a secure website!")
else:
    print("This site is not very secure, proceed with caution!")

d()

#-- re.split(pattern, text) : splits the text on occurances of the pattern, returns a list

# split on the garbage
text = 'Python,Regex;Splitting-Example. Fun, right?'
words = re.split(r"[,.;\s-]+", text)
print(words)

d()

#-- re.sub(pattern, replacer, text) : replaces the occurrences of the pattern in a string with the replacer

number = "(770) 888-1180"

# Want to replace anything that is not a number
formatted_number = re.sub(r"\D", '', number)
print(formatted_number)

# Anonymous chat
chat = '''
@Yve-bee123 : "I think I love Regex"
@Travis : "Aren't you married?"
@Yve_bee123 : "It's just not the same"
@Travis : "They better not see this!
'''

anon_chat = re.sub(r"@[\w-]+", '@user-anon', chat)
print(anon_chat)

anon_chat = re.sub(r"@[A-Za-z|\d|_|-]+", '@user-anon', chat)
print(anon_chat)

d()

#-- Side Quest - Grouping

text = "123-456"

pattern = r"(\d+)-(\d+)"
thematch = re.search(pattern, text)
if thematch:
    print(thematch.group())
    print(f"Group 1: {thematch.group(1)}") # Output: 123
    print(f"Group 2: {thematch.group(2)}") # Output: 456