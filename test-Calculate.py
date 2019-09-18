import pytest
@pytest.mark.parametrize("a,b,expected",[
                            (2,3,5),
                            (3,7,10),
                            ])
                            
def test_add(a, b, expected):#must be the same as the top
    from Calculate import add
    result = add(a,b)
    assert result == pytest.approx(expected)
