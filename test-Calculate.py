import pytest
@pytest.mark.parametrize("a,b,expected", [
                            (2,3,5),
                            (3,7,10),
                            ])
                            
def test_add(a, b, expected):#must be the same as the top
    from Calculate import add
    answer = add(a,b)
    assert answer == pytest.approx(expected)