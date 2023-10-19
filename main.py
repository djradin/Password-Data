import pickle
import os.path


passw = ""
login = {"user": "pass"}
signon = False
selection = ["read", "write"]
choice = ""
while not signon:
    user = input("Please enter your username")
    passw = input("Please enter your password")
    if user in login.keys() and passw in login.values():
        print("Login accepted.")
        signon = True

while choice not in selection:
    choice = input("Please select read or write.")
    if choice == "read" and os.path.isfile("data.txt"):
        print(pickle.loads("data.txt"))
    elif choice == "write":
        write = input("please write something to write into the file.")
        with open("data.txt", "wb") as file:
            pickle.dump(write, file)
