from twttr import shorten

def main():
    test_upper_case()
    test_number()
    test_punctuation()

def test_upper_case():
    assert shorten("twitter") == 'twttr'
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('TwItTeR') == 'TwtTR'

def test_number():
    assert shorten('12345') == '12345'
    assert shorten('67890') == '67890'
def test_punctuation():
    assert shorten(',?!:;.') == ',?!:;.'

if __name__ =='__main__':
    main()
