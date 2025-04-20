import os

directory_path="/home/sudo-mdsazib/Documents/Programing World/Python/Learning Myself"
content=os.listdir(directory_path)
for item in content:
    print(item)