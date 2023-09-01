# forename = input('Skriv in ditt namn: ')
# print('Hej'+ forename)
# surename = input('Skriv in ditt efternamn: ')
# print('Välkommen '+ surename + forename)
import math                                               
tal1 = int(input("Skriv in ett tal"))  
# tal1 --> 22 --> rount(22,2) --> math.sqrt()
roten_ur_talet = math.sqrt(tal1)
avrundat = round(roten_ur_talet,2)            
print(avrundat)             
# varför rundar inte denna kod av decimalerna till 2st?