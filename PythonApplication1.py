'''
Importing some important libararies,Like time which will be used                                        #student ID: F022796
to delay some outputs and leave proper time for the user to
read instructions and pandas to taransform the dataset into dataframe.
'''
import time
import pandas as pd

#In this project, I try to build a dataset of tarvelling destinations.
#Here is the popular Destinations to travel according to Tripadvisor website Worldwide.
# attached with average daily cost according to www.budjetyourtrip.com  .
pop_dest=[('Crete', 'Greece',62),('New York City', 'New York',144),('Kyoto', 'Japan',89),
              ('Tokyo', 'Japan',75),('Lisbon', 'Portugal',114),('Marrakech', 'Morocco',60),
              ('Bangkok', 'Thailand',70),('Dubai', 'United Arab Emirates',198),
              ('Istanbul', 'Turkey',25),('Barcelona', 'Spain',137),('Bali', 'Indonesia',65),
              ('Paris', 'France',94),('Phuket', 'Thailand',99),('Rome','Italy',115)]


#The user is asked to introduce himeslf/herself.
ans1=input("Hi,can you insert your name?\n",)
print('Welcome',ans1,'\n')

#Delay outputs for one second, So the user get to read the
#instructions easily.
time.sleep(1)

#Asking the user non sense questions ;). 
ans2=input("Do you have any plans ahead ?\n",)
time.sleep(1)
print('Never mind, we got plans for you ;) \n')
time.sleep(1)

#The show has started...In which the user will be asked a yes-no question type.  
#regardless if the answer is in upper case or lower case, the program tackles this issue with input().lower() format.  
#Then, he/she will be directed to the the next steps. 
#However, the user will be asked to input again if the answer is not yes or no.

while True:
    ans3 = input("What about traveling?(yes/no)").lower()
    if ans3=='yes':
        time.sleep(1)
        break
    elif ans3=="no":
        print("C'mon, we insist you try ")
        break
    else: 
        print("Please, enter either (yes/no) to continue")


#Then, the user will be asked to choose from specific set of numbers and each number result in a certian output.

while True:

    ans4 =input('Please, choose from: Add new destination [1],View all destinations [2], Pick randomly[3],\n Number of destinations[4], End[5]\n')
 # 1- To add new places with associated cost.
    if ans4 =='1':
        print(('Add more destinations').center(40,'='))
        time.sleep(1)
        x= input('City:')
        z=input('Country:')
        y=int(input('Cost per day: $ '))   
        result = [(x),(z),(y)]
        pop_dest.append(result)
        df=pd.DataFrame(pop_dest,columns=['City', 'Country','Cost_per_day'])
#2-View all the dataset in a dataframe format.       
    elif ans4 == '2':
        df=pd.DataFrame(pop_dest,columns=['City', 'Country','Cost_per_day'])
        print(df)       
#3- (Try your luck) option by using the sample() feature.     
    elif ans4 == '3':
       df=pd.DataFrame(pop_dest,columns=['City', 'Country','Cost_per_day'])
       print('Hint: try number *4* which shows the current number of destinations.\n')
       time.sleep(1.5)
       print('Cannot decide, we decide on behalf of you ;) \n')
       time.sleep(1.5)
       x=int(input('Enter a number and check your next destination/destinations ?\n'))
       luck=df.sample(n = x, replace = False)    
       print(luck)
#4- (Sum of the destination) option.
    elif ans4=='4':
        df=pd.DataFrame(pop_dest,columns=['City', 'Country','Cost_per_day'])
        print(len(df.index))

#5- The ending, amigo.
    elif ans4 == '5': 
        print('Have a nice trip, amigo')
        print('''
                                                  
                                  -/-                      
            0   0   0      -/-     
         ---|---|---|---------~~~~~~    
                
                  ''')

        break
#6-  
    else:
        print('Please, enter from 1 to 5 only')
        