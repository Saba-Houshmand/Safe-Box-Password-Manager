from project import email_format, birth_date_format, password_format

def test_email_format():
    assert email_format("saba.houshmand@gmail.com") == True
    assert email_format("saba.houshmand.gmail.com") == False
    assert email_format("saba.houshmand@.com") == False

def test_birth_date_format():
    assert birth_date_format("2006-11-19") == True
    assert birth_date_format("2023-1-1") == False
    assert birth_date_format("2006/11/19") == False

def test_password_format():
    assert password_format("1234") == True
    assert password_format("abcd") == False
    assert password_format("123") == False