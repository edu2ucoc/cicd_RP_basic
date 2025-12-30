from app import add, mul  # mul import 추가

# 곱하기 테스트
def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0

# 더하기 테스트
def test_mul():
    assert mul(2, 3) == 6
    assert mul(0, 5) == 0