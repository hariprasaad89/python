#reading the file
with open ("/testFile.txt",'r') as rdfile:
    content=rdfile.readlines()
with open ("/outputtestFile.txt","w") as fp:
    line2 = "line5"
    for line in content:
        if  line.strip() != line2.strip():
            
                fp.writelines(line)
        else:
            print(line)
        
     