import math as m
def add_time(start, duration, days = None):
  
    week_d = ["monday", "tuesday", "wednesday", 
    "thursday", "friday", "saturday", "sunday"]
    
    days_ = str(days).lower()
    
    start_p = start.split(" ")
      
    start_period = start_p[0].split(":")
    duration_period =  duration.split(":")
    day_c = lambda x : (x//12)
    helper_ = lambda x, y : ((x*60 + y)/60)
    days_counter = lambda x: (x/24) 
        
    hlp = helper_(int(start_period[0]), int(start_period[1])) + helper_(int(duration_period[0]), int(duration_period[1]))
      
    day_z = day_c(hlp)
      
    min_add = int(start_period[1])+  int(duration_period[1])
      
    hr_  = int(start_period[0]) +  int(duration_period[0])
    hr_add  = round((hr_ /12.)% 1 * 12.)
  
    ampm_ = start_p[1]
    if min_add >= 60:
        min_add = min_add - 60
        hr_add = hr_add + 1
  
    if day_z ==0 or (day_z)%2 ==0:
        ampm = start_p[1]
  
    elif (day_z)%2 !=0:
        if start_p[1] == "AM":
            ampm = "PM"
        else:
            ampm = "AM"
    
    days_count = round(days_counter(round(hlp)))
    if days:          
        if days_count == 0 and days:
            add_time = str(hr_add) +":"+str("{:02d}".format(int(min_add))) + " "+ampm+ ", "+ days_.capitalize()
            return add_time
            
        elif days_count >0 and days_count ==1:
            if ampm_ == "PM" and ampm =="AM": 
                add_time = str(hr_add) +":"+str("{:02d}".format(int(min_add))) + " "+ampm+ " (next day)"
                return add_time
            
            else:
                i = week_d.index(days_)
                j = i + days_count
                days_ = week_d[j]
                add_time = str(hr_add) +":"+str("{:02d}".format(int(min_add))) + " "+ampm+ ", "+ days_.capitalize()+ " (next day)"
                return add_time
        
        elif days_count >0 and days_count >1:
            i = week_d.index(days_)
            j = i + days_count
            if j<7:
                j = week_d[j]
            elif j >7:
                while j>6:
                    j -= 7
                j = week_d[j]
            add_time = str(hr_add) +":"+str("{:02d}".format(int(min_add))) + " "+ampm+ ", "+ j.capitalize()
            return add_time + " ("+str(days_count) + " days later)"
    
    else:
        if days_count == 0:
            add_time = str(hr_add) +":"+str("{:02d}".format(int(min_add))) + " "+ampm
            return add_time
        
        elif days_count >0 and days_count ==1:
            if ampm_ == "PM" and ampm =="AM": 
                add_time = str(hr_add) +":"+str("{:02d}".format(int(min_add))) + " "+ampm+ " (next day)"
                return add_time
            elif ampm_ == "AM" and ampm =="PM" and hlp <24:
                add_time = str(hr_add) +":"+str("{:02d}".format(min_add)) + " "+ampm
                return add_time
            else:
                add_time = str(hr_add) +":"+str("{:02d}".format(int(min_add))) + " "+ampm+ " (next day)"
                return add_time
        
        elif days_count >0 and days_count >1:
            add_time = str(hr_add) +":"+str("{:02d}".format(int(min_add))) + " "+ampm+" "
            return add_time + "("+str(days_count) +  " days later)"
    
"""    
print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12", "monDay"))
# Returns: 7:42 AM (9 days later)

"""