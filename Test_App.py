# Задание 1. Необходимо протестировать программу по работе с бухгалтерией
#
# Следует протестировать основные функции по получению информации о документах,
# добавлении и удалении элементов из словаря.
# Используйте fixture для загрузки данных в тестовый класс

import unittest
import os
import json
from io import StringIO
import sys
from mock import patch
from src import app


class TestSecretaryProgram(unittest.TestCase):

    def setUp(self):
        current_path = str(os.path.dirname(os.path.abspath(__file__)))
        f_directories = os.path.join(current_path, 'src/fixtures/directories.json')
        f_documents = os.path.join(current_path, 'src/fixtures/documents.json')
        with open(f_documents, 'r') as out_docs:
            app.documents = json.load(out_docs)
        with open(f_directories, 'r') as out_dirs:
            app.directories = json.load(out_dirs)

    def test_get_all_doc_owners_names(self):
        self.assertTrue(app.get_all_doc_owners_names())

    def test_get_doc_owner_name_exist(self):
        with patch('src.app.input', return_value='11-2'):
            self.assertEqual(app.get_doc_owner_name(), "Геннадий Покемонов")

    @patch('builtins.input', lambda x: '1111')
    def test_get_doc_owner_name_not_exist(self):
        self.assertFalse(app.get_doc_owner_name())

    def test_show_all_docs_info(self):
        sys.stdout = mystdout = StringIO()
        app.show_all_docs_info()
        self.assertTrue(mystdout.getvalue())

    @patch('builtins.input', lambda x: '11-2')
    def test_get_doc_shelf(self):
        self.assertEqual(app.get_doc_shelf(), '1')

    @patch('src.app.input')
    def test_add_new_doc(self, mock_input):
        mock_input.side_effect = ['Test_Number', 'Test_Type', 'Test_Name', 'Test_Shelf']
        app.add_new_doc()
        self.assertGreater(len(app.documents), 3)
        self.assertGreater(len(app.directories), 3)

    def test_delete_doc(self):
        with patch('src.app.input', return_value='11-2'):
            app.delete_doc()
        self.assertFalse(app.check_document_existance('11-2'))
        self.assertNotIn('11-2', app.directories['1'])

    @patch('src.app.input')
    def test_move_doc_to_shelf(self, mock_input):
        mock_input.side_effect = ['Test_Number', 'Test_Shelf']
        app.move_doc_to_shelf()
        self.assertIn('Test_Number', app.directories['Test_Shelf'])

    def test_add_new_shelf(self):
        app.add_new_shelf('500')
        self.assertIn('500', app.directories)

    @patch('builtins.input', lambda x: 'q')
    def test_secretary_program_start(self):
        self.assertFalse(app.secretary_program_start())


if __name__ == '__main__':
    unittest.main(buffer=True)
