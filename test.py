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
    eq_(lam("x y->x+y")(1,2), 3)
    eq_(lam("x,y->x%y")(7,3), 1)
    eq_(lam("x y->x%y")(7,3), 1)
    eq_(lam("x,y,z->x-y+z")(3,4,6), 5)
    eq_(lam("x y z->x-y+z")(3,4,6), 5)


def test_single_arg_left_lack_op():
    eq_(lam("-5")(1), -4)
    eq_(lam("*2")(7), 14)
    eq_(lam("**2")(3), 9)

    my_mock = Mock()
    my_mock.a = 10
    my_mock.some_method.return_value = 3.14
    eq_(lam(".a")(my_mock), 10)
    eq_(lam(".some_method()")(my_mock), 3.14)

def test_special_parse_no_return_op():
    eq_(lam("x")(1), 1)
    eq_(lam("x*x")(5), 25)
    eq_(lam("x**3")(4), 64)
    eq_(lam("x+y")(4, 5), 9)


# def test_single_arg_right_lack_op_case0():
#     eq_(lam("2**")(10), 20)




## http://math.andrej.com/2009/04/09/pythons-lambda-is-broken/
def test_im_not_broken():
    func_list = [lam("x+%s"%i) for i in range(10)]
    eq_(func_list[0](0), 0)
    eq_(func_list[7](2), 9)
















