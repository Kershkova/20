my_text_file = open("file.txt", "x")
my_text_list = ['File with entered text']
for i in my_text_list:
    k = str(input("Введіть рядок: "))
    if k == "" or k == " ":
        break
    my_text_list.append(k)
print(my_text_list)
file = open('file.txt', 'w')
for line in range(0, len(my_text_list)):
    file.write(my_text_list[line]+"\n")
file.close()


