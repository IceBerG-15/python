def convert_to_ist(day, hour, minute):
    # Check if input is within valid ranges
    ist_hour_diff = 5
    ist_minute_diff = 30
    ist_hour = hour + ist_hour_diff
    ist_minute = minute + ist_minute_diff
    if ist_minute >= 60:
        ist_minute -= 60
        ist_hour += 1
    if ist_hour >= 24:
        day = (day + 1) % 7
        ist_hour %= 24
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return days_of_week[day], ist_hour, ist_minute

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
            ist_day, ist_hour, ist_minute = convert_to_ist(day, hour, minute)
            print(f"In IST, it's {ist_day} {ist_hour:02d}:{ist_minute:02d}")
            print('--------------------------------------')

if __name__=='__main__':
    main()