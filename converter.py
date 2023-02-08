import constants
import logging

def number_converter(n):
    
    numbers_devided = []
    number_tuple = tuple()
    number = str(n)
    number_list = list(number)
    minus = ''
    
    if(number[0] == '-'):
            minus = 'minus '
            number = number[1:]

    if(len(number) < 5 or int(number) in constants.number_dict.keys() 
       or number == constants.ZEROS_ONE_MILLION or number == constants.ZEROS_ONE_BILLION):

        if (number == constants.ZEROS_ONE_THOUSAND or number == constants.ZEROS_ONE_MILLION 
            or number == constants.ZEROS_ONE_BILLION):
            
            numbers_devided = [int('1'+number)]
            
        else:   
            for i in range(len(number_list)):
                
                numbers_devided.append(number_list[i] + int(len(number_list) - i - 1) * '0')
                numbers_devided = [int(el) for el in numbers_devided]
                numbers_devided = [item for item in numbers_devided if item != 0]
            
            if(sum(numbers_devided[-2:]) in constants.numberTEEN):
                
                summed_digits = sum(numbers_devided[-2:])
                del numbers_devided[-2:]
                numbers_devided.append(summed_digits)
                
            for i in range(len(numbers_devided)):          
                counter = list(str(numbers_devided[i])).count('0')
                if(counter == 0):
                    counter = 'none'
                if(len(str(numbers_devided[i])) - 1 == counter and counter !=1 ):
                    
                    numbers_devided[i] = list(number_tuple + (
                                                        int(str(numbers_devided[i])[0])
                                                        ,round(numbers_devided[i]/ int(str(numbers_devided[i])[0]))
                                                        ))   
        result = []
        for item in numbers_devided:
            if isinstance(item, list):
                result.extend(item)
            else:   
                result.append(item)

        number_in_words = ''
        for list_item in result:
            for dict_key in constants.sorted_number_dict.keys():
                if dict_key == list_item:
                    number_in_words += ''+constants.sorted_number_dict[dict_key]+' '
                        
        return number_in_words
       
    elif(len(number) >= 5):
        
        constants.number_devidor(number)
        
    full_word = ''
    for el in constants.number_devidor(number):
        full_word = full_word + number_converter(el)
       
    return minus + full_word
    
print(number_converter(-132481981564))

