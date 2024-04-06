from um import count

def main():
    pass

def test_upper_lower_case():
    assert count("Um, thanks for the album") == 1
    assert count("Um, thanks, um...") == 2
def test_word_with_um():
    assert count("yummi") == 0

def test_around_by_space():
    assert count("hello um world") == 1
    assert count("um?") == 1

if __name__ =='__main__':
    main()
