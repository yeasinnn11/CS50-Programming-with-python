from plates import is_valid

def main():
    test_min_and_max_characters()
    test_start_with_two_latters()
    
    test_punctuation()
    test_number_zero()

def test_min_and_max_characters():
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFGH")== False
def test_start_with_two_latters():
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid('22') == False

def test_number_zero():
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False
def test_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("PI3!14") == False
    assert is_valid('PI 14') == False

if __name__ == "__main__":
    main()
