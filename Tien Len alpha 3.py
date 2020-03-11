# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 19:31:18 2019

@author: Jalaa
"""
import random
#DECK=["0","3s","3c","3d","3h","4s","4c","4d","4h","5s","5c","5d","5h","6s","6c","6d","6h","7s","7c","7d","7h","8s","8c","8d","8h","9s","9c","9d","9h","ts","tc","td","th","js","jc","jd","jh","qs","qc","qd","qh","ks","kc","kd","kh","as","ac","ad","ah","2s","2c","2d","2h"]

def main(aa,bb,cc,dd):
    cards =["0","3s","3c","3d","3h","4s","4c","4d","4h","5s","5c","5d","5h","6s","6c","6d","6h","7s","7c","7d","7h","8s","8c","8d","8h","9s","9c","9d","9h","ts","tc","td","th","js","jc","jd","jh","qs","qc","qd","qh","ks","kc","kd","kh","as","ac","ad","ah","2s","2c","2d","2h"]
    CARDS =["0","3s","3c","3d","3h","4s","4c","4d","4h","5s","5c","5d","5h","6s","6c","6d","6h","7s","7c","7d","7h","8s","8c","8d","8h","9s","9c","9d","9h","ts","tc","td","th","js","jc","jd","jh","qs","qc","qd","qh","ks","kc","kd","kh","as","ac","ad","ah","2s","2c","2d","2h"]
    rank=["3","4","5","6","7","8","9","t","j","q","k","a","0","2"]
    
    #times = input("times: ")
    times=input("shuffle ___ times:")
    qq = " "
    try:
        times = int(times)
    except ValueError:
        times = 1000
        qq = input("quit? y/n: ")
        if len(qq) > 0:
            if qq[0] == "y":
                print("cac")
                sys.exit()
        #if len(qq) > 4:            
         #   if qq[2] == "C":
          #          cards=asCii(cards)
           #         CARDS=asCii(CARDS)
                    
 
    
    shuffle(cards,times)
    #print(cards)
    o=[]
    t=[]
    h=[]
    f=[]
    deal(cards,o,t,h,f)
    o=sort(o,CARDS)
    t=sort(t,CARDS)
    h=sort(h,CARDS)    
    f=sort(f,CARDS)
    print(cards, "\n")
    print(o)
    print(t)

    #OLD CODE BELOW#
    
    rule=["open"]
    last=["0"]
    print(cards)
    print("\n\n\n\n")
    oi=aa
    ti=bb
    hi=cc
    fi=dd 
    rotate(o,rank,rule,last,CARDS,t,h,f,oi,ti,hi,fi)



def asCii(p):
    j=0
    while j < len(p):
        duck=[]
        i = p[j]
        duck.append(i[0])
        duck.append(i[1])
        if duck[1] == "s":
           duck[1] = "\u2660" 
        if duck[1] == "c":
           duck[1] = "\u2663"
        if duck[1] == "d":
           duck[1] = "\u2662"
        if duck[1] == "h":
           duck[1] = "\u2661"           
        s = ""
        s = s.join(duck)
        p[j] = s
        j+=1
    return(p)
    
    
    '''
    khoai=1
    while khoai < 53:
        duck=[]
        card = cards[khoai]
        duck.append(card[0])
        duck.append(card[1])
        if khoai%4==1:
           duck[1] = "\u2660" 
        if khoai%4==2:
           duck[1] = "\u2663" 
        if khoai%4==3:
           duck[1] = "\u2662" 
        if khoai%4==0:
           duck[1] = "\u2661"            
        s = ""
        s = s.join(duck)
        cards[khoai]=s
        khoai+=1
    print(cards)
    return(cards)
    '''

def sort(p,CARDS):
    #srtd=0
    #while srtd == 0:        
        a=0
        while a < 12:
            b=0
            pa=p[a+1]
            
            while b < a+1:
                pb=p[b]
                #print(pa)
                #print(pb)
                if CARDS.index(pb) > CARDS.index(pa):
                    p[a+1] = pb
                    p[b] = pa
                    pa=p[a+1]
                    pb=p[b]                    
                #print(p)
                #cac=input("cac")
                b+=1
            a+=1
        return(p)     
        
      
    


def deal(cards,o,t,h,f):
    a=1
    while a<52:
        b=cards[a]
        o.append(b)
        a+=1        
        b=cards[a]
        t.append(b)
        a+=1
        b=cards[a]
        h.append(b)
        a+=1
        b=cards[a]
        f.append(b)
        a+=1
    
def shuffle(c,t):
    times = 0    
    while times < t:       
        p=random.randint(0,1)
        if p == 0:
            p1=random.randint(2,51)
            s1=c[1:p1]
            b=0
            while b < len(s1): 
                temp = s1[b]
                c.remove(temp)
                c.append(temp)
                b+=1
                #if times == 0 or times == 5:
                                #print(s1[b-1])
            times+=1
        else:
            p1=random.randint(2,50)
            p2=random.randint(p1,51)
            s1=c[p1:p2]
            b=1
            while b < p2-p1: 
                temp = s1[b]
                c.remove(temp)
                c.append(temp)
                b+=1
                #if times == 0:
                 #               print(s1[b-1])
            times+=1       
    
     







# OLD CODE BELOW#
        
        
        
        
        
        
        

def check(a,x,y,z):
    if a==0:
        return(0)
    if a==1 and x+y+z==0:
        return(1)
    else:
        return(2)
    


def asCii(p):
    j=0
    while j < len(p):
        duck=[]
        i = p[j]
        duck.append(i[0])
        duck.append(i[1])
        if duck[1] == "s":
           duck[1] = "\u2660" 
        if duck[1] == "c":
           duck[1] = "\u2663"
        if duck[1] == "d":
           duck[1] = "\u2662"
        if duck[1] == "h":
           duck[1] = "\u2661"           
        s = ""
        s = s.join(duck)
        p[j] = s
        j+=1
    return(p)


def rotate(o,rank,rule,last,card,t,h,f,oi,ti,hi,fi):
    a=0   
    while a==0:
        ch=check(oi,ti,hi,fi)
        if ch==2:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("rule ",rule)
            print("last ",last)
            print("player 1")
            oint=[]           
            i = 0
            while i < len(o):
                oint.append(o[i])
                i+=1
            oint = asCii(oint)
            print(oint)
            oi=play(o,rank,rule,last,card,oi)

        if ch==1:
            rule[0]="open"
            last[0]="0"
            oi=1
            ti=1
            hi=1
            fi=1
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("rule ",rule)
            print("last ",last)
            print("player 1")
            oint=[]           
            i = 0
            while i < len(o):
                oint.append(o[i])
                i+=1
            oint = asCii(oint)
            print(oint)            
            oi=play(o,rank,rule,last,card,oi)
        if len(o)==0:
            print("Player 1 wins!")
            main(1,0,0,0)
            a+=1
            
        ch=check(ti,oi,hi,fi)
        if ch==2:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("rule ",rule)
            print("last ",last)
            print("player 2")
            oint=[]           
            i = 0
            while i < len(t):
                oint.append(t[i])
                i+=1
            oint = asCii(oint)
            print(oint) 
            ti=play(t,rank,rule,last,card,ti)
        if ch==1:
            rule[0]="open"
            last[0]="0" 
            oi=1
            ti=1
            hi=1
            fi=1
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("rule ",rule)
            print("last ",last)
            print("player 2")
            oint=[]           
            i = 0
            while i < len(t):
                oint.append(t[i])
                i+=1
            oint = asCii(oint)
            print(oint)             
            ti=play(t,rank,rule,last,card,ti)
        if len(t)==0:
            print("Player 2 wins!")
            main(0,1,0,0)
            a+=1
            
        ch=check(hi,oi,ti,fi)
        if ch==2:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("rule ",rule)
            print("last ",last)
            print("player 3")
            oint=[]           
            i = 0
            while i < len(h):
                oint.append(h[i])
                i+=1
            oint = asCii(oint)
            print(oint)
            hi=play(h,rank,rule,last,card,hi)
        if ch==1:
            rule[0]="open"
            last[0]="0" 
            oi=1
            ti=1
            hi=1
            fi=1
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("rule ",rule)
            print("last ",last)
            print("player 3")
            oint=[]           
            i = 0
            while i < len(h):
                oint.append(h[i])
                i+=1
            oint = asCii(oint)
            print(oint)            
            hi=play(h,rank,rule,last,card,hi)
        if len(h)==0:
            print("Player 3 wins!")
            main(0,0,1,0)
            a+=1
            
        ch=check(fi,oi,hi,ti)
        if ch==2:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("rule ",rule)
            print("last ",last)
            print("player 4")
            oint=[]           
            i = 0
            while i < len(f):
                oint.append(f[i])
                i+=1
            oint = asCii(oint)
            print(oint)
            fi=play(f,rank,rule,last,card,fi)
        if ch==1:
            rule[0]="open"
            last[0]="0" 
            oi=1
            ti=1
            hi=1
            fi=1
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("rule ",rule)
            print("last ",last)
            print("player 4")
            print(f)            
            fi=play(f,rank,rule,last,card,fi)
        if len(f)==0:
            print("Player 4 wins!")
            main(0,0,0,1)
            a+=1
    
    
def play(o,r,u,l,card,oi):
    d=0
    while d==0:
        a=input("play:")
        if a[0]=="p":
            #print("passed")
            return(0)
            d+=1
        else:    
            b=a.split(",")
            c=0
            for i in b:
                for j in o:
                    if i==j:
                        c+=1    
            if c!=len(b):
                print("you do not have those cards\nto play 8\u2660 9\u2663 10\u2662 j\u2661, type: 8s,9c,td,jh\n")
            else:
                if len(b)==1 and (u[0]=="sing" or u[0]=="open" or u[0]=="two") and card.index(b[0])>card.index(l[0]):                  
                    l[0]=b[-1]    
                    for i in b:
                        o.remove(i)
                    if card.index(b[-1])>48:
                        u[0]="two"
                    else:
                        u[0]="sing"
                    #print(len(b))
                    #print("played 1")
                    return(1)
                    d+=1                   
                if len(b)==2 and card.index(b[-1])>card.index(l[0]) and (u[0]=="open" or u[0]=="dubs" or u[0]=="dubtwo"):
                    z=b[0]
                    x=b[1]
                    if z[0]==x[0]:
                        l[0]=b[-1]    
                        for i in b:
                            o.remove(i)
                        if card.index(b[-1])>48:
                            u[0]="dubtwo"
                        else:
                            u[0]="dubs"
                        #print("played")
                        return(1)
                        d+=1
                    else:
                        print("this is not a valid set of cards 1")
                if len(b)==3:
                    z=b[0]
                    y=b[1]
                    x=b[2]
                    if z[0]==x[0] and z[0]==y[0] and (u[0]=="open" or u[0]=="trips") and card.index(b[-1])>card.index(l[0]):
                        l[0]=b[-1]    
                        for i in b:
                            o.remove(i)
                        u[0]="trips"
                        #print("played")
                        return(1)
                        d+=1
                    if r.index(z[0])==r.index(y[0])-1 and r.index(x[0])==r.index(y[0])+1 and (u[0]=="open" or u[0]=="run3") and card.index(b[-1])>card.index(l[0]):
                        l[0]=b[-1]    
                        for i in b:
                            o.remove(i)
                        u[0]="run3"
                        print("played")
                        return(1)
                        d+=1
                    else:
                        print("this is not a valid set of cards 2")   
                if len(b)==4:
                    z=b[0]
                    y=b[1]
                    x=b[2]
                    w=b[3]
                    if z[0]==x[0] and z[0]==y[0] and z[0]==w[0] and (u[0]=="open" or u[0]=="quad" or u[0]=="two" or u[0]=="dubtwo") and card.index(b[-1])>card.index(l[0]):
                        l[0]=b[-1]
                        for i in b:
                            o.remove(i)
                        u[0]="quad"
                        #print(len(b))
                        #print("played 4")
                        return(1)
                        d+=1
                    if r.index(z[0])==r.index(y[0])-1 and r.index(x[0])==r.index(y[0])+1 and r.index(x[0])==r.index(w[0])-1 and (u[0]=="open" or u[0]=="run4") and card.index(b[-1])>card.index(l[0]):
                        l[0]=b[-1]
                        for i in b:
                            o.remove(i)
                        u[0]="run4"
                        #print(len(b))
                        #print("played 4")                        
                        return(1)
                        d+=1
                    else:
                        print("this is not a valid set of cards 3")
                if len(b)>4:
                    i=0
                    j=0
                    run="run{}"
                    while i<len(b)-1:
                        g=b[i]
                        h=b[i+1]
                        if r.index(g[0])==r.index(h[0])-1:
                            j+=1
                        i+=1
                    if i==j and (u[0]==run.format(len(b)) or u[0]=="open") and card.index(b[-1])>card.index(l[0]):
                        l[0]=b[-1]
                        for x in b:
                            o.remove(x)                    
                        u[0]=run.format(len(b))
                        print(run.format(len(b)))
                        #print("played 5")
                        return(1)
                        d+=1                        
                if len(b)==6 and (u[0]=="two" or (u[0]=="6killer" and card.index(b[-1])>card.index(l[0]))):
                    t1=b[0]
                    t2=b[1]
                    t3=b[2]
                    t4=b[3]
                    t5=b[4]
                    t6=b[5]
                    if r.index(t1[0])==r.index(t2[0]) and r.index(t2[0])==r.index(t3[0])-1 and r.index(t4[0])==r.index(t3[0]) and r.index(t4[0])==r.index(t5[0])-1 and r.index(t6[0])==r.index(t5[0]):
                        if u[0]=="two" or (u[0]=="6killer" and card.index(b[-1])>card.index(l[0])):
                            l[0]=b[-1]
                            for x in b:
                                o.remove(x)
                            u[0]="6killer"
                            return(1)
                            d+=1
                            
                else:
                    print("this is not a valid set of cards")                        
            
            


aaa=random.randint(1,4)
if aaa==1:
    ww=1
    xx=0
    yy=0
    zz=0
if aaa==2:
    ww=0
    xx=1
    yy=0
    zz=0
if aaa==3:
    ww=0
    xx=0
    yy=1
    zz=0
if aaa==4:
    ww=0
    xx=0
    yy=0
    zz=1
        
main(ww,xx,yy,zz)
    
    
   