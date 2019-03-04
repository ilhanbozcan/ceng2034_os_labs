import os
import datetime
home_directory = (os.path.expanduser("~"))
os.chdir(home_directory)
try:
    os.mkdir("os_lab_0")
    print("*****    os_lab_0 has created!!!    *****")

    os.chdir("os_lab_0")
    open("1.txt", "a").close()
    open("2.txt", "a").close()
    open("3.py", "a").close()
    print("*****    1.txt and 2.py have created in os_lab_0    *****")

    print("*****    Last Modified Time    *****")

    for file in os.listdir(os.getcwd()):
        file_stat = os.stat(file).st_mtime
        file_modified = datetime.datetime.fromtimestamp(file_stat)
        print(file , " ======== " , file_modified)
    print("******  txt.files    *******")

    for i in os.listdir(os.getcwd()):
        if i.endswith(".txt"):
            print(i)
except FileExistsError:
    print("*****     os_lab_0 already exists    *****\n*****     Delete folder and try again ******")










