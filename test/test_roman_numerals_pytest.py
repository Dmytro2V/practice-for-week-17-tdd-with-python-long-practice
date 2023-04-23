from app.roman_numerals import parse

def test_roman_numeral_parser():
    def test_IX():
        value = parse('IX')

        assert value == 9