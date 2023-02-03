import operator

def converter(a):
    number_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',13:
    'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen'
    , 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30:'thirty', 40:'forty', 50: 'fifty',
    60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand', 
    1000000: 'million', 1000000000: 'billion', 1000000000000: 'trillion'
    }
    sort_data = sorted(number_dict.items(), reverse=True)
    sorted_number_dict = dict(sort_data)
    
    
    number_to_append = []
    number_tuple = tuple()
    new_list = []
    number = str(a)
    number_list = list(str(number))
    for i in range(len(number_list)):
        
        number_to_append.append(number_list[i] + int(len(number_list) - i - 1) * '0')
        number_to_append = [int(el) for el in number_to_append]
        number_to_append_without_0 = [item for item in number_to_append if item != 0]
    print(number_to_append_without_0)

    for i in range(len(number_to_append_without_0)):
        counter = list(str(number_to_append_without_0[i])).count('0')
        if(counter == 0):
            counter = 'none'
        if(len(str(number_to_append_without_0[i])) - 1 == counter and counter !=1 ):
            
            number_to_append_without_0[i] = list(number_tuple + (
                                                int(str(number_to_append_without_0[i])[0])
                                                ,round(number_to_append_without_0[i]/ int(str(number_to_append_without_0[i])[0]))
                                                ))
            
            result = []
            for item in number_to_append_without_0:
                if isinstance(item, list):
                    result.extend(item)
                else:   
                    result.append(item)

    number_in_words = ''
    for list_item in result:
        for dict_key in sorted_number_dict.keys():
            if dict_key == list_item:
                number_in_words += ''+sorted_number_dict[dict_key]+' '
                
    return number_in_words

  
print(converter(10001))

