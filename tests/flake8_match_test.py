import ast

from flake8_match import Plugin


def results(s):
    return {'{}:{}: {}'.format(*r) for r in Plugin(ast.parse(s)).run()}


def test_trivial():
    assert not results('')


def test_assignment_expression_not_ok():
    src = '''\
match 1:
    case 1:
        print(1)
'''
    msg, = results(src)
    assert msg == '1:0: MAT001 do not use match statements'
