import mock
import sender

def test_sender():
    with mock.patch('socket.socket'):
        c = MyClass()
        c.tcp_socket.connect.assert_called_with('0.0.0.0', '6767')

from mock import ANY

class MyS():
    def connect(self, address): #The signature
        pass

@patch("socket.socket.connect", autospec=sender.send_data, side_effect=socket.socket.connect)
@override_settings(SERVER_IP='127.0.0.1')
def test_ip_from_settings(self, connect_mock):
    """
    The IP to connect to is taken from the Django settings.
    """
    result = connections.get_result()
    connect_mock.assert_called_with(ANY,('127.0.0.1', TCP_PORT))