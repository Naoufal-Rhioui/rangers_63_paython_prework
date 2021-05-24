def hello_name(user_name):
    print("Hello " + user_name.title() + '!')
#hello_name('naoufal')

def odd_numbers():
    for i in range(1,101,2):
        print(i)
        
#odd_numbers()

def max_num_in_list(a_list):
    max_num = max(a_list)
    return max_num

test = max_num_in_list([2,3,5,8,9])
#print(max_num_in_list([2,3,5,8,9]))


def is_leap(a_year):
    if a_year % 4 == 0 and (a_year % 400 == 0 or a_year % 100 != 0):
        print(True)
    else:
        print(False)

#is_leap_year(2019)



def checkConsecutive(l):
	return sorted(l) == list(range(min(l), max(l)+1))
	
lst = [2, 3, 1, 4, 5]
#print(checkConsecutive(lst))
