#Python program to help students with elements of periodic table
#program will diplay all the details of the element along with photos upon entering atomic number or the name of the element.
# It will with further provide students with a link to wikipedia for that particular element


import csv

#importing module to displayc picture of the given element along with its details
from tkinter import *
from PIL import ImageTk, Image


f=open("elements.csv", "r")
g=open("wiki.txt",'r')

data=csv.reader(f)
wiki=g.readlines()                        #this will convert links into list for easy access upon calling them

def eledetail():
    while True:

        elem=input("Enter the atomic number/ atom number you want to search for : \n")
        
        # if user entered atomic number :
        
        if elem.isdigit() :
            for i in data :
                if i[0]==elem:
                    print("Atomic number = ",i[0])
                    print("Element Name = ",i[1])
                    print("Atomic Symbol = ",i[2])
                    print("Atomic Mass = ",i[3])
                    print("Period,Group = ",i[4],",",i[5])
                    print("Phase = ",i[6])

                    # this portion only displays the given information if the element is radioactive else it will not be displayed
                    if i[7] in "":
                       pass
                    else:
                        print("It is a Radioactive element")
                    if i[8] in "":
                        pass
                    else:
                        print("It is naturally occuring element")

                        
                    print("Element type = ",i[9],"\n")
                    print("*-----------------------------------------------------------------------*-Physical properties of this element are-*--------------------------------------------------------------------------*\n")
                    print("Atomic radius = ",i[10])
                    print("Electronegativity = ",i[11])
                    print("Density = ",i[12])
                    print("Melting point = ", i[13])
                    print("Boiling point = ", i[14])
                    print("Number of isotopes = ",i[15])
                    imn=int(i[0])

                    # -1 to index list element according to syntax

                    linkk=wiki[imn]
                    print("For more information you can visit : ",linkk)

                    # to diplay the picture of the given elements.
                    

                    imn=str(imn)

                    path = imn + '.jpeg'     #setting path for image accordinfg to atomic number entered
                
                    window = Tk()

                    window.title(i[1])
    
                    canv = Canvas(window, width=520, height=195, bg='white')
                    canv.grid(row=2, column=3)
        
                    img = ImageTk.PhotoImage(Image.open(path))

                    canv.create_image(0, 0, anchor=NW, image=img)

    
                    window.mainloop()

               


#If user entered the name of the element
        elif elem.isalpha():

            elem=elem.capitalize()   # to make the inital letter capital in case used entered tha name all in lower case 
            for i in data :
                if i[1]==elem:
                    print("Atomic number = ",i[0])
                    print("Element Name = ",i[1])
                    print("Atomic Symbol = ",i[2])
                    print("Atomic Mass = ",i[3])
                    print("Period,Group = ",i[4],",",i[5])
                    print("Phase = ",i[6])
                    if i[7] in "":
                       pass
                    else:
                        print("It is a Radioactive element")
                    if i[8] in "":
                        pass
                    else:
                        print("It is naturally occuring element")
                    print("Element type = ",i[9],"\n")
                    print("*-----------------------------------------------------------------------*-Physical properties of this element are-*--------------------------------------------------------------------------*\n")
                    print("Atomic radius = ",i[10])
                    print("Electronegativity = ",i[11])
                    print("Density = ",i[12])
                    print("Melting point = ", i[13])
                    print("Boiling point = ", i[14])
                    print("Number of isotopes = ",i[15])
                    imn=int(i[0])

                    linkk=wiki[imn]
                    print("For more information you can visit : ",linkk)

                    imn=str(imn)

                    path = imn + '.jpeg'
                
                    window = Tk()

                    window.title(i[1])
    
                    canv = Canvas(window, width=500, height=195, bg='white')
                    canv.grid(row=2, column=3)

                    img = ImageTk.PhotoImage(Image.open(path))

                    canv.create_image(0, 0, anchor=NW, image=img)

    
                    window.mainloop()
        
#loop portion to run the program multiple times with user's choice taken in y/Y as yes or n/N as no 
        print("Do you want to dive more into the world of elements ?  (Y/N)  ")
        choice = input()
        if choice not in 'yY':
            break          



#call out the funtion to perform actions
eledetail()
   
f.close()
g.close()
