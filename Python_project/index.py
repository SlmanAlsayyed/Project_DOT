from flask import Flask, render_template
import re
# import numpy
import os

#------------------------------------------------
#This program is a small store can display ,add ,decrese Quantity,simple GUI in(Webpage)
#auto add and remove and update in file without any interact with file
#------------------------------------------------
#if i have more time i can use 'numpy' to make a simple study on sales and its presentation it in bars :)


app = Flask(__name__)
def clear_file():
    with open('store.txt','w') as file:
        file.write('')
        file.close()
def clear_screen():
    os.system('cls')

#use Regex to read data from the file and return it
def read_data_from_file(x):
    with open('store.txt', 'r') as file:
        data = file.read()
    patt = re.compile(rf"{x}\s*(.*)")
    matches = patt.findall(data)
    return matches

#Sort data using my logic in dictionary and return it
def sort_iteams(lis):
    dic = {}
    x=read_data_from_file(lis[0])
    x1=read_data_from_file(lis[1])
    x2=read_data_from_file(lis[2])
    x3=read_data_from_file(lis[3])
    x4=read_data_from_file(lis[4])
    for i in range(0,len(x)):
        dic[x[i]] = [ x1[i],x2[i],x3[i],x4[i] ]
    return dic

#Function to display all Data from Dictionary
def show_iteams(lis):
    iteams={}
    iteams = sort_iteams(lis)
    for key, value in iteams.items():
        print(f"ID:{key} --> Name : {value[0]} | Price : {value[1]} | Qyn : {value[2]} | Selling : {value[3]} | Remaining : {int(value[2])-int(value[3])}")

#Function to add an iteam in that file
def add_iteam():
    with open('store.txt', 'r') as file:
        data = file.read()
    patt = re.compile(r"Iteam*(.*)")
    matches = patt.findall(data)
    file.close()
    
    name=input("Enter The Name of iteam : ")
    price= input("Enter The price of iteam : ")
    qyn = input("Enter The Quantity of iteam : ")

    
    
    with open('store.txt', 'a') as file:
            file.write(f"Iteam: {len(matches)+1}\n")
            file.write(f"Name: {name}\n")  
            file.write(f"Price: {price}\n")
            file.write(f"Quantity: {qyn}\n")
            file.write(f"Selling: 0\n\n")
            file.close()
    print("Succfuly add an iteam!")

#function to handle content of file when make decrese to specfic iteam
def sell_iteam(lis):
    iteams = {}
    iteams = sort_iteams(lis)
   
    id = input("Enter the id of iteam : ")
    if int(iteams[f'{id}'][2]) > 0  :
        iteams[f'{id}'][2] = int(iteams[f'{id}'][2])-1
        iteams[f'{id}'][3] = int(iteams[f'{id}'][3])+1
        clear_file()
        for key, value in iteams.items():
            with open('store.txt', 'a') as file:
                    file.write(f"Iteam: {key}\n")
                    file.write(f"Name: {value[0]}\n")  
                    file.write(f"Price: {value[1]}\n")
                    file.write(f"Quantity: {value[2]}\n")
                    file.write(f"Selling: {value[3]}\n\n")
                    file.close()
    else:
        print("The Qyn is Zero !")
    lis = ["Iteam:","Name:","Price:","Quantity:","Selling:"]
    sell_iteam(lis)


#function to make local host and run html file using flask
def run_web_app(lis):
    app = Flask(__name__)
    @app.route('/')
    def index():

        dic= {}
        
        dic = sort_iteams(lis)
        return render_template('index.html', iteams=dic)

    if __name__ == "__main__":
        app.run(debug=False)




while True:
    lis = ["Iteam:","Name:","Price:","Quantity:","Selling:"]
    print("---------------------")
    print("   Control Panel     ")
    print("---------------------")
    print("1- Display all iteams")
    print("2- Add an iteam")
    print("3- Sell an iteam")
    print("4- Run webpage To show with GUI")
    print("5- Exit")
    choose = input("Enter Here -->")
    if choose == '1':
        #This will display all iteams from the file 'store.txt'
        clear_screen()
        print("------------------")
        print("------Iteams------")
        print("------------------")
        show_iteams(lis)
    if choose == '2':
        #this will add an iteam to the store 
        clear_screen()
        add_iteam()
    if choose == '3':
        #this will decrese one from the specfic iteam
        clear_screen()
        sell_iteam(lis)
    if choose == '4':
        #this will make local webpage and show all iteams with GUI
        clear_screen()
        run_web_app(lis)
    if choose == '5':
        #for exit
        clear_screen()
        print("- Good Bye -")
        break