# write code here
try:
    with open("text_file.txt", "w") as f:
        f.write("Hello, Good Morning!!!")
except IOError:
    print("Error working with file...")
else:
    print("File written successfully")