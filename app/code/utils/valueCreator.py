import random


def value_selector_for_body(value):
    if value == 'a':
        a = [ x for x in range(1,25+1) ]
        print("a: ",a)
        value = value+str(random.choice(a))
    elif value == 'aa':
        a = [ x for x in range(1,8+1) ]
        print("aa: ",a)
        value = value+str(random.choice(a))
    return value

def random_value_genrator(number_of_value, difference=7, list_of_values=['a','b']):
    difference_list = [difference+2,difference,difference+4]
    counter = 0 
    value_list = []
    value = random.choice(list_of_values)
    for i in range(number_of_value):
        if counter <= difference:
            counter += 1
        else:
            difference = random.choice(difference_list)
            value = random.choice(list_of_values)   
            counter = 0
        value_list.append(value)
    return value_list

def random_value_genrator_for_body(number_of_value, difference=4, list_of_values=['a','aa']):
    difference_list = [difference+2,difference,difference+4]
    counter = 0 
    value_list = []
    value = random.choice(list_of_values)
    value = value_selector_for_body(value)
    for i in range(number_of_value):
        if counter <= difference:
            counter += 1
        else:
            difference = random.choice(difference_list)
            counter = 0
            value = random.choice(list_of_values)
            value = value_selector_for_body(value)
            
        value_list.append(value)
    return value_list

# how to use it 
if __name__ == '__main__':
    a = random_value_genrator_for_body(200, difference=10, list_of_values=['a','aa'])
    print(a)

