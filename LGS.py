print("Welcome to the letter grade system.")
a = int(input("please write your first midterm exam grade:"))
b = int(input("please write your second midterm exam grade:"))
c = int(input("please write your final exam grade:"))
d = c*(30/100)
e = b*(30/100)
f = c*(40/100)
g = d+e+f
if 90 <= g:
    print("Your grade is AA")
elif 85 <= g:
    print("Your grade is BA")
elif 80 <= g:
    print("Your grade is BB")
elif 75 <= g:
    print("Your grade is CB")
elif 70 <= g:
    print("Your grade is CC")
elif 65 <= g:
    print("Your grade is DC")
elif 60 <= g:
    print("Your grade is DD")
elif 55 <= g:
    print("Your grade is FD")
else:
    print("Your grade is FF")




