#scrivere un programma per il calcolo di area di 4 rettangoli avendo base e altezza generati randomica
"senza la fuzione"
"""
import random
base_1=random.randint(1,20)
altazza_1=random.randint(1,20)
area_1=base_1*altazza_1
print(area_1)

base_2=random.randint(1,20)
altazza_2=random.randint(1,20)
area_2=base_2*altazza_2
print(area_2)

base_3=random.randint(1,20)
altazza_3=random.randint(1,20)
area_3=base_3*altazza_3
print(area_3)

base_4=random.randint(1,20)
altazza_4=random.randint(1,20)
area_4=base_4*altazza_4
print(area_4)
"""



#il sotto problema del calolo del area di un rettangolo e costituto da 2 imuput e un solo output area
"con procedura"
import random
def procedura_calcolo_area_rettangolo(base,altazza):
    area=base*altazza
    print(area)


if __name__ =='___main__':
    a=random.randint(0,20)
    b=random.randint(0,20)
    procedura_calcolo_area_rettangolo(a,b)
    

"con le funzioni"
def procedura_calcolo_area_rettangolo(base,altazza):
    area=base*altazza
    return(area)

if __name__ =='___main__':
    a2=random.randint(0,20)
    b2=random.randint(0,20)
    area=procedura_calcolo_area_rettangolo(a2,b2)
    print(area)
