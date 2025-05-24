import exercises_1
import unittest

class TestOperations(unittest.TestCase):
    def test_add_operands(self):
        self.assertEqual(exercises_1.add_operands(2,3), 5)
        self.assertEqual(exercises_1.add_operands(0,0), 0)

    def test_substract_operands(self):
        self.assertEqual(exercises_1.substract_operands(2,3), -1)
        self.assertEqual(exercises_1.substract_operands(0,0), 0)
        self.assertEqual(exercises_1.substract_operands(5,1), 4)
        self.assertEqual(exercises_1.substract_operands(5,-1), 6)

    def test_multiply_operands(self):
        self.assertEqual(exercises_1.multiply_operands(2,3), 6)
        self.assertEqual(exercises_1.multiply_operands(0,0), 0)
        self.assertEqual(exercises_1.multiply_operands(5,-1), -5)

    def test_yearly_salary(self):
        self.assertAlmostEqual(exercises_1.calculate_year_salary(17.5), 36400)
        self.assertEqual(exercises_1.calculate_year_salary(0), 0)
        self.assertEqual(exercises_1.calculate_year_salary(1), 2080)

    def test_hello_name(self):
        self.assertEqual(exercises_1.hello_string("Luis"), "Hello Luis")
        self.assertEqual(exercises_1.hello_string(""), "Hello ")
        self.assertEqual(exercises_1.hello_string("a"), "Hello a")

    def test_repeat_string(self):
        self.assertEqual(exercises_1.repeat_string("*",3), "***")
        self.assertEqual(exercises_1.repeat_string("",10), "")
        self.assertEqual(exercises_1.repeat_string("a", 0), "")
        self.assertEqual(exercises_1.repeat_string("a", 5), "aaaaa")
    
    def test_create_list(self):
        returned_list = exercises_1.create_list()
        self.assertEqual(len(returned_list), 5)
        self.assertEqual(type(returned_list), list)
    
    def test_list_size(self):
        self.assertEqual(exercises_1.list_size([]), 0)
        self.assertEqual(exercises_1.list_size(["a", "b", "c"]), 3)
        self.assertEqual(exercises_1.list_size(["abc"]), 1)
        self.assertEqual(exercises_1.list_size([1,2,3,4,5]), 5)

    def test_extract_list_element(self):
        self.assertEqual(exercises_1.get_list_element([1,2,3,4,5], -1), None)
        self.assertEqual(exercises_1.get_list_element([1,2,3,4,5], 5), None)
        self.assertEqual(exercises_1.get_list_element([1,2,3,4,5], 6), None)
        self.assertEqual(exercises_1.get_list_element([], 0), None)
        self.assertEqual(exercises_1.get_list_element([1,2,3,4,5], 1), 2)
        self.assertEqual(exercises_1.get_list_element([1,2,3,4,5], 4), 5)
        self.assertEqual(exercises_1.get_list_element([1,2,3,4,5], 0), 1)
    
    def test_list_range(self):
        self.assertEqual(exercises_1.get_list_range([1,2,3,4,5], 0,2), [1,2])
    
    def test_replace_list_element(self):
        self.assertEqual(exercises_1.replace_list_element([1,2,3,4,5], 0, 0), [0,2,3,4,5])
        self.assertEqual(exercises_1.replace_list_element([], 0, 0), [])
        
    def test_add_element_list(self):
        self.assertEqual(exercises_1.add_element_end([],3),[3])
        self.assertEqual(exercises_1.add_element_end([5,4],3),[5,4,3])
    
    def test_merge_lists(self):
        self.assertEqual(exercises_1.merge_lists([2],[7,8]), [2,7,8])
    
    def test_create_tuple(self):
        returned_tuple = exercises_1.create_tuple()
        self.assertEqual(len(returned_tuple), 5)
        self.assertEqual(type(returned_tuple), tuple)

    def test_create_dictionary(self):
        returned_dictionary = exercises_1.create_dictionary()
        self.assertEqual(len(returned_dictionary), 2)
        self.assertEqual(type(returned_dictionary), dict)
    
    def test_dictionary_add_element(self):
        dictionary = {}
        exercises_1.replace_or_insert_dict_value(dictionary,"first", 1)
        self.assertEqual(len(dictionary), 1)
        self.assertEqual(dictionary['first'], 1)
        dictionary['second'] = 0
        exercises_1.replace_or_insert_dict_value(dictionary,"second", 3)
        self.assertEqual(len(dictionary), 2)
        self.assertEqual(dictionary['second'], 3)
    
    def test_greater_than(self):
        self.assertEqual(exercises_1.x_greater_y(4,3), True)
        self.assertEqual(exercises_1.x_greater_y(3,4), False)
        self.assertEqual(exercises_1.x_greater_y(0,0), False)
    
    def test_greater_equal_than(self):
        self.assertEqual(exercises_1.x_greater_equal_than_y(4,3), True)
        self.assertEqual(exercises_1.x_greater_equal_than_y(3,4), False)
        self.assertEqual(exercises_1.x_greater_equal_than_y(0,0), True)

    def test_equal_than(self):
        self.assertEqual(exercises_1.x_equal_y(4,3), False)
        self.assertEqual(exercises_1.x_equal_y(3,4), False)
        self.assertEqual(exercises_1.x_equal_y(0,0), True)
    
    def test_less_equal_than(self):
        self.assertEqual(exercises_1.x_less_equal_than_y(4,3), False)
        self.assertEqual(exercises_1.x_less_equal_than_y(3,4), True)
        self.assertEqual(exercises_1.x_less_equal_than_y(0,0), True)
    
    def test_less_than(self):
        self.assertEqual(exercises_1.x_less_than_y(4,3), False)
        self.assertEqual(exercises_1.x_less_than_y(3,4), True)
        self.assertEqual(exercises_1.x_less_than_y(0,0), False)
        

if __name__ == "__main__":
    unittest.main()
