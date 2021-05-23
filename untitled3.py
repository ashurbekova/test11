# yosh = int(input('yoshingiz nechida?  '))
# if yosh<=7:
#     baho=0
# elif yosh<=17:
#     baho=50
# elif yosh<65:
#     baho=80
# else:
#         baho=25
# print(f"Sizga kirish {baho} tenge")
        
# kun = input("Bugun nima kun?>>>")
# if kun.upper()=='SHANBA' or kun.upper()=='YAKSHANBA':
#     print('Bugun dam olish kuni.')
# else:
#     print('Bugun ish kuni.')

# kun = input("Bugun haftaning qanday kuni?")
# harorat = float(input("havo harorati qanday")) 
# if kun.lower()=='yakshanba' and harorat>=30:
#     print("Cho'milgani kettik!")
# elif kun.lower()=='yakshanba' and harorat<30:
#     print("uyda dam olamiz!")
# else:
#     print('Ishga bor')
  
# narh = 1000 #мижоз 1000 тенгелик таом олди
# choy = True #мижоз чой хам олди
# salat = False #мижоз салат олмади

# if choy and salat: #мижоз чой хам салат хам олган булса
#     narh = narh + 500 #нархга 500 танга кушамиз
# elif choy or salat: #агар чой ёки салат олган булса 
#     narh = narh + 250 #нархга 250 кушамиз
    
# print(f"Jami  {narh}  t")
    

# narh = 1500 # mijoz 1500 so'mga ovqat oldi
# choy = True
# salat = True
# non = False
# kompot = False
# assorti = False
# #Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
# if choy:   # agar choy olsa
#     print("Mijoz choy oldi.")
#     narh = narh + 300
# if salat:  # agar salat olsa
#     print("Mijoz salat oldi.")
#     narh = narh + 500
# if non:    # agar non olsa
#     print("Mijoz non oldi.")
#     narh = narh + 200
# if kompot: # agar kompot olsa
#     print("Mijoz kompot oldi.")
#     narh = narh + 500
# if assorti: # agar assorti olsa
#     print("Mijoz assorti oldi.")
#     narh = narh + 1500
    
# print(f"Jami {narh} so'm")

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# 'manti' in menu # menu da manti bormi?
# Natija: False


# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# 'osh' in menu # menu da osh bormi?
# Natija: True

#12
# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# ovqat = input('Nima ovqat yeysiz?>>>')
# if ovqat.lower() in menu:
#     print('Buyurtma qabul qilindi.')
# else:
#     print('Afsuski bizda bunday ovqat yo\'q')

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]

# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"Menuda {taom} bor")
#     else:
#         print(f"Kechirasiz, menuda {taom} yo'q")
        
        
        
menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = ["osh","somsa","manti", "shashlik"]

if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
    for taom in buyurtmalar:
        if taom in menu:
            print(f"Menuda {taom} bor")
        else:
            print(f"Kechirasiz, menuda {taom} yo'q")
else: # agar ro'yxat bo'sh bo'lsa
    print("Savatchangiz bo'sh!")
    мен Усмантаев Сардорбек Мухаммадалиевич
    





