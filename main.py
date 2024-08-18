# Following tutorial from https://www.youtube.com/watch?v=s-Ga8c3toVY&list=PLs3IFJPw3G9Jwaimh5yTKot1kV5zmzupt&index=10
# This is BEST USED when hiding individual actions using '''

import pyrebase

firebaseConfig = {"apiKey": "AIzaSyD2mFSY8V7rZVk6JuhyEzzAgNNszkNhmKo",
  "authDomain": "my-first-firebase-projec-277dd.firebaseapp.com",
  "projectId": "my-first-firebase-projec-277dd",
  "storageBucket": "my-first-firebase-projec-277dd.appspot.com",
  "messagingSenderId": "1061313522723",
  "appId": "1:1061313522723:web:65610c6175937212d3d596",
  "measurementId": "G-BRHMVJ515R",
  "databaseURL": "https://my-first-firebase-projec-277dd-default-rtdb.firebaseio.com/"}
# Copy this from the web app link on console.firebase.google.com, make sure they are strings "", these are your firebase
# configuration credentials. databaseURL is not given in the copy and paste, create a new database in the Realtime
# database tab and copy the url given

firebase = pyrebase.initialize_app(firebaseConfig)
# This initializes an app with the given configuration credentials copied aboved. This creates an app to your firebase proj

# Initialize these variables so you can use them to interact with different components on firebase
db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()

'''
# AUTHENTICATION
# Login: (only works with emails/passwords already registered)
email = input("Enter your email: ")
password = input("Enter your password: ")
try: # Runs the following code if no errors
    auth.sign_in_with_email_and_password(email, password)
    print("You have successfully logged in!")
except: # Runs the following code if there are errors
    print ("Invalid email or password. Please try again.")

# Signup: (creates a new email/password)
email = input("Enter your email: ")
password = input("Create your password: ")
confirmpassword = input("Confirm your password: ")
if password == confirmpassword:
    try:
        auth.create_user_with_email_and_password(email, password)
        print("You have successfully created your account!")
    except: # If an email is already registered, it will not create a new user. Try code failed
        print("This email is already used. Please try again.")
else:
    print("Your password does not match. Please try again")


# STORAGE *changed False to True on the rules tab on firebase*
# Upload: (store a file onto the root storage folder or into subfolders)
filename = input("Enter the name of the file that you would like to store: ")  # Make sure to include the .txt
cloudfilename = input("Enter the information for the file on the cloud (subfolders and/or file name): ")
# If you entered wiki/texts/loremipsumtext.txt it will create a folder called wiki with a subfolder called texts and
# that will contain the text file you named as loremipsumtext.txt
storage.child(cloudfilename).put(filename)
# The child method navigates to a specific path or "child" within the storage. In this case, cloudfilename represents 
# the name or path where you want to store the file in the cloud storage
print(f"\nYou have stored {filename} on to the cloud.")
print(f"URL to access stored file: {storage.child(cloudfilename).get_url(None)}")

# Download: (search for a file on the cloud and download it)
cloudfilename = input("Enter the file name you would like to download: ") # If stored in folders, add / to input
storage.child(cloudfilename).download("", "downloaded.txt")
print("Download complete.")
# Looks for cloudfilename in storage, no additional pathway needed so empty string "", names downloaded file

# Read: (read a file)
import urllib
cloudfilename = input("Enter the file name you would like to open: ") # Must be file name on cloud
url = storage.child(cloudfilename).get_url(None)
readfile = urllib.request.urlopen(url).read()
print(readfile) # THIS DOESN'T WORK, MAYBE OLD VERSION OF PYTHON OR SSL CERTIFICATE PROBLEM'''


# DATABASE
