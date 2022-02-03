import unittest
from app import*
from unittest.mock import patch

class TestFunctions(unittest.TestCase):

    def test_check_document_existance(self):
        self.assertEqual(check_document_existance('2207 876234'), True)

    @patch('builtins.input', side_effect=['2207 876234'])
    def test_get_doc_owner_name(self,mock_input):
        result = get_doc_owner_name()
        self.assertEqual(result, 'Василий Гупкин')

    def test_get_all_doc_owners_names(self):
        self.assertEqual(get_all_doc_owners_names(), {'Василий Гупкин', 'Аристарх Павлов', 'Василий Теркин'})

    def test_remove_doc_from_shelf(self):
        self.assertEqual(remove_doc_from_shelf('5455 028765'), ([['234'], ['10006'], ['9', '2207 876234'], []]))

    @patch('builtins.input', side_effect=['1', '5'])
    def test_add_new_shelf(self, mock_input):
        calling_1 = mock_input()
        calling_2 = mock_input()
        self.assertEqual(add_new_shelf(calling_1),  ('1', False))
        self.assertEqual(add_new_shelf(calling_2), ('5', True))

    @patch('builtins.input', side_effect=['11-2'])
    def test_delete_doc(self, mock_input):
        result = delete_doc()
        self.assertEqual(result,  ('11-2', True))

    def test_append_doc_to_shelf(self):
        self.assertEqual(append_doc_to_shelf('9', '3'), ['9'])

    @patch('builtins.input', side_effect=['2207 876234'])
    def test_get_doc_shelf(self, mock_input):
        self.assertEqual(get_doc_shelf(),  '1')

    @patch('builtins.input', side_effect=['2207 876234', '3'])
    def test_move_doc_to_shelf(self, mock_input):        
        result = move_doc_to_shelf()
        self.assertEqual(result, ('2207 876234', '3'))

    def test_show_document_info(self):
        self.assertEqual(show_document_info({'type':'passport', 'number':'2207 876234', 'name':'Василий Гупкин'}), ('passport', '2207 876234', 'Василий Гупкин'))

    @patch('builtins.input', side_effect=['234', 'passport', 'Василий Теркин', '1'])
    def test_add_new_doc(self, mock_input):
        result = add_new_doc()
        self.assertEqual(result, '1')

if __name__ == '__main__':
    unittest.main()