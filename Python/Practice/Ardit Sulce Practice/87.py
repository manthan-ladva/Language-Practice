checklist = ["Portugal", "Germany", "Spain"]

with open("87countriesmissing.txt", 'r') as file:
    content = file.readlines()
content = [i.rstrip("\n") for i in content]

all_list = sorted(content + checklist)

with open("87countries_with_missing.txt", 'w') as file:
    for i in all_list:
        file.write(i + '\n')
