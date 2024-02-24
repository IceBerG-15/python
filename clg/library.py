actual_date = input("enter actual date:(dd/mm/yy) ")
expected_date = input("enter expected date:(dd/mm/yy) ")
fine = 0
if actual_date==expected_date:
    fine = 0
else:
    actual_date = actual_date.split("/")
    expected_date = expected_date.split("/")
    if actual_date[1]==expected_date[1] and actual_date[0]!=expected_date[0]:
        fine = 15*(int(actual_date[0]) - int(expected_date[0]))
    elif actual_date[2]==expected_date[2] and actual_date[1]!=expected_date[1]:
        fine = 500*(int(actual_date[1]) - int(expected_date[1]))
    else:
        fine = 10000
print('Fine: ',fine)
