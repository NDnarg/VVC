import os
SEQUENCE=['Tango2','FoodMarket4','Campfire','CatRobot','DaylightRoad2','ParkRunning3','MarketPlace','RitualDance','Cactus','BasketballDrive','BQTerrace','BasketballDrill','BQMall','PartyScene','RaceHorsesC','BasketballPass','BQSquare','BlowingBubbles','RaceHorses','FourPeople','Johnny','KristenAndSara','BasketballDrillText','ArenaOfValor','SlideEditing','SlideShow']
QP=[22,27,32,37]
for sequence in SEQUENCE:
    for qp in QP:
        cmd='./EncoderApp -c /home/niuwh/Desktop/VVCSoftware_VTM-VTM-10.0/cfg/encoder_intra_vtm.cfg -c /home/niuwh/Desktop/VVCSoftware_VTM-VTM-10.0/cfg/per-sequence/'+str(sequence)+'.cfg'

        os.system(cmd+' -q '+str(qp)+' -f 1 | tee -a /home/niuwh/Desktop/ordinary_quant_ai_1f/'+str(sequence)+'/'+str(sequence)+'_qp'+str(qp)+'.txt &')
