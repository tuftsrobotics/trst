from trst.navigation.pid import PID

def test_pid():
    a = PID()
    res = a.update(5.0)
    assert type(res) == float
