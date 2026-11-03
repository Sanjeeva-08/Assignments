P=input()
Q=input()
validation=False
if Q[0]=="+":
    validation=True
else:
    validation=False
P_start=0
Matching=False
for i in range(1,len(Q)):
    if Q[i]==Q[i-1]=="+":
        validation=True
if validation==True:
    Matching=False
    
elif P==Q:
    Matching=True
    
for i in range(0,len(Q)-1):
    if Q[i+1]=="+":
        previous=Q[i]
        P_char_counter=0
        if i>0 and P_start==0:
            P_start=i
        if P[0]==Q[0]:
            for j in range(P_start,len(P)):
                if P[j]==previous:
                    P_char_counter+=1
                else:
                    break
            P_start=P_start+P_char_counter
            if P_char_counter==0:
                Matching=False
            else:
                Matching=True
            remaining=P[P_start:]
            remaining_Q=Q[i+2:]
            if remaining==remaining_Q:
                Matching=True
            else:
                Matching=False
        else:
            Matching=False
 
print(Matching)