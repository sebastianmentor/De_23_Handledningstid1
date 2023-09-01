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
#----------------------------------------------------------
# användaren_mata_in = '55'

# if användaren_mata_in.isnumeric() == True:
#     tal1 = int(användaren_mata_in)
# else:
#     print('Du mata in fel! Programmet stängs av!')
#     tal1 = None

# if tal1 != None:
#     print(tal1**2)
#----------------------------------------------------------

# while True:
#     try:
#         summa_pengar = int(input("Hur mycket pengar har du?"))
#         break
#     except ValueError:
#         print("Svara med endast siffror")
#----------------------------------------------------------

# if 5 == 5:
#     pass 

# if 5 != 5:
#     pass 
#----------------------------------------------------------

# delat = (150-190)/190 # Ursprungsvärde på 190 , ökat till 230 , 230-190=40

# print(f'Den procentuella förändringen är {delat:>30}')
#----------------------------------------------------------
# tal = 24

# print(23 > tal)
#----------------------------------------------------------
# nummer1 = int(input("Mata in ett tal: "))
# nummer2 = int(input("mata in ett tal: "))
# nummer3 = int(input("Mata in ett tal: "))

# if nummer1 > nummer2 :
#     largets = nummer1 # --> nummer1 > nummer2 och nummer3
#     if nummer3 > nummer1: # --> nummer3 > nummer1 > nummer2
#         largets = nummer3
# else: # nummer2 > nummer1
#     largets = nummer2 # --> nummer2 > nummer1 och nummer3
#     if nummer3 > nummer2: # -- nummer3 > nummer2 > nummer1
#         largets = nummer3

# print("Största talet är " , int(largets))
#----------------------------------------------------------
# nummer1 = int(input("Mata in ett tal: "))
# nummer2 = int(input("mata in ett tal: "))
# nummer3 = int(input("Mata in ett tal: "))

# # nr1 = 4 , nr2 = 3 , nr3 = 2
# if nummer1 > nummer2:
#     if nummer1 > nummer3:
#         largets = nummer1 # --> nummer1 > nummer2 och nummer3
#     if nummer3 > nummer1:
#         largets = nummer3 # --> nummer3 > nummer2 och nummer1
# else: # nummer2 > nummer1
#     if nummer3 > nummer2: # -- nummer3 > nummer2 > nummer1
#         largets = nummer3
#     else:
#         largets = nummer2 # --> nummer2 > nummer1 och nummer3

# print("Största talet är " , int(largets))
#----------------------------------------------------------