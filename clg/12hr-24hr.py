time = input('enter time: ')
x = time[-2:]
hour = int(time.split(':')[0])
if hour==12 and x=='AM':
    print('00'+time[2:-2])
elif x=='PM':
    print(str(hour+12)+time[2:-2])