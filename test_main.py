from main import add
import pytest

def test_add_default_values():
    assert add() == -3

def test_add_type_error():
    with pytest.raises(TypeError):
        add('1')

@pytest.mark.parametrize("a,b,c,r", [(10, -2, 50, 58), (-2.2, 2.2, -2.2, -2.2), (True, False, True, 2),
                                     (100+20j, -100-20j, -32+75j, -32+75j), ((1,), (2,), (3,), (1, 2, 3)),
                                     ('i ', 'love ', 'python & git', 'i love python & git'), (0, 0, 0, 0), 
                                     (['python'], ['git'], ['github'], ['python', 'git', 'github'])],
                                     ids=['int', 'float', 'bool', 'complex', 'turple', 'str', 'zero', 'list'])
def test_add(a, b, c, r):
    assert add(a, b, c) == r