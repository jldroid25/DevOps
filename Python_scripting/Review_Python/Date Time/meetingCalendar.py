#------- A Script to write an Upcoming  Meeting calendar Date --------

import calendar

print("Next Team Meetings will be on: ")
# 1 --> 13 due to 0 based List[] indexes
for m in range(1, 13): 
    
    cal = calendar.monthcalendar(2021, m)
    
    weekone = cal[0]
    weektwo = cal[1]
   
    # if That Friday is not an overlapping from previous or next month
    # the meeting should be on the first of current month
    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        # put on the Friday second week of current month
        meetday = weektwo[calendar.FRIDAY]

    print("%10s %2s" % (calendar.month_name[m], meetday))
