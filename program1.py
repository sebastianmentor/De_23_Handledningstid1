# forename = input('Skriv in ditt namn: ')
# print('Hej'+ forename)
# surename = input('Skriv in ditt efternamn: ')
# print('Välkommen '+ surename + forename)
#----------------------------------------------------------
# import math                                               
# tal1 = int(input("Skriv in ett tal"))  
# # tal1 --> 22 --> rount(22,2) --> math.sqrt()
# roten_ur_talet = math.sqrt(tal1)
# avrundat = round(roten_ur_talet,2)            
# print(avrundat)             
# # varför rundar inte denna kod av decimalerna till 2st?
#----------------------------------------------------------
# rabatt = input("Har du rabatter? (Ja/Nej)").lower()
# ok = ["ja", "nej"]
# # if rabatt in ok:
# #     rabatt == 1
# # else:
# #     print("Du kan endast svara med 'Ja' eller 'Nej', försök igen.")
# if rabatt not in ok:
#     print('Skriv in igen')
# else:
#     if rabatt == "ja":

#         rabatt = 1

#     elif rabatt == "nej":

#         rabatt = 0
#----------------------------------------------------------
# rabatt = input("Har du rabatter? (ja/nej): ").lower()
# if rabatt == 'ja':
#     har_rabbat = True
# else:
#     har_rabbat = False

# if har_rabbat == True:
#     print("Vi ger rabatt!")
# else:
#     print("Du får ingen rabatt!")
#----------------------------------------------------------
# cash = 5
# if 15<= cash and cash < 25:     # 15<= cash < 25
#     discount = input("Do you have discount?: ")
#     if discount == "yes":
#       print("You can buy a small burger and fries")
#     else:
#        print("You can only buy a small burger")