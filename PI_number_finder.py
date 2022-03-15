# PI_number_finder



def PI_numer_enter():
    global User_Input
    User_Input = input("Enter the decimal place of PI, you would like to know")
    
    pass

PI_numer_enter()

PI_raw = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
PI_ready = PI_raw - 3


PI_List = []




Loop_var = int(User_Input) + 1



for i in range(Loop_var):
    PI_ready = PI_ready * 10
    List_var = PI_ready // 1

    PI_List.append(List_var)
    
    PI_ready = PI_ready - List_var


print(PI_List[int(User_Input)-1])












