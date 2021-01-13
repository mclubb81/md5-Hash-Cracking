# Import Libraries
import hashlib
import random
import pandas as pd

# Known hash value given
knownHash = "74B104101A970A5408262B50F2082D65"

# Test from value already in table. In this case password is: computer
# knownHash = "df53ca268240ca76670c8566ee54568a" 


# Declare List of Possible Password Fragments Based on Public Records
passFrag = [
    "bob", "smith", "dec", "december", "12", "23", "85", "34","1985",
    "chicago", "chi", "il", "illinois", "bulls" , "bears", "socks"
    "white", "water", "ww", "uww", "warhawk", "warhawks", "wis", "wi", 
    "software", "soft", "engineer", "eng", "swe", "computer", "comp", "science",
    "sci", "java", "cpp", "python", "py", "csharp", "jscript", "php",
    "jane", "doe", "wife", "april", "04",
    "01", "1989", "89", "love", "secret", "god"
    ]

"""
Constructing random passwords from passFrag and checking 
that requirements for length and prior membership of dataframe
are met. If all requirements are met then the password and it's 
hash are stored in the dataframe.
"""
# Declaring number of possible password combinations based on fragments above
numPossibilities = 13500

# Empty DataFrame to store passwords and hash values in later
# df = pd.DataFrame(columns = ['Password', 'Hash Value'])

# Read Dataframe from old csv
df = pd.read_csv('rainbow.csv')

# Function to generate random passwords 
def generateRandPass(passFrag, numFragments):
    # Pull random sample of a specific number of fragments
    randomFrag = random.sample(passFrag, numFragments)
    # Construct new password from sample above
    newPassword = ""
    for i in range(0,numFragments):
        newPassword += randomFrag[i]
    return newPassword

# Generating new passwords and storing them and their hash value in DataFrame
while len(df) < numPossibilities:
    # Generate new password assuming you can have up to three fragments
    newPass = generateRandPass(passFrag, random.randint(1,3)) # Randomly choosing fragment size
    
    # Statement to check if password is the correct length between 5 and 8 characters
    if (len(newPass) >= 5 and len(newPass) <= 8):
        # Check if password is already in DataFrame
        if newPass not in df.values:
            # Create hash for new password
            myNewHash = hashlib.md5(newPass.encode("ascii"))
            
            # Appending New Password and Hash onto DataFrame
            df = df.append({'Password' : newPass, 'Hash Value' : myNewHash.hexdigest()}, ignore_index = True)
            print(len(df))
            
# Generating CSV File from DataFrame
df.to_csv('rainbow.csv',index=False)
            
# Comparing hash values in DataFrame to known hash value and storing matching passwords in list
matchIndexList = df.index[df['Hash Value'] == knownHash].tolist()
potentialPasswords = []

 
for i in range(0,len(matchIndexList)):
   potentialPasswords.append(df.at[matchIndexList[i], 'Password'])
   print("Potential Password:" , potentialPasswords[i])
    