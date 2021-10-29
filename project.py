import os
from time import sleep
def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')
sleep(2)
screen_clear()

from matplotlib import pyplot as plt
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
        if(1==self.num):
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
        elif(2==self.num):
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
        elif(3==self.num):
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
        elif(4==self.num):
                pass
        elif(5==self.num):
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
        elif(6==self.num):
             pass


    def change(self,num,s):
            self.detail+=" "
            self.detail+=s
            return
    def add(name,detail):
         pass
        


                

   




obj1 = plant("Neem",1,"\033[1;32;40mDetails - \n\nAzadirachta indica, commonly known as neem, nimtree or Indian lilac, and in Nigeria called dogoyaro or dogonyaro, is a tree in the mahogany family Meliaceae.\nIt is one of two species in the genus Azadirachta, and is native to the Indian subcontinent and most of the countries in Africa.\n\nAmount of Plantation - It is typically grown in tropical and semi-tropical regions.\n\nNeem trees also grow on islands in southern Iran. Its fruits and seeds are the source of neem oil.Uses - Neem leaves are dried in India and placed in cupboards to prevent\ninsects eating the clothes, and also in tins where rice is stored. The flowers are also used in many Indian festivals like Ugadi.\n\nEffect on Environment - In 1995, the European Patent Office (EPO) granted a patent on an anti-fungal product derived from neem to the United States Department of Agriculture and W. R. Grace and Company. The Indian government challenged the patent when it was granted, claiming that the process for which the patent had been granted had been in use in India for more than 2,000 years.")
obj2 = plant("Rubber_tree",2,"\033[1;32;40mDetails - \n\nRubber tree, (Hevea brasiliensis), South American tropical tree of the spurge family (Euphorbiaceae). It has soft wood; high, branching limbs; and a large area of bark. The\nmilky liquid (latex) that oozes from any wound to the tree bark contains about 30 percent rubber, which can be coagulated and processed into solid products, such as tires.\n\nAmount of plantation:  Cultivated on plantations in the tropics and subtropics, especially in Southeast Asia and western AfricaUses: It is used in producing dipped goods,\nsuch as surgical gloves.\n\nEffect: Over half of these plantations are in areas which are susceptible to insufficient water availability and soil erosion. Scientists have also linked rubber monoculture to reduction in water reserves, soil productivity and biodiversity in South-East Asia.")
obj3 = plant("Tulsi",3,"\033[1;32;40mDetails - \n\nOcimum tenuiflorum, commonly known as holy basil or tulsi, is an aromatic perennial plant in the family Lamiaceae. It is native to the Indian subcontinent and widespread as\na cultivated plant throughout the Southeast Asian tropics.\n\nAmount of Plantation - The three main morphotypes cultivated in India and Nepal are Ram tulsi (the most common type, with broad bright green leaves that are slightly sweet), the less common purplish green-leaved (Krishna or Shyam tulsi) and the common wild vana tulsi.\n\nUses - Tulsi (Sanskrit:-Surasa) has been used in Ayurveda and Siddha practices for its supposed treatment of diseases. For centuries, the dried leaves have been mixed with\nstored grains to repel insects.\n\nEffect on Environment - Tulsi is a sacred plant for Hindus. It is worshipped as the avatar of Lakshmi, and may be planted in courtyards of Hindu houses or Hanuman temples.\nThe ritual lighting of lamps each evening during Kartik includes the worship of the tulsi plant. Vaishnavas followers of Vishnu are known as those who bear the tulsi around\nthe neck.")
obj4 = plant("Money_Plant",4,"\033[1;32;40mDetails - \n\nEpipremnum aureum is a species in the arum family Araceae, native to Mo orea in the Society Islands of French Polynesia. The species is a popular houseplant in temperate\nregions but has also become naturalised in tropical and sub-tropical forests worldwide, including northern South Africa, Australia, Southeast Asia, South Asia, the Pacific Islands and the West Indies, where it has caused severe ecological damage in some cases.\n\nAmount of Plantation - In 2021 an old vine with naturally occurring fruit was unofficially reported to have been found in South Florida which had infructescenses covered by\ngreen hexagonal scales approximately 3 mm (1/8 in) thick, which scales eventually peeled away to reveal an orange kernel fruit eaten by local wildlife (probably squirrels)\nand having an odor similar to a ripe cantaloupe melon.\n\nUses - The plant can remove indoor pollutants such as formaldehyde, trichloroethene, toluene, xylene, and benzene in controlled circumstances (e.g. a sealed room). A study\nfound that this effect declined as the molecular weight of the polluting substance increased.\n\nEffect on Environment - The plant is listed as toxic to cats and dogs by the ASPCA, because of the presence of insoluble raphides. Care should be taken to ensure the plant\nis not consumed by pets. Symptoms may include oral irritation, vomiting, and difficulty in swallowing.")
obj5 = plant("Aloe_vera",5,"\033[1;32;40mDetails - \n\nAloe vera is a succulent plant species of the genus Aloe. Having some 500 species, Aloe is widely distributed, and is considered an invasive species in many world regions.\n\nAmount of Plantation: An evergreen perennial, it originates from the Arabian Peninsula, but grows wild in tropical, semi-tropical, and arid climates around the world. There\nis large-scale agricultural production of Aloe vera in Australia, Cuba, the Dominican Republic, China, Mexico, India, Jamaica, Spain, where it grows even well inland, Kenya, Tanzania, and South Africa, along with the USA to supply the cosmetics industry.\n\nUses: It is used in many consumer products, including beverages, skin lotion, cosmetics, ointments or in the form of gel for minor burns and sunburns. There is little\nclinical evidence for the effectiveness or safety of Aloe vera extract as a cosmetic or topical drug.Effect: Aloe vera helps to clear the air of dangerous carcinogens\nincluding benzene and formaldehyde. Unlike most plants, aloe releases oxygen and absorbs carbon dioxide during the night.")
obj6 = plant("Peepal",6,"\033[1;32;40mDetails - \n\nFicus religiosa or sacred fig is a species of fig native to the Indian subcontinent and Indochin] that belongs to Moraceae, the fig or mulberry family. It is also known as\nthe bodhi tree, pippala tree, peepul tree, peepal tree, pipal tree, or ashvattha tree (in India and Nepal).\n\nAmount of Plantation - In the Middle East, it is preferably planted as an avenue or road verge tree. In the Philippines and in Nicaragua the species is cultivated in parks\nand along roadsides and pavements, while in Paraguay it occurs in forests at lower elevations.\n\nUses - Ficus religiosa is used in traditional medicine for about fifty types of disorders including asthma, diabetes, diarrhea, epilepsy, gastric problems, inflammatory\ndisorders, infectious and sexual disorders. Prayer beads are made from the seeds of Ficus religiosa, considered sacred because of the closeness to Buddha himself and his\nenlightenment.\n\nEffects on Environment - Ficus religiosa is tolerant to various climate zones (Köppen climate classification categories of Af, Am, Aw/As, Cfa, Cwa and Csa) and various types of soils. In Paraguay the tree species occurs in forests at lower elevations, and in China the species has been reported growing at altitudes ranging from 400 metres\n(1,300 ft) to 700 metres (2,300 ft). In India, being a native species, it occurs both naturally in wild as well as cultivated up to altitudes of 1,520 metres (4,990 ft).")
obj7 = plant("Maple",7,"\033[1;32;40mDetails - \n\nAcer is a genus of trees and shrubs commonly known as maples. The genus is placed in the family Sapindaceae. There are approximately 132 species, most of which are native to Asia with a number also appearing in Europe, northern Africa, and North America. The maples usually have easily recognizable palmate leaves (Acer negundo is an exception)\nand distinctive winged fruits. The closest relatives of the maples are the horse chestnuts. Maple syrup is made from the sap of some maple species.\n\nAmount of Plantation: Many maples have bright autumn foliage, and many countries have leaf-watching traditions. The sugar maple (Acer saccharum) is the primary contributor\nto fall foliage season in North America.In Japan, the custom of viewing the changing colour of maples in the autumn is called momijigari. Nikko and Kyoto are particularly\nfavoured destinations for this activity. In Korea, the same viewing activity is called danpung-nori and the Seoraksan and Naejang-san mountains are among the best-known\ndestinations.\n\nUses: Maple wood is commonly used in high-end furniture, flooring, cabinetry, and kitchen accessories. Because of its durability and strength, maple can be found used as\nflooring in bowling alleys and for bowling pins.\n\nEffect: The maple trees  in Québec capture the carbon produced by the equivalent of 290,000 cars in a year. That’s 9% of all cars in Québec.")
obj8 = plant("Mango",8,"\033[1;32;40mDetails - \n\nA mango is an edible stone fruit produced by the tropical tree Mangifera indica which is believed to have originated from the region between northwestern Myanmar, Bangladesh,and northeastern India. M. indica has been cultivated in South and Southeast Asia since ancient times resulting in two distinct types of modern mango cultivars: the Indian\ntype and the Southeast Asian type. Other species in the genus Mangifera also produce edible fruits that are also called mangoes, the majority of which are found in the\nMalesian ecoregion.\n\nAmount of Plantation: Worldwide, there are several hundred cultivars of mango. Depending on the cultivar, mango fruit varies in size, shape, sweetness, skin color, and flesh color which may be pale yellow, gold, green, or orange. The mango is the national fruit of India, Pakistan and the Philippines, while the mango tree is the national tree of\nBangladesh.\n\nUses: Mangos have been an important crop in India for millennia. Today, these colorful, sweet fruits are a mainstay of Indian cuisine and are popular throughout the world.\nThe vitamins, minerals, and antioxidants in mangos can provide important health benefits. For example, vitamin K helps your blood clot effectively and helps prevent anemia.\nIt also plays an important role in helping strengthen your bones.Mangos are also rich in vitamin C, which is important for forming blood vessels and healthy collagen,as well as helping you heal.\n\nEffects: The use of agrochemicals (including fertilizers) and transport of mangos together account for approximately 60% of the industry's greenhouse gas emissions. produced for each kg of mango fruit produced. The majority of these emissions (57%) come from the production and use of agrochemicals, notably fertilizers.")
obj9 = plant("Mint",9,"\033[1;32;40mDetails - \n\nMentha (also known as mint, from Greek μίνθα míntha, Linear B mi-ta) is a genus of plants in the family Lamiaceae (mint family).[4] The exact distinction between species is\nunclear; it is estimated that 13 to 24 species exist. Hybridization occurs naturally where some species' ranges overlap. Many hybrids and cultivars are known.\n\nAmount of Plantation - The most common and popular mints for commercial cultivation are peppermint (Mentha × piperita), native spearmint (Mentha spicata), Scotch spearmint\n(Mentha x gracilis), and cornmint (Mentha arvensis); also (more recently) apple mint (Mentha suaveolens). Mints are supposed to make good companion plants, repelling pesty insects and attracting beneficial ones. They are susceptible to whitefly and aphids.Uses - The leaf, fresh or dried, is the culinary source of mint. Fresh mint is usually\npreferred over dried mint when storage of the mint is not a problem. The leaves have a warm, fresh, aromatic, sweet flavor with a cool aftertaste, and are used in teas,\nbeverages, jellies, syrups, candies, and ice creams. Menthol from mint essential oil (40–90%) is an ingredient of many cosmetics and some perfumes. Menthol and mint essentialoil are also used in aromatherapy which may have clinical use to alleviate post-surgery nausea.\n\nEffects on Environment - Mentha pliocenica fossil seeds have been excavated in Pliocene deposits of Dvorets on the right bank of the Dnieper river between the cities of\nRechitsa and Loyew, in south-eastern Belarus. The fossil seeds are similar to the seeds of Mentha aquatica and Mentha arvensis.")
ls=[]
new=9
i=1  
# ls=[["Neem","Rubber_tree","Tulsi"],["MoneyPlant","Aloe_Vera","Peepal"],["Maple","Mango","Mint"]]
mydata = [["\033[1;32;40m1", "\033[1;32;40mNeem"],  ["\033[1;32;40m2", "\033[1;32;40mRubber Tree"], ["\033[1;32;40m3", "\033[1;32;40mTulsi"],  ["\033[1;32;40m4", "\033[1;32;40mMoney Plant"],["\033[1;32;40m5", "\033[1;32;40mAloe Vera"], ["\033[1;32;40m6", "\033[1;32;40mPeepal"],   ["\033[1;32;40m7", "\033[1;32;40mMaple"], ["\033[1;32;40m8", "\033[1;32;40mMango"],["\033[1;32;40m9", "\033[1;32;40mMint"]]
num=1
while  i>0: 
 print('\033[1;32;40m─' * 90)
 head = ["\033[1;32;40mSr. No.", "\033[1;32;40mName"]
  
  # display table
 print("")
 print((('\033[1;32;40m<')+(('\033[1;32;40m─')*3)+'Plants Display Card'+(('\033[1;32;40m─')*3)+('\033[1;32;40m>')+'\n'))
 print(tabulate(mydata, headers=head, tablefmt='fancy_grid', numalign='center'))
 if 9<new:
     print("\033[1;32;40mNewly added data:\t")
     print(" ")
     for obj in ls:
         print(" ",obj.num," ",obj.name," ",obj.detail)
      
#  for i in range(3):
#     for j in range(3):
#        print("   ",ls[i][j],end=" ")  
#        num=num+1
#     print("\n")

 print("")
 print('\033[1;32;40m─' * 90)
 print("")
 print(('\033[1;32;40m<')+(('\033[1;32;40m─')*3)+'Choices'+(('\033[1;32;40m─')*3)+('\033[1;32;40m>')+'\n\n1. About\n\n2. Plantation Graphs\n\n3. Add Information\n\n4. Add a Plant\n\n5. Exit\n')
 print('\033[1;32;40m─' * 90)
 print("")
 user=int(input(('\033[1;31;40m<')+(('\033[1;31;40m─')*3)+'Enter your Choice'+(('\033[1;31;40m─')*3)+('\033[1;31;40m>')+'\t'))
 print("")
 print('\033[1;32;40m─' * 90) 
 
 if 5==user:
     break
 elif 1==user:
    plant_num=int(input("\n\033[1;32;40mWhich Plant:\t"))
    if 1==plant_num:
        sleep(2)
        screen_clear()
        obj1.display(obj1)
        sleep(20)
        screen_clear()
    elif 2==plant_num:
        sleep(2)
        screen_clear()
        obj2.display(obj2)
        sleep(20)
        screen_clear()
    elif 3==plant_num:
        sleep(2)
        screen_clear()
        print("\n")
        obj3.display(obj3)
        sleep(20)
        screen_clear()
    elif 4==plant_num:
        sleep(2)
        screen_clear()
        obj4.display(obj4)
        sleep(20)
        screen_clear()
    elif 5==plant_num:
        sleep(2)
        screen_clear()
        obj5.display(obj5)
        sleep(20)
        screen_clear()
    elif 6==plant_num:
        sleep(2)
        screen_clear()
        obj6.display(obj6)
        sleep(20)
        screen_clear()
    elif 7==plant_num:
        sleep(2)
        screen_clear()
        obj7.display(obj7)
        sleep(20)
        screen_clear()
    elif 8==plant_num:
        sleep(2)
        screen_clear()
        obj8.display(obj8)
        sleep(20)
        screen_clear()
    elif 9==plant_num:
        sleep(2)
        screen_clear()
        obj9.display(obj9)
        sleep(20)
        screen_clear()
 elif 2==user:
    graph_num=int(input("\n\033[1;32;40mWhich Plant:\t"))
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
 elif 3==user:
     plant_num=int(input("\033[1;32;40mWhich Plant:\t"))
     if 1==plant_num:
        sleep(2)
        screen_clear()
        s=input("\033[1;32;40mAdd Line:\t")
        obj1.change(plant_num,s)
        sleep(2)
        screen_clear()
     if 2==plant_num:
        sleep(2)
        screen_clear()
        s=input("\033[1;32;40mAdd Line:\t")
        obj2.change(plant_num,s)
        sleep(2)
        screen_clear()
     if 3==plant_num:
        sleep(2)
        screen_clear()
        s=input("\033[1;32;40mAdd Line:\t")
        obj3.change(plant_num,s)
        sleep(2)
        screen_clear()
     if 4==plant_num:
        sleep(2)
        screen_clear()
        s=input("\033[1;32;40mAdd Line:\t")
        obj4.change(plant_num,s)
        sleep(2)
        screen_clear()
     if 5==plant_num:
        sleep(2)
        screen_clear()
        s=input("\033[1;32;40mAdd Line:\t")
        obj5.change(plant_num,s)
        sleep(2)
        screen_clear()
     if 6==plant_num:
        sleep(2)
        screen_clear()
        s=input("\033[1;32;40mAdd Line:\t")
        obj6.change(plant_num,s)
        sleep(2)
        screen_clear()
     if 7==plant_num:
        sleep(2)
        screen_clear()
        s=input("\033[1;32;40mAdd Line:\t")
        obj7.change(plant_num,s)
        sleep(2)
        screen_clear()
     if 8==plant_num:
        sleep(2)
        screen_clear()
        s=input("\033[1;32;40mAdd Line:\t")
        obj8.change(plant_num,s)
        sleep(2)
        screen_clear()
     if 9==plant_num:
        sleep(2)
        screen_clear()
        s=input("\033[1;32;40mAdd Line:\t")
        obj9.change(plant_num,s)
        sleep(2)
        screen_clear()
         
 elif 4==user:
    plant_nam=input("\033[1;32;40mName of the Plant:\t")
    plant_detail=input("\033[1;32;40mAbout Plant:\t")
    new+=1
    new_obj=plant(plant_nam,new,plant_detail)
    ls.append(new_obj)
    sleep(2)
    screen_clear()
         
           
