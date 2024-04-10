from seasons import check_birthday

def main():
    test_check_birthday()

def test_check_birthday():
    assert check_birthday("1999-01-01") == ("1999", "01", "01")
    assert check_birthday("1999-1-1") == None
    assert check_birthday("January 1, 1999") == None

if __name__=='__main__':
    main()
