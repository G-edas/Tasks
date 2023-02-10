import converter



def test_number_converter():
    assert converter.number_converter(489484848) == 'four hundred eighty nine million four hundred eighty four thousand eight hundred forty eight'
    assert converter.number_converter(-11123) == 'minus eleven thousand one hundred twenty three'
    assert converter.number_converter(1575745275) == 'one billion five hundred seventy five million seven hundred forty five thousand two hundred seventy five'
    assert converter.number_converter(-1245) == 'minus one thousand two hundred forty five'
    assert converter.number_converter(-2) == 'minus two'
    assert converter.number_converter(-5000) == 'minus five thousand'
    assert converter.number_converter(240) == 'two hundred forty'
    assert converter.number_converter(50000) == 'fifty thousand'
    assert converter.number_converter(-50000) == 'minus fifty thousand'
    assert converter.number_converter(0) == 'zero'


