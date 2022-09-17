def arithmetic_arranger(problems,solve=False):
  if len(problems)>5:
    return "Error: Too many problems." 
  row1=[]
  row2_1=[]
  row2_2=[]
  length=[]
  solution=[]
  f=""
  g=""
  h=""
  for i in problems:
    a,b,c=map(str,i.split(" "))
    if b!="+" and b!="-":
        return "Error: Operator must be '+' or '-'."
    if not a.isdigit() or not c.isdigit():
        return "Error: Numbers must only contain digits."    
    d=len(a)
    e=len(c)
    if d>4 or e>4:
        return "Error: Numbers cannot be more than four digits."
    if d>=e:
        length.append(d+2)
    else:
        length.append(e+2)
    solution.append(eval(i))
    row1.append(a)
    row2_1.append(b)
    row2_2.append(c)
  length_of_list=len(row1)
  if solve is False:  
    for i in range(length_of_list):
        if i==length_of_list-1:
            f+=row1[i].rjust(length[i])+"\n"
            g+=row2_1[i].ljust(2)+row2_2[i].rjust(length[i]-2)+"\n"
            h+="-"*length[i]
        else:        
            f+=row1[i].rjust(length[i])+" "*4
            g+=row2_1[i].ljust(2)+row2_2[i].rjust(length[i]-2)+" "*4
            h+="-"*length[i]+" "*4
  else:
     j=""
     for i in range(length_of_list):
        if i!=length_of_list-1:  
            f+=row1[i].rjust(length[i]," ")+" "*4
            g+=row2_1[i].ljust(2," ")+row2_2[i].rjust(length[i]-2," ")+" "*4
            h+="-"*length[i]+" "*4
            j+=str(solution[i]).rjust(length[i]," ")+" "*4
        else:
            f+=row1[i].rjust(length[i]," ")+"\n"
            g+=row2_1[i].ljust(2," ")+row2_2[i].rjust(length[i]-2," ")+"\n"
            h+="-"*length[i]+"\n"
            j+=str(solution[i]).rjust(length[i]," ")    
  if solve is False:
    k=f+g+h
    return k
  else:
    k=f+g+h+j
    return k

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True))
