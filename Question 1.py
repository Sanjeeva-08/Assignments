a=int(input("Enter a*a grid : "))
grid=[]
for i in range(a):
    grid.append(["#"]*a)
#print(grid)
Q_position=[-1]*a
rows=0
columns=0
count_of_grids=0
possible_outcomes=[]
while rows>=0:
    while columns<a:
        safe_place=True
        for i in range(rows):
            if Q_position[i]==columns or abs(Q_position[i]-columns)==abs(i-rows):
                safe_place=False
                break
        if safe_place:
            break
        columns+=1
    if columns<a:
        Q_position[rows]=columns
        grid[rows][columns]="Q"
        if rows==a-1:
            answer=[]
            for i in grid:
                answer.append("".join(i))
            possible_outcomes.append(answer)
            count_of_grids+=1
            grid[rows][columns]="#"
            columns+=1
        else:
            rows+=1
            columns=0
    else:
        rows-=1
        if rows>=0:
            columns=Q_position[rows]
            grid[rows][columns]="#"
            columns+=1
print(possible_outcomes,",",count_of_grids)