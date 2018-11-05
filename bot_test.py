import requests, check
import requests_mock
import main_bot as mb

def test_do():
    with requests_mock.Mocker() as m:
        m.get('http://test.com', text='resp')
        assert requests.get('http://test.com').text == 'resp'

def test_checkPuppy():
    foo_content = '<source src="http://test.com" >'
    with requests_mock.Mocker() as m:
        m.get('http://200.7.6.134', status_code=200, text=foo_content)
        m.get('http://test.com', status_code=200)
        ok, resp = check.check_url('http://200.7.6.134')
        assert ok == True

def test_failed_checkPuppy():
    with requests_mock.Mocker() as m:
        m.get('http://200.7.6.134', status_code=401)
        ok, resp = check.check_url('http://200.7.6.134')
        assert ok == False

def test_failed_inner_checkPuppy():
    foo_content = '<source src="http://test.com" >'
    with requests_mock.Mocker() as m:
        m.get('http://200.7.6.134', status_code=200, text=foo_content)
        m.get('http://test.com', status_code=500)
        ok, resp = check.check_url('http://200.7.6.134')
        assert ok == False