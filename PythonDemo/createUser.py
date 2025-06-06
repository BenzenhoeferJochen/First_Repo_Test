import subprocess

user_name = input("Please input a username for the new user.\n")
subprocess.run(["sudo", "useradd", "-m", user_name])
delete_user = input("Delete User?.\n")
if delete_user:
    subprocess.run(["sudo", "userdel", "-fr", user_name])


print("Done")
