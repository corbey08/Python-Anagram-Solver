x = input("Enter Word 1: ")
y = input("Enter Word 2: ")

x_list = []
y_list = []

for char in x:
    if char == " ":
        continue
    else:
        x_list.append(char.lower())

for char in y:
    if char == " ":
        continue
    else:
        y_list.append(char.lower())

x_list = sorted(x_list)
y_list = sorted(y_list)

if x_list == y_list:
    print("Anagrams")
else:
    print("Not anagrams")