#10 deneme hakkı ile bilgisayarın belirlemiş olduğu sayiyi bulma.

import random
i = 0                                                                                  

for i in range(1):               
    r = random.randint(0, 100)                                                        #random.randint(a,b) ifadesi a ile b arasında rastgele sayı seçmesine yarar.
while i <= 10 :                                                                       #Bu döngünün çalışabilmesi için i ifadesinin 10'Dan küçük olması gerekmektedir.
    if i < 10:
        sayi = int(input("Sayi giriniz :"))
        if sayi == r:                            
            print("Sayiyi buldunuz. Bilgisayarın seçtiği sayi {}".format(sayi))
            i +=1                                                                     #i+=1 ifadesi her denemenizde yukarıda girilen i=0 değerine 1 ekleyecektir.
            break
        elif sayi < r:
            print(" Vermiş olduğunuz sayi küçüktür {} ".format(sayi))
            i+=1
        elif sayi > r:
            print("Vermiş olduğunuz sayi büyüktür {}" .format(sayi)) 
            i+=1
    elif i == 10:                                                                      #i ifadesi 10'a eşit olduğunda while döngüsü kırılacak ve program duracaktır.
        print("Hakkiniz tükendi. istenilen sayi {} ".format(r))
        i +=1
        break
