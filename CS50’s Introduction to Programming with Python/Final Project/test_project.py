import pytest
from tkinter import Tk
from project import TextEditor

@pytest.fixture
def app():
    window = Tk()
    editor = TextEditor(window)
    yield editor
    window.destroy()

def test_open_file(app):
    # Check if open_file method inserts text into text area
    app.open_file()
    assert app.text_area.get(1.0, "end-1c") != ''
def test_save_file(app):
    # Check if save_file method saves text correctly
    app.text_area.delete(1.0, "end")
    app.text_area.insert(1.0, "Test text")
    app.save_file()
    app.open_file()
    saved_text = app.text_area.get(1.0, "end-1c")
    assert saved_text.strip() == "Test text"

def test_cut(app):
    # Check if cut method cuts the selected text
    app.text_area.delete(1.0, "end")
    app.text_area.insert(1.0, "Test text")
    app.text_area.tag_add("sel", "1.0", "1.4")
    app.cut()
    assert app.text_area.get(1.0, "end-1c") == " text"



def test_about(app):
    # Check if about method displays the about dialog
    app.about()
    # Since the about method just shows an info dialog, there's no error to raise or handle

if __name__ == "__main__":
    pytest.main()




