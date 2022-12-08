import numpy as np
import glob
import os

def levenshtein(seq1,seq2):
    size_x = len(seq1)+1
    size_y = len(seq2)+1
    
    matrix = np.zeros((size_x,size_y))
    
    for x in range(1,size_x):
        matrix[x,0]=x
    for y in range(1,size_y):
        matrix[0,y]=y
    for x in range(1,size_x):
        for y in range(1,size_y):
            if seq1[x-1]==seq2[y-1]:
                matrix[x,y]=min(matrix[x-1,y]+1,matrix[x-1,y-1],matrix[x,y-1]+1)
            else:
                matrix[x,y]=min(matrix[x-1,y]+1,matrix[x-1,y-1]+1,matrix[x,y-1]+1)
    return (matrix[size_x-1,size_y-1])    

k=0

print("Enter 1 for checking folders\n")
print("Enter 2 for checking between two files:\n")
choice=int(input())

if (choice==1):
    
    plag=int(input("percent of plagarism allowed"))
    path1=input("path of the folder to scan:\n")
    os.chdir(path1)
    
    myFiles=glob.glob('*.txt')
    print("\nThe files available are:\n")
    print(myFiles)
    
    path=input("\nEnter master file path:\n")
    with open(path,'r') as file:
        data=file.read().replace('\n','')
        str1=data.replace(' ','')
    print("\nplagarized files are:")
    for i in range(len(myFiles)):
        with open(myFiles[i],'r') as file:
            data=file.read().replace('\n','')
            str2=data.replace(' ','')
        if(len(str1)>len(str2)):
            length=len(str1)
        else:
            length=len(str2)
            
        n=100-round((levenshtein(str1,str2)/length)*100,2)
        
        if (n>plag):
            print(path,"and",myFiles[i],n,"% plagarized")
            k=k+1
    if(k==0):
        print("no plagarized")
    
    
elif(choice==2):   
    
    
    plag=int(input("percent of plagarism allowed"))
    path2=input("path of 1st file:\n")
    path3=input("path of 2nd file:\n")
    with open(path2, 'r') as file:
        data=file.read().replace('\n', '')
        str1=data.replace(' ', '')

    with open(path3, 'r') as file:
        data=file.read().replace('\n', '')
        str2=data.replace(' ', '')

    if(len(str1)>len(str2)):
        length=len(str1)
    else:
        length=len(str2)

    n=100-round((levenshtein(str1,str2)/length)*100,2)
    if(n>plag):
        print("\n For the files",path2,"and",path3,n,"% similarity")
    else:
        print("\nSimilarity are below given level")
        
