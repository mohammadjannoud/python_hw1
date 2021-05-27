L=['Network' , 'Math' , 'Programming', 'Physics' , 'Music']
longest='';
long=0;
for item in L:
    if(len(item)>long):
        longest=item
        long=len(item)
print('The longest word is: ',longest)
