'''
Importing some important libarary,Like time which will be used                                        #student ID: F022796

to delay some outputs and leave proper time for the user to
read instructions
'''
import time
import pandas as pd
import numpy as np

pop_dest=[('Crete', 'Greece',62),('New York City', 'New York',144),('Kyoto', 'Japan',89),
              ('Tokyo', 'Japan',75),('Lisbon', 'Portugal',114),('Marrakech', 'Morocco',60),
              ('Bangkok', 'Thailand',70),('Dubai', 'United Arab Emirates',198),
              ('Istanbul', 'Turkey',25),('Barcelona', 'Spain',137),('Bali', 'Indonesia',65),
              ('Paris', 'France',94),('Phuket', 'Thailand',99),('Rome','Italy',115)]



df=pd.DataFrame(pop_dest,columns=['City', 'Country','Cost_per_day'], index=None)

#userIndex=int(input('Budget limit: '))
#if(userIndex >=50):

import matplotlib.pyplot as plt
import pandas as pd

# a simple line plot
df.plot(kind='bar',x='City',y='Cost_per_day')

