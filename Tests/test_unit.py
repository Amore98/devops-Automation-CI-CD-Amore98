from BE.calculator_helper import CalculatorHelper
from assertpy import assert_that
import pytest
##setup and teardown test 
class BaseTest:
    def setup_method(self):
       
        self.calculator = CalculatorHelper()
    
    def teardown_method(self):
        self.calculator = None


class TestCalculator(BaseTest) :

        
       

    def test_add(self):
        ##Arrange
        ##calculator = CalculatorHelper()
        ##Action
        value = self.calculator.add(1, 2)
        ##Assert
        assert value == 3
        assert_that(value).is_equal_to(3)
    def test_subtract(self):
        ##Arrange
        #calculator = CalculatorHelper()
        ##Action
       # value = calculator.subtract(1, 2)
        value = self.calculator.subtract(1, 2)
        ##Assert
        assert value == -1

    def test_multiply(self):
       # calculator = CalculatorHelper()
        #value = calculator.multiply(1, 2)
        #Acction
        value = self.calculator.multiply(1, 2)
        ##Assert
        assert value == 2

    def test_divide(self):
        #calculator = CalculatorHelper()
        #value = calculator.divide(1, 2)
        #Action
        value = self.calculator.divide(1, 2)
        ##Assert
        assert value == 0.5

    def test_divide_by_zero(self):

        with pytest.raises(ZeroDivisionError):
            self.calculator.divide(1, 0)


####DDT
@pytest.mark.parametrize("a,b, expected",
     [(3,3,6), 
      (2,-4, -2), 
      (6,9, 15)
 ])
def test_add_py(a,b, expected):
    calculator = CalculatorHelper()
    assert calculator.add(a,b) == expected