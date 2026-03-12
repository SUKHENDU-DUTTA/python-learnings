import os
files = os.listdir("E:\MY MEMORY")
i=1
for file in files:
    if file.endswith(".jpg"):
        print(file)
        os.rename(f"E:\MY MEMORY/{file}",f"E:\MY MEMORY/{1}.jpg")
        i=i+1