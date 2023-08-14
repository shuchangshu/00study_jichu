import  math
import  pytest
from test02 import Rectangle
def test_area():
    sum1=Rectangle(10,80)
    assert sum1.area()==800
    # assert False

@pytest.mark.parametrize("expect",[200])
def test_perimeter(expect):
    sum2=Rectangle(10,90)
    assert sum2.perimeter()==expect
    # assert False


def test_diff():
    sum3=Rectangle(70,80)
    assert sum3.diff()==10
    # assert False

# 这里就是实例化一个公共资源my_sum

@pytest.fixture()
def my_rct():
    allsum=Rectangle(1,2)
    # 这个只用来返回对象，妈卖批
    return allsum
def test_resize(my_rct):
   assert my_rct.resize(10,20)==(10,20)
    # assert False


def test_get_length(my_sum):
    assert  my_sum.get_length()==70
    # assert False


@pytest.fixture()
def my_rct():
    allsum=Rectangle(10,20)
    # 这个只用来返回对象，妈卖批
    return allsum
@pytest.mark.parametrize(("length","width","expect"),[(20,10,10)])
def test_diff(my_rct,length, width, expect):
    # rect = Rectangle(length, width),产生的my_rct只能当对象，不能在进行赋值对象
    # assert my_rct.resize(length,width)==expect
    assert my_rct.diff (length, width) == pytest.approx (expect)


# @pytest.mark.parametrize(( "width", "expected_width"),[(80,60),( 100, 0)])
# def test_get_width( width, expected_width):
#     sum=Rectangle(,width)
#     assert sum.get_width()==
#     assert False
