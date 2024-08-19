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
print(readfile) # THIS DOESN'T WORK, MAYBE OLD VERSION OF PYTHON OR SSL CERTIFICATE PROBLEM


# DATABASE
# Create: (add/create data into the database)
data = {"age":35, "city":"Toronto", "employed":True, "name":"John Smith"}
db.child("users").push(data) # Creates a child/subfolder called users and stores each key object inside
# Without the .child(subfolder name), the key objects would be stored in the root folder. Can also ADD more .childs
# However this creates a new id for the set of data, regardless of if its in a subfolder or not
data = {"age":28, "city":"New York", "employed":True, "name":"Jane Smith"}
db.child("users").child("myownid").set(data)
# This allows for the subfolder with the data to be called myownid rather than a randomly generated id

# Update: (update data in the database)
db.child("users").child("myownid").update({"name":"Olivia Green"})
# Follows pathway, finds the corresponding key, updates changes. If key doesn't exist, it will create a new one
# What if you don't know the id or child name:
people = db.child("users").get()   # Store each user in a variable
for person in people.each():   # Go through each user
  if person.val()["name"] == "Olivia Green":    # If the data under the key "name" is Olivia Green (.val = data)
    db.child("users").child(person.key()).update({"name":"Jane Smith"})
    # Follows pathway to update name (.key = id/child name)

# Delete: (remove data in the database)
db.child("users").child("manualperson").child("age").remove()  # Works when you know the child/id name
# What if you don't know the id or child name:
people = db.child("users").get()   # Store each user in a variable
for person in people.each():   # Go through each user
  if person.val()["name"] == "Pip":   # If user's name is Pip
    db.child("users").child(person.key()).child("age").remove()   # Takes key (id), follows pathway, removes age data'''

# Read: (open data in the database)
# To optimize query performance, you should change the rules for the Realtime Database on Firebase. Add: "users": {
# .indexOn":["age", "city", "name", "employed"]} Firebase creates an index for the specified fields, that filters/sort
# these fields. Without indexing, Firebase would have to scan through all the data to satisfy the query, which is slow
people = db.child("users").order_by_child("name").equal_to("Ravi").get()
# Order each user by name and only get users with a name equal to Ravi
for person in people.each():   # For each person who passed through above code
  print (person.val()["age"])   # Prints only their ages

people = db.child("users").order_by_child("age").start_at(30).get()
# Order each user by age and only get users with age of at least 30
for person in people.each():
  print (person.val())
# You can add .end_at(int) after the .start_at(int) to get an age range filter

people = db.child("users").order_by_child("employed").equal_to(True).limit_to_first(1).get()
for person in people.each():
  print (person.val()["name"])
# .limit_to_first(int) only retrieves the first number of results. .limit_to_last(int) does the opposite