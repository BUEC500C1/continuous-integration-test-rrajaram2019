def lint_test(inp):
  out=inp*2
  return out

def test_func():
  assert lint_test(3)==6
  assert lint_test(5)==10
