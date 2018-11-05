import requests, check
import requests_mock
import main_bot as mb

def test_do():
    with requests_mock.Mocker() as m:
        m.get('http://test.com', text='resp')
        assert requests.get('http://test.com').text == 'resp'

def test_checkPuppy():
    # Have empty list to avoid test
    subscribed_users = list()
    with requests_mock.Mocker() as m:
        m.get('http://200.7.6.134', status_code=200, text='resp')
        ok, resp = check.check_url('http://200.7.6.134')
        assert ok == True