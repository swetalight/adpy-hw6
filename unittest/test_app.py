import unittest
import json
import os

from app import (
    init_app, remove_doc_from_shelf, append_doc_to_shelf, check_document_existance
)


def json_load(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


class SecretaryTestCase(unittest.TestCase):

    def setUp(self) -> None:
        base_path = os.path.abspath('.')
        directories_file_path = os.path.join(base_path, 'fixtures', 'directories.json')
        self.directories = json_load(directories_file_path) or None
        documents_file_path = os.path.join(base_path, 'fixtures', 'documents.json')
        self.documents = json_load(documents_file_path) or None

        self.test_doc_number = '10000000000 TEST DOCUMENT'
        self.test_shelf_number = '1'

        init_app(self.documents, self.directories)

    def test_documents(self):
        self.assertTrue((type(self.documents) == list), 'Check loaded documents data')

    def test_directories(self):
        self.assertTrue((type(self.directories) == dict), 'Check loaded directories data')

    def test_check_document_existance_success(self):
        self.assertTrue(check_document_existance('2207 876234'))

    def test_check_document_existance_failed(self):
        self.assertFalse(check_document_existance('-'))

    def test_append_doc_to_shelf(self):
        using_shelf = self.test_shelf_number
        old_shelf_len = len(self.directories[using_shelf])
        new_doc_number = self.test_doc_number
        append_doc_to_shelf(doc_number=new_doc_number, shelf_number=using_shelf)
        new_shelf_len = len(self.directories[using_shelf])
        self.assertGreater(new_shelf_len, old_shelf_len)

    def test_remove_doc_from_shelf(self):
        using_shelf = self.test_shelf_number
        remove_doc_number = self.test_doc_number
        append_doc_to_shelf(remove_doc_number, using_shelf)
        old_shelf_len = len(self.directories[using_shelf])
        remove_doc_from_shelf(remove_doc_number)
        new_shelf_len = len(self.directories[using_shelf])
        self.assertGreater(old_shelf_len, new_shelf_len)


if __name__ == '__main__':
    unittest.main()
