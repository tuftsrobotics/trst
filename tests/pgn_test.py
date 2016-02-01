
from trst.pgns import Pgns
from tests.util import raises, get_sample_fp

def get_pgns_instance(fp):
    return Pgns(get_sample_fp(fp))

def test_init_with_default_fp():
    a = get_pgns_instance('default_pgns')
    assert type(a.valid_set) is set
    assert len(a.valid_set) == 7
    true_set = set([0x1F119, 0x1F801, 0x1F802, 0x1F805, 0x1F010, 0x1F112, 0x1FD02])
    assert a.valid_set == true_set

def test_init_with_null_file():
    a = get_pgns_instance('null')
    assert type(a.valid_set) is set
    assert len(a.valid_set) == 0

def test_init_with_multiline_file():
    a = get_pgns_instance('multiline_pgns')
    assert type(a.valid_set) is set
    assert len(a.valid_set) == 7
    true_set = set([0x1F119, 0x1F801, 0x1F802, 0x1F805, 0x1F010, 0x1F112, 0x1FD02])
    assert a.valid_set == true_set

def test_is_valid_func():
    a = get_pgns_instance('default_pgns')
    func = a.is_valid_pgn

    raises(ValueError, func, 'helloworld')
    raises(ValueError, func, '')
    raises(TypeError, func, 0x1F119)
    assert not func('0') 
    assert func('1F119')

def test_get_filter_func():
    a = get_pgns_instance('default_pgns')
    func = a.get_filter_func()

    raises(ValueError, func, 'helloworld')
    raises(ValueError, func, '')
    raises(TypeError, func, 0x1F119)
    assert not func('0') 
    assert func('1F119')

