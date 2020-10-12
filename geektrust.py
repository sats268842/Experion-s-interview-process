import sys
support_kingdom=0
supported_kingdom=[]
kingdom = ["SPACE","LAND","WATER","ICE","AIR","FIRE"]
msg_knd = []
msg_scrt = []

def readFile():

    input_file = sys.argv[1]
    file = open(input_file, 'r')
    Lines = file.readlines() 
    for line in Lines: 
       for word in line.split():
          if word in kingdom:
             msg_knd.append(word)

          else:
                
              if(len(line.split())<=2):
                    msg_scrt.append(word)  
                
              else:
                    i=1
                    length=len(line.split())
                    word1=""
                    for i in range(1,length):
                       word1= word1+line.split()[i]
                    msg_scrt.append(word1)
                    break

def checking():
    global support_kingdom
    global supported_kingdom

    count1=0
    air_flag= True;
    land_flag= True;
    fire_flag= True;
    water_flag= True;
    ice_flag= True;      
    
    readFile()
   

    count =len(msg_knd)
    for kingdom in msg_knd:

            if kingdom == "AIR":
                if any(c in ('R') for c in msg_scrt[count1]) and any(c in ('O') for c in msg_scrt[count1]) and any(c in ('Z') for c in msg_scrt[count1]) and air_flag:
                        support_kingdom+=1
                        supported_kingdom.append(kingdom)
                        air_flag= False

            if kingdom == "LAND":
                if any(c in 'F' for c in msg_scrt[count1]) and any(c in 'I' for c in msg_scrt[count1]) and any(c in 'S' for c in msg_scrt[count1]) and any(c in 'U' for c in msg_scrt[count1]) and land_flag and  (msg_scrt[count1].count('F')==2):
                        support_kingdom+=1
                        supported_kingdom.append(kingdom)
                        land_flag= False
            
            if kingdom == "ICE":
                if any(c in 'V' for c in msg_scrt[count1]) and any(c in 'T' for c in msg_scrt[count1]) and any(c in 'H' for c in msg_scrt[count1]) and any(c in 'O' for c in msg_scrt[count1]) and any(c in 'A' for c in msg_scrt[count1]) and (msg_scrt[count1].count('T')==3) and ice_flag:
                        support_kingdom+=1
                        supported_kingdom.append(kingdom)
                        ice_flag= False

            if kingdom == "FIRE":
                if any(c in 'J' for c in msg_scrt[count1]) and any(c in 'X' for c in msg_scrt[count1]) and any(c in 'G' for c in msg_scrt[count1]) and any(c in 'M' for c in msg_scrt[count1]) and any(c in 'U' for c in msg_scrt[count1])  and any(c in 'T' for c in msg_scrt[count1]) and fire_flag:
                    support_kingdom+=1
                    supported_kingdom.append(kingdom)
                    fire_flag= False
                    
            if kingdom == "WATER":
                 if any(c in 'J' for c in msg_scrt[count1]) and any(c in 'A' for c in msg_scrt[count1]) and any(c in 'V' for c in msg_scrt[count1]) and any(c in 'W' for c in msg_scrt[count1])  and any(c in 'B' for c in msg_scrt[count1]) and any(c in 'Z' for c in msg_scrt[count1]) and (msg_scrt[count1].count('V')==2) and water_flag:
                        support_kingdom+=1
                        supported_kingdom.append(kingdom)
                        water_flag= False
            count1+=1

def main():
   checking()
   if(support_kingdom>=3):
        supported_kingdom.insert(0,"SPACE")
        for i in supported_kingdom:
            print(i,end =" ")
   else:
        print("NONE")
    
   

if __name__ == "__main__":
    main()
    