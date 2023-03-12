from datetime import datetime

f = open("/content/emp.txt","r")
read = f.readlines()
f.close()
print(len(read))

# Append data to List
emp_lst = []
for i in range(len(read)):
  emp_lst.append(read[i])
  emp_lst[i] = emp_lst[i].split()

emp_lst

set_emp = set()
for row in emp_lst:
    emp_id = row[0]
    set_emp.add(emp_id)

print(set_emp)

for emp_id in set_emp:
  break_time = datetime.strptime("00:00:00", '%H:%M:%S')
  for i in range(len(emp_lst)):
    if emp_lst[i][0] == emp_id and emp_lst[i][3] == 'break-start':
      for j in range(i+1,len(emp_lst)):
        if emp_lst[j][0] == emp_id and emp_lst[j][3] == 'break-stop':
          datetime_str = str(emp_lst[i][2])
          dt = datetime.strptime(datetime_str,'%H:%M:%S')
        
          datetime_str1 = str(emp_lst[j][2])
          dt1 = datetime.strptime(datetime_str1,'%H:%M:%S')
            
          break_time = dt1 - dt
          break
    
    if emp_lst[i][0] == emp_id and emp_lst[i][3] == 'clock-in':
      for j in range(i+1,len(emp_lst)):
        if emp_lst[j][0] == emp_id and emp_lst[j][3] == 'clock-out':
          datetime_str = str(emp_lst[i][2])
          wt = datetime.strptime(datetime_str,'%H:%M:%S')
        
          datetime_str1 = str(emp_lst[j][2])
          wt1 = datetime.strptime(datetime_str1,'%H:%M:%S')
            
          working_hour = wt1 - wt
          break

  print("Working Time")
  print("{}".format(emp_id),working_hour)
