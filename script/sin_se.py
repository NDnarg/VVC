import os

cmd='./EncoderApp -c /home/niuwh/Desktop/VVCSoftware_VTM-VTM-10.0/cfg/encoder_intra_vtm.cfg -c /home/niuwh/Desktop/VVCSoftware_VTM-VTM-10.0/cfg/per-sequence/RaceHorses.cfg'

os.system(cmd+' -q 22 | tee -a /home/niuwh/Desktop/sequence/RaceHorses.txt &')
os.system(cmd+' -q 27 | tee -a /home/niuwh/Desktop/sequence/RaceHorses.txt &')
os.system(cmd+' -q 32 | tee -a /home/niuwh/Desktop/sequence/RaceHorses.txt &')
os.system(cmd+' -q 37 | tee -a /home/niuwh/Desktop/sequence/RaceHorses.txt &')
