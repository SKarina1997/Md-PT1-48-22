while True:
    # entering a parameter
   length_str = input('Please, enter the maximum number of characters in line from 35 to 50\n')
   if length_str.isdigit():
        if int(length_str) > 35 and int(length_str) < 50 :
            length_str = int(length_str)
            break
        else:
            print("The number is not correct")
   
with open('D:/Мое/Мое/Python/txt.txt','r') as f:
    line = f.readlines()
with open('D:/Мое/Мое/Python/txt-new.txt','w') as f:
    text = " "
    counter = 0
    for i in line:
        for j in i.split():
            new_count = counter+len(j)
            if counter !=0:
                new_count +=1
            if new_count >= length_str:
                text += "\n"
                counter = 0
            if counter !=0:
                text += ' '
                counter += 1
            text += j
            counter += len(j)
    txt_new = text.split('\n')
    for l in txt_new:
        checked = l.count(' ')
        if len(l) < length_str and checked !=0:
            final = (length_str-len(l))//checked
            surplus = (length_str-len(l))%checked
            if final > 0:
                l=l.replace(' ',(' ') + (' ') *final)
            if surplus > 0:
                l=l.replace((' ') + (' ') *final,(' ') + (' ')*final + (' '),surplus)
        l = l + '\n'
        f.writelines(l)
print('We have created a copy of text')