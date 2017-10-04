file = open("document.txt",'w')
file.write("Line 1\n")

l = ["Mona","Mota","Gaaja"]
for item in l:
    file.write(item + "\n")
file.close()
