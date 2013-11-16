from nose.tools import nottest, istest, raises,eq_,ok_
from mock import Mock

from lamstr import lam

def test_single__arg_return_lambda_gen():
    eq_(lam("x->None")(0), None)
    eq_(lam("x->x")(1), 1)
    eq_(lam("x->x*x")(2), 4)
    eq_(lam("x->x**x")(3), 27)

def test_multi_args_return_lambda_gen():
    eq_(lam("x,y->x+y")(1,2), 3)
    eq_(lam("x,y->x%y")(7,3), 1)
    eq_(lam("x,y,z->x-y+z")(3,4,6), 5)


def test_single_arg_left_lack_op():
    eq_(lam("-5")(1), -4)
    eq_(lam("*2")(7), 14)

    my_mock = Mock()
    my_mock.a = 10
    my_mock.some_method.return_value = 3.14
    eq_(lam(".a")(my_mock), 10)
    eq_(lam(".some_method()")(my_mock), 3.14)

def test_special_parse_no_return_op():
    eq_(lam("x")(1), 1)
    eq_(lam("x*x")(5), 25)
    eq_(lam("x**3")(4), 64)


