def BAT1BOWL2():
    print("SUMMARY")
    print("INNINGS  BATTING  BOWLING  SCORE")
    Q5="SELECT INNINGS,BATTING,BOWLING,SCORE FROM BAT1";
    cur.execute(Q5)
    data=cur.fetchone()
    print(data)
    print("TARGET  INNINGS  BATTING  BOWLING  SCORE")
    Q6="SELECT TARGET,INNINGS,BATTING,BOWLING,SCORE FROM BOWL2";
    cur.execute(Q6)
    data2=cur.fetchone()
    print(data2)

def BOWL1BAT2():
    print("SUMMARY")
    print("INNINGS  BATTING  BOWLING  SCORE")
    Q7="SELECT INNINGS,BATTING,BOWLING,SCORE FROM BOWL1";
    cur.execute(Q7)
    data3=cur.fetchone()
    print(data3)
    print("TARGET  INNINGS  BATTING  BOWLING  SCORE")
    Q8="SELECT TARGET,INNINGS,BATTING,BOWLING,SCORE FROM BAT2"
    cur.execute(Q8)
    data4=cur.fetchone()
    print(data4)

def BAT1(S1):
    QUERY="UPDATE BAT1 SET SCORE={}".format(S1)
    cur.execute(QUERY)
    con.commit()

def BAT2(S2,T):
    QUERY="UPDATE BAT2 SET TARGET={},SCORE={}".format(T,S2)
    cur.execute(QUERY)
    con.commit()

def BOWL1(S1):
    QUERY="UPDATE BOWL1 SET SCORE={}".format(S1)
    cur.execute(QUERY)
    con.commit()

def BOWL2(S2,T):
    QUERY="UPDATE BOWL2 SET TARGET={},SCORE={}".format(T,S2)
    cur.execute(QUERY)
    con.commit()

def Score():
    Q10="SELECT TARGET FROM BOWL2";
    cur.execute(Q10)
    data5=cur.fetchone()
    if int(data5[0])==0:
        BOWL1BAT2()
    else:
        BAT1BOWL2()
        
#MAIN PROGRAM
import random
import math
import mysql.connector as MS
con=MS.connect(host="localhost",user="root",password="kaliff",database="handcricket")
if con.is_connected()==True:
    cur=con.cursor()
    while True:
        print("\n        HANDCRICKET   IN         ")
        print("     COMPUTER   __PRODUCT OF SK       ")
        print("\nLoading......")
        print("welcome Back..")
        print("Select")
        print("PRESS-1 TO PLAY MATCH:")
        print("PRESS-2 TO SEE THE LAST MATCH SCORE:")
        print("PRESS-3 TO EXIT::")
        OPT2=int(input("Enter your choice:"))
        if OPT2==2:
            print("LAST MATCH SCORE==:")
            Score()
        elif OPT2==3:
            print("THANK YOU FOR PLAYING \n REMEBER TO PLAY AGAIN :) ")
            break
        elif OPT2==1:
            Q1="UPDATE BAT1 SET SCORE=0";
            Q2="UPDATE BAT2 SET TARGET=0,SCORE=0";
            Q3="UPDATE BOWL1 SET SCORE=0";
            Q4="UPDATE BOWL2 SET TARGET=0,SCORE=0";

            cur.execute(Q1)
            con.commit()
            cur.execute(Q2)
            con.commit()
            cur.execute(Q3)
            con.commit()
            cur.execute(Q4)
            con.commit()
            TOSS=input("ODD OR EVEN")
            COMPUTER = random.randint(0,6)
            ME = int(input ("enter the toss"))
            print("your toss:",ME)
            print("computer toss:",COMPUTER)

            if TOSS=='EVEN':
                if(COMPUTER+ME)%2==0:
                    print("you won the toss")
                    LIVE=input("BATTING OR BOWLING")
                else:
                    CHOICE=random.random()
                    if(CHOICE<0.5):
                        print("COMPUTER WON THE TOSS AND CHOSE TO BAT")
                        LIVE="BOWLING"
                    else:
                        print("COMPUTER WON THE TOSS AND CHOICE TO BOWL")   
                        LIVE="BATTING"
            
            if TOSS == "ODD":
                if(ME+COMPUTER) % 2 ==1:
                    LIVE= input ("BATTING OR BOWLING")
                else:
                    choice = random.random()
                    if(choice < 0.5):
                        print("COMPUTER WON THE TOSS AND CHOICE TO BAT")
                        LIVE = "BOWLING"
                    else:
                        print("COMPUTER WON THE TOSS AND CHOICE TO BOWL")
                        LIVE = "BATTING"
            
            SCORE=0
            TARGET=1
            INNINGS=1
            S1=0
            S2=0
            T=S1+1
            while True:
                print("YOU:",LIVE,"INNINGS:",INNINGS)
                ME=int(input("Enter a number : "))
                COMPUTER =random.randint(0,6)
                print("YOU:",ME)  
                print("COMPUTER",COMPUTER)
	
                if(ME==COMPUTER):
                    if(LIVE=="BATTING" and INNINGS==1):
                        LIVE="BOWLING"
                        INNINGS=2
                        print("OUT...")
                        print(" TO DEFEND :",SCORE+1)
                    elif(LIVE=="BOWLING" and INNINGS== 1):
                        LIVE="BATTING"
                        INNINGS=2
                        print("OUT...")	
                        print ("TARGET IS :", TARGET)
                    elif(LIVE=="BATTING" and INNINGS ==2):
                        BOWL1BAT2()
                        print("OUTT... COMPUTER WON THE MATCH	")
                        break
                    elif(LIVE=="BOWLING" and INNINGS ==2):
                        BAT1BOWL2()
                        print("OUTT.. YOU WON THE MATCH")
                        break	
                else:
                    if(LIVE=="BATTING" and INNINGS==1):
                        if ME==0:
                          SCORE=SCORE+COMPUTER
                          S1=S1+COMPUTER
                          BAT1(S1)
                        else:
                          SCORE=SCORE+ME
                          S1=S1+ME
                          BAT1(S1)
                        print("SCORE:",SCORE)
                    elif(LIVE =="BATTING" and INNINGS== 2):
                        if(TARGET-ME>0):
                            if ME==0:
                                TARGET=TARGET- COMPUTER
                                S2=S2+COMPUTER
                                T=S1+1
                                BAT2(S2,T)
                            else:    
                                TARGET=TARGET-ME
                                S2=S2+ME
                                T=S1+1
                                BAT2(S2,T)
                            print("TARGET:",TARGET)
                        else:
                            if ME==0:
                                S2=S2+COMPUTER
                            else:
                                S2=S2+ME
                            BAT2(S2,T)
                            BOWL1BAT2()
                            print("YOU WON THE MATCH")
                            break
                    elif(LIVE=="BOWLING" and INNINGS==1):
                        if COMPUTER==0:
                            TARGET=TARGET+ME
                            S1=S1+ME
                            BOWL1(S1)
                        else:
                            TARGET = TARGET +COMPUTER
                            S1=S1+COMPUTER
                            BOWL1(S1)
                        print("SCORE:",TARGET )
                    elif(LIVE =="BOWLING" and INNINGS==2):
                        if(SCORE-COMPUTER>0):
                           if COMPUTER==0:
                             SCORE=SCORE-ME
                             S2=S2+ME
                             T=S1+1
                             BOWL2(S2,T)
                           else:    
                             SCORE=SCORE-COMPUTER
                             S2=S2+COMPUTER
                             T=S1+1
                             BOWL2(S2,T)
                           print("TO DEFEND:",SCORE)
                        else:
                            if COMPUTER==0:
                                S2=S2+ME
                            else:
                                S2=S2+COMPUTER
                            BOWL2(S2,T)
                            BAT1BOWL2()
                            print("YOU LOST THE MATCH COMPUTER WON ")									   
                            break
