import os
from time import sleep
def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')
sleep(2)
screen_clear()

from matplotlib import pyplot as plt, use
from tabulate import tabulate
import numpy as np

class plant(object):
    #constructor
    def __init__(self, name, num,detail):
        self.name = name
        self.num = num
        self.detail=detail
    #to display data
    def display(self, ob):
        print(ob.detail)
    #to display graph
    def graph(self ,num):
        if(self.num==1):
                w=0.1
                x= ["Aio2g12737","Aio2g12807","Aio2g12732","Aio2g12712","Aio2g12732","Aio2g12732","Aio2g127122","Aio2g127374"]
                Leaf=[10,9,1020,2,4,1,1,2]
                Callus=[0,0,900,0,0,10,0,12]
                s1=[10,9,1020,2,4,1,1,2]
                s2=[23,412,900,23,31,140,21,122]
                s3=[132,931,1020,232,32,331,321,32]
                s4=[440,110,300,110,120,102,321,12]
                bar1=np.arange(len(x))
                bar2=[i+w for i in bar1]
                bar3=[i+2*w for i in bar1]
                bar4=[i+3*w for i in bar1]
                bar5=[i+4*w for i in bar1]
                bar6=[i+5*w for i in bar1]
                plt.bar(bar1,Leaf,w,label="Leaf")
                plt.bar(bar2,Callus,w,label="Callus")
                plt.bar(bar3,s1,w,label="s1")
                plt.bar(bar4,s2,w,label="s2")
                plt.bar(bar5,s3,w,label="s3")
                plt.bar(bar6,s4,w,label="s4")
                plt.xlabel("Gene Id")
                plt.ylabel("Fold change (log10)")
                plt.title("Need Gene Id")
                plt.legend()
                plt.xticks(bar1,x)
                plt.show()
        elif(self.num==2):
                w=0.4
                x= ["2014","2015","2016","2017","2018","2019"]
                production=[12,13,15,17,17,18]
                consumption=[10,11,13,14,15,16]
                bar1=np.arange(len(x))
                bar2=[i+w for i in bar1]
                plt.bar(bar1,production,w,label="production")
                plt.bar(bar2,consumption,w,label="consumption")
                plt.xlabel(" consumption and production")
                plt.ylabel("Million Tonnes")
                plt.title("World Natural Rubber year wise Consumption and Production")
                plt.legend()
                plt.xticks(bar1,x)
                plt.show()
        elif(self.num==3):
                w=0.2
                x= ["Tulsi 0.5%","Tulsi 1.0%","Tulsi 2.0%","Tulsi 5.0%","Tulsi 10%"]
                AA=[15.5,22.4,29,38.25,41]
                PG=[12,16.75,16.25,18,21]
                PI=[12.25,14.75,18.25,18.25,22.75]
                bar1=np.arange(len(x))
                bar2=[i+w for i in bar1]
                bar3=[i+2*w for i in bar1]
                plt.bar(bar1,AA,w,label="AA")
                plt.bar(bar2,PG,w,label="PG")
                plt.bar(bar3,PI,w,label="PI")
                plt.xlabel("Amount of Tulsi")
                plt.ylabel("in millimeters")
                plt.title("Comparison of mea inhibition zone against AA,PG and PI")
                plt.legend()
                plt.xticks(bar1,x)
                plt.show()
        elif(self.num==4):
                pass
        elif(self.num==5):
                w=0.4
                x= ["2014","2015","2016","2017"]
                Powder=[100,20,120,200]
                Gels=[200,20,420,212]
                plt.bar(x,Powder,w,label="Powder")
                plt.bar(x,Gels,w,bottom=Powder,label="Gels")
                plt.xlabel("Year")
                plt.ylabel("Market Value(USD Million)")
                plt.title("Aloe vera consumption in cosmetics and medicines")
                plt.legend()
                plt.show()
        elif(self.num==6):
             pass


    def change(self,num,s):
            self.detail+=" "
            self.detail+=s
            return
    def add(name,detail):
         pass
        


                

   




obj1 = plant("Neem",1,"Details - \n Azadirachta indica, commonly known as neem, nimtree or Indian lilac, and in Nigeria called dogoyaro or dogonyaro, is a tree in the mahogany family Meliaceae.\n It is one of two species in the genus Azadirachta, and is native to the Indian subcontinent and most of the countries in Africa.\n Amount of Plantation - It is typically grown in tropical and semi-tropical regions.\n Neem trees also grow on islands in southern Iran. Its fruits and seeds are the source of neem oil.Uses - Neem leaves are dried in India and placed in cupboards to prevent insects eating the clothes, and also in tins where rice is stored. The flowers are also used in many Indian festivals like Ugadi.Effect on Environment - In 1995, the European Patent Office (EPO) granted a patent on an anti-fungal product derived from neem to the United States Department of Agriculture and W. R. Grace and Company. The Indian government challenged the patent when it was granted, claiming that the process for which the patent had been granted had been in use in India for more than 2,000 years.")
obj2 = plant("Rubber_tree",2,"Details - \n Rubber tree, (Hevea brasiliensis), South American tropical tree of the spurge family (Euphorbiaceae). It has soft wood; high, branching limbs; and a large area of bark. The milky liquid (latex) that oozes from any wound to the tree bark contains about 30 percent rubber, which can be coagulated and processed into solid products, such as tires.Amount of plantation:  Cultivated on plantations in the tropics and subtropics, especially in Southeast Asia and western AfricaUses: It is used in producing dipped goods, such as surgical glovesEffect: Over half of these plantations are in areas which are susceptible to insufficient water availability and soil erosion. Scientists have also linked rubber monoculture to reduction in water reserves, soil productivity and biodiversity in South-East Asia.")
obj3 = plant("Tulsi",3,"Details - \n Ocimum tenuiflorum, commonly known as holy basil or tulsi, is an aromatic perennial plant in the family Lamiaceae. It is native to the Indian subcontinent and widespread as a cultivated plant throughout the Southeast Asian tropics. Amount of Plantation - The three main morphotypes cultivated in India and Nepal are Ram tulsi (the most common type, with broad bright green leaves that are slightly sweet), the less common purplish green-leaved (Krishna or Shyam tulsi) and the common wild vana tulsi. Uses - Tulsi (Sanskrit:-Surasa) has been used in Ayurveda and Siddha practices for its supposed treatment of diseases. For centuries, the dried leaves have been mixed with stored grains to repel insects.Effect on Environment - Tulsi is a sacred plant for Hindus. It is worshipped as the avatar of Lakshmi, and may be planted in courtyards of Hindu houses or Hanuman temples. The ritual lighting of lamps each evening during Kartik includes the worship of the tulsi plant. Vaishnavas followers of Vishnu are known as those who bear the tulsi around the neck.")
obj4 = plant("Money_Plant",4,"Details - \n Epipremnum aureum is a species in the arum family Araceae, native to Mo orea in the Society Islands of French Polynesia. The species is a popular houseplant in temperate regions but has also become naturalised in tropical and sub-tropical forests worldwide, including northern South Africa, Australia, Southeast Asia, South Asia, the Pacific Islands and the West Indies, where it has caused severe ecological damage in some cases.Amount of Plantation - In 2021 an old vine with naturally occurring fruit was unofficially reported to have been found in South Florida which had infructescenses covered by green hexagonal scales approximately 3 mm (1/8 in) thick, which scales eventually peeled away to reveal an orange kernel fruit eaten by local wildlife (probably squirrels) and having an odor similar to a ripe cantaloupe melon.Uses - The plant can remove indoor pollutants such as formaldehyde, trichloroethene, toluene, xylene, and benzene in controlled circumstances (e.g. a sealed room). A study found that this effect declined as the molecular weight of the polluting substance increased. Effect on Environment - The plant is listed as toxic to cats and dogs by the ASPCA, because of the presence of insoluble raphides. Care should be taken to ensure the plant is not consumed by pets. Symptoms may include oral irritation, vomiting, and difficulty in swallowing.")
obj5 = plant("Aloe_vera",5,"Details - \n Aloe vera is a succulent plant species of the genus Aloe.[3] Having some 500 species, Aloe is widely distributed, and is considered an invasive species in many world regions.Amount of Plantation: An evergreen perennial, it originates from the Arabian Peninsula, but grows wild in tropical, semi-tropical, and arid climates around the world. There is large-scale agricultural production of Aloe vera in Australia,[40] Cuba, the Dominican Republic, China, Mexico,[41] India,[42] Jamaica,[43] Spain, where it grows even well inland,[44] Kenya, Tanzania, and South Africa,[20] along with the USA[46] to supply the cosmetics industry.[3] Uses: It is used in many consumer products, including beverages, skin lotion, cosmetics, ointments or in the form of gel for minor burns and sunburns. There is little clinical evidence for the effectiveness or safety of Aloe vera extract as a cosmetic or topical drug.Effect: Aloe vera helps to clear the air of dangerous carcinogens including benzene and formaldehyde. Unlike most plants, aloe releases oxygen and absorbs carbon dioxide during the night")
obj6 = plant("Peepal",6,"Details - \n Ficus religiosa or sacred fig is a species of fig native to the Indian subcontinent and Indochin] that belongs to Moraceae, the fig or mulberry family. It is also known as the bodhi tree,[4] pippala tree, peepul tree,[2] peepal tree, pipal tree,[citation needed] or ashvattha tree (in India and Nepal).Amount of Plantation - In the Middle East, it is preferably planted as an avenue or road verge tree. In the Philippines and in Nicaragua the species is cultivated in parks and along roadsides and pavements, while in Paraguay it occurs in forests at lower elevations.Uses - Ficus religiosa is used in traditional medicine for about fifty types of disorders including asthma, diabetes, diarrhea, epilepsy, gastric problems, inflammatory disorders, infectious and sexual disorders. Prayer beads are made from the seeds of Ficus religiosa, considered sacred because of the closeness to Buddha himself and his enlightenment.Effects on Environment - Ficus religiosa is tolerant to various climate zones (Köppen climate classification categories of Af, Am, Aw/As, Cfa, Cwa and Csa) and various types of soils. In Paraguay the tree species occurs in forests at lower elevations, and in China the species has been reported growing at altitudes ranging from 400 metres (1,300 ft) to 700 metres (2,300 ft). In India, being a native species, it occurs both naturally in wild as well as cultivated up to altitudes of 1,520 metres (4,990 ft).")
obj7 = plant("Maple",7,"Details - \n Acer is a genus of trees and shrubs commonly known as maples. The genus is placed in the family Sapindaceae.[1] There are approximately 132 species, most of which are native to Asia with a number also appearing in Europe, northern Africa, and North America. The maples usually have easily recognizable palmate leaves (Acer negundo is an exception) and distinctive winged fruits. The closest relatives of the maples are the horse chestnuts. Maple syrup is made from the sap of some maple species.Amount of Plantation: Many maples have bright autumn foliage, and many countries have leaf-watching traditions. The sugar maple (Acer saccharum) is the primary contributor to fall foliage season in North America.In Japan, the custom of viewing the changing colour of maples in the autumn is called momijigari. Nikko and Kyoto are particularly favoured destinations for this activity. In Korea, the same viewing activity is called danpung-nori and the Seoraksan and Naejang-san mountains are among the best-known destinations.Uses: Maple wood is commonly used in high-end furniture, flooring, cabinetry, and kitchen accessories. Because of its durability and strength, maple can be found used as flooring in bowling alleys and for bowling pins.Effect: the maple trees  in Québec capture the carbon produced by the equivalent of 290,000 cars in a year. That’s 9% of all cars in Québec.")
obj8 = plant("Mango",8,"Details - \n A mango is an edible stone fruit produced by the tropical tree Mangifera indica which is believed to have originated from the region between northwestern Myanmar, Bangladesh, and northeastern India.[1] M. indica has been cultivated in South and Southeast Asia since ancient times resulting in two distinct types of modern mango cultivars: the Indian type and the Southeast Asian type.[2][3] Other species in the genus Mangifera also produce edible fruits that are also called mangoes, the majority of which are found in the Malesian ecoregionAmount of Plantation: Worldwide, there are several hundred cultivars of mango. Depending on the cultivar, mango fruit varies in size, shape, sweetness, skin color, and flesh color which may be pale yellow, gold, green, or orange.[5] The mango is the national fruit of India, Pakistan and the Philippines,[6][7] while the mango tree is the national tree of Bangladesh.[8]Uses: Mangos have been an important crop in India for millennia. Today, these colorful, sweet fruits are a mainstay of Indian cuisine and are popular throughout the world. The vitamins, minerals, and antioxidants in mangos can provide important health benefits. For example, vitamin K helps your blood clot effectively and helps prevent anemia. It also plays an important role in helping strengthen your bones.Mangos are also rich in vitamin C, which is important for forming blood vessels and healthy collagen, as well as helping you heal.Effects: The use of agrochemicals (including fertilizers) and transport of mangos together account for approximately 60% of the industry's greenhouse gas emissions. produced for each kg of mango fruit produced. The majority of these emissions (57%) come from the production and use of agrochemicals, notably fertilizers.")
obj9 = plant("Mint",9,"Details - \n Mentha (also known as mint, from Greek μίνθα míntha,[2] Linear B mi-ta[3]) is a genus of plants in the family Lamiaceae (mint family).[4] The exact distinction between species is unclear; it is estimated that 13 to 24 species exist.[5][1] Hybridization occurs naturally where some species' ranges overlap. Many hybrids and cultivars are known.Amount of Plantation - The most common and popular mints for commercial cultivation are peppermint (Mentha × piperita), native spearmint (Mentha spicata), Scotch spearmint (Mentha x gracilis), and cornmint (Mentha arvensis);[13] also (more recently) apple mint (Mentha suaveolens). Mints are supposed to make good companion plants, repelling pesty insects and attracting beneficial ones. They are susceptible to whitefly and aphids.Uses - The leaf, fresh or dried, is the culinary source of mint. Fresh mint is usually preferred over dried mint when storage of the mint is not a problem. The leaves have a warm, fresh, aromatic, sweet flavor with a cool aftertaste, and are used in teas, beverages, jellies, syrups, candies, and ice creams. Menthol from mint essential oil (40–90%) is an ingredient of many cosmetics and some perfumes. Menthol and mint essential oil are also used in aromatherapy which may have clinical use to alleviate post-surgery nausea.Effects on Environment - Mentha pliocenica fossil seeds have been excavated in Pliocene deposits of Dvorets on the right bank of the Dnieper river between the cities of Rechitsa and Loyew, in south-eastern Belarus. The fossil seeds are similar to the seeds of Mentha aquatica and Mentha arvensis.")
ls=[]
new=9
i=1  
# ls=[["Neem","Rubber_tree","Tulsi"],["MoneyPlant","Aloe_Vera","Peepal"],["Maple","Mango","Mint"]]
mydata = [["1", "Neem"],  ["2", "Rubber tree"], ["3", "Tulsi"],  ["4", "Money plant"],["5", "Aloe Vera"], ["6", "Peepal"],   ["7", "Mapple"], ["8", "Mango"],["9", "Mint"]]
num=1
while  i>0: 
 print("-----------------------------------------------------------------------------------------")
 head = ["S.no", "Name"]
  
  # display table
 print(tabulate(mydata, headers=head, tablefmt="grid"))
 if new>9:
     print("Newly added data: ")
     print(" ")
     for obj in ls:
         print(" ",obj.num," ",obj.name," ",obj.detail)
      
#  for i in range(3):
#     for j in range(3):
#        print("   ",ls[i][j],end=" ")  
#        num=num+1
#     print("\n")

    
 print("-----------------------------------------------------------------------------------------")
 print("\n---Choices---\n\n1. About\n\n2. Plantation graphs\n\n3. Add information\n\n4. Add a plant\n\n5. Exit\n\n")
 user=int(input("<---Enter a choice----> "))
 print("-----------------------------------------------------------------------------------------")

 
 if user==5:
     break
 elif user==1:
    plant_num=int(input("Which Plant : "))
    if plant_num==1:
        sleep(2)
        screen_clear()
        obj1.display(obj1)
        sleep(20)
        screen_clear()
    elif plant_num==2:
        sleep(2)
        screen_clear()
        obj2.display(obj2)
        sleep(20)
        screen_clear()
    elif plant_num==3:
        sleep(2)
        screen_clear()
        print("\n")
        obj3.display(obj3)
        sleep(20)
        screen_clear()
    elif plant_num==4:
        sleep(2)
        screen_clear()
        obj4.display(obj4)
        sleep(20)
        screen_clear()
    elif plant_num==5:
        sleep(2)
        screen_clear()
        obj5.display(obj5)
        sleep(20)
        screen_clear()
    elif plant_num==6:
        sleep(2)
        screen_clear()
        obj6.display(obj6)
        sleep(20)
        screen_clear()
    elif plant_num==7:
        sleep(2)
        screen_clear()
        obj7.display(obj7)
        sleep(20)
        screen_clear()
    elif plant_num==8:
        sleep(2)
        screen_clear()
        obj8.display(obj8)
        sleep(20)
        screen_clear()
    elif plant_num==9:
        sleep(2)
        screen_clear()
        obj9.display(obj9)
        sleep(20)
        screen_clear()
 elif user==2:
    graph_num=int(input("Which Plant : "))
    if graph_num==1:
        sleep(2)
        obj1.graph(1)
        screen_clear()
    elif graph_num==2:
        sleep(2)
        obj2.graph(2)
        screen_clear()
    elif graph_num==3:
        sleep(2)
        obj3.graph(3)
        screen_clear()
    elif graph_num==4:
        sleep(2)
        obj4.graph(4)
        screen_clear()
    elif graph_num==5:
        sleep(2)
        obj5.graph(5)
        screen_clear()
    elif graph_num==6:
        sleep(2)
        obj6.graph(6)
        screen_clear()
    elif graph_num==7:
        sleep(2)
        obj7.graph(7)
        screen_clear()
    elif graph_num==8:
        sleep(2)
        obj8.graph(8)
        screen_clear()
    elif graph_num==9:
        sleep(2)
        obj9.graph(9)
        screen_clear()
 elif user==3:
     plant_num=int(input("Which Plant : "))
     if plant_num==1:
        sleep(2)
        screen_clear()
        s=input("add line: ")
        obj1.change(plant_num,s)
        sleep(2)
        screen_clear()
     if plant_num==2:
        sleep(2)
        screen_clear()
        s=input("add line: ")
        obj2.change(plant_num,s)
        sleep(2)
        screen_clear()
     if plant_num==3:
        sleep(2)
        screen_clear()
        s=input("add line: ")
        obj3.change(plant_num,s)
        sleep(2)
        screen_clear()
     if plant_num==4:
        sleep(2)
        screen_clear()
        s=input("add line: ")
        obj4.change(plant_num,s)
        sleep(2)
        screen_clear()
     if plant_num==5:
        sleep(2)
        screen_clear()
        s=input("add line: ")
        obj5.change(plant_num,s)
        sleep(2)
        screen_clear()
     if plant_num==6:
        sleep(2)
        screen_clear()
        s=input("add line: ")
        obj6.change(plant_num,s)
        sleep(2)
        screen_clear()
     if plant_num==7:
        sleep(2)
        screen_clear()
        s=input("add line: ")
        obj7.change(plant_num,s)
        sleep(2)
        screen_clear()
     if plant_num==8:
        sleep(2)
        screen_clear()
        s=input("add line: ")
        obj8.change(plant_num,s)
        sleep(2)
        screen_clear()
     if plant_num==9:
        sleep(2)
        screen_clear()
        s=input("Add Line: ")
        obj9.change(plant_num,s)
        sleep(2)
        screen_clear()
         
 elif user==4:
    plant_nam=input("Name of the Plant : ")
    plant_detail=input("About Plant : ")
    new+=1
    new_obj=plant(plant_nam,new,plant_detail)
    ls.append(new_obj)
    sleep(2)
    screen_clear()
         
           
