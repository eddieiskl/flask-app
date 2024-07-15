file1 = open("requirements.txt", 'a')
current_dep = file1.write(input("enter new dependency: "))
file1.close()
file = open("requirements.txt", 'r')
for line in file.readlines():
    print(f"current dep is: {line}", end='')