from bank import value

def main():
    test_arguments()
    test_return_20()
    test_return_100()

def test_arguments():
    assert value('hello gi') == 0
    assert value('Hello') == 0
    assert value('HELLO GI') == 0
def test_return_20():
    assert value('hey') == 20
    assert value('hi') == 20
def test_return_100():
    assert value("What's up?") == 100
    assert value("good morning") == 100

if __name__=='__main__':
    main()
