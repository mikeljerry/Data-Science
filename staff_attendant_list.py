#collecting staff morning login list
filename='staff_attendant_list.txt'
print('enter Quit when time is 10am.')
attendant_list=[]
while True:
    staff_name=input('what is your name? ')
    attendant_list.append(staff_name)
    staff_dept=input("what's your department? ")
    attendant_list.append(staff_dept)
    login_time=input('login time: ')
    time=float(login_time)
    attendant_list.append(time)
    time=float(login_time)
    if time>10:
        print('you are late',staff_name)
        break
    else:
        continue   
with open(filename,'a') as f:
    for list in attendant_list:
        f.write(str(list)+'\t')
    print(staff_name,' come the next working day')
