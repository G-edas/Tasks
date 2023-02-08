import logging
# declare constants
ZEROS_ONE_THOUSAND = '000'
ZEROS_ONE_MILLION = '000000'
ZEROS_ONE_BILLION = '000000000'
ZEROS_ONE_TRILLION = '000000000000'
numberTEEN = range(11,20)

number_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',13:
    'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen'
    , 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30:'thirty', 40:'forty', 50: 'fifty',
    60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand', 
    1000000: 'million', 1000000000: 'billion'
    # , 1000000000000: 'trillion'
}

sort_data = sorted(number_dict.items(), reverse=True)
sorted_number_dict = dict(sort_data)

def number_devidor(number):
    
    try:
        if(len(number) in range(5, 7)):
            parsing_number = [int(number) // 1000, '000',  int(number) % 1000]
        elif(len(number) in range(7, 10)):
            parsing_number = [int(number) // 1000000, '000000',  int(number) % 1000000]
        elif(len(number) in range(10,13)):  
            parsing_number = [int(number) // 1000000000, '000000000',  int(number) % 1000000000]
        # elif(len(number) in range(13,16)):  
        #     parsing_number = [int(number) // 1000000000000, '000000000000',  int(number) % 1000000000000]
        
        return parsing_number
    except:
        raise Exception("Number is out -999 billion to 999 billion range")