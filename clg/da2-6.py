def convert_to_greece(day, hour, minute):
    greece_hour_diff = 2
    greece_minute_diff = 30
    greece_hour = hour - greece_hour_diff
    greece_minute = minute - greece_minute_diff
    if greece_minute < 0:
        greece_minute += 60
        greece_hour -= 1
    if greece_hour < 0:
        day = (day - 1) % 7
        greece_hour %= 24
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return days_of_week[day], greece_hour, greece_minute

def main():
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    t = int(input("number of inputs: "))
    for _ in range(t):
        day = input('Enter the day: ')
        hour = int(input('Enter Hours: '))
        minute = int(input('Enter Minutes of time: '))
        if day not in days_of_week or hour<0 or hour>24 or minute<0 or minute>60:
            print('Invalid Input')
        else:
            day = days_of_week.index(day)
            gst_day, gst_hour, gst_minute = convert_to_greece(day, hour, minute)
            print(f"In IST, it's {gst_day} {gst_hour:02d}:{gst_minute:02d}")
            print('--------------------------------------')

if __name__=='__main__':
    main()