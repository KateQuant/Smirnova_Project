import unittest

from qpa_final_project.data.script import *


class ScriptTest(unittest.TestCase):
    def test_convert_dna_to_rna(self):
        data_dna = {
            'test_actual_1': convert_dna_to_rna('Atgggca'),
            'test_actual_2': convert_dna_to_rna('T'),
            'test_actual_3': convert_dna_to_rna(123),
            'test_actual_4': convert_dna_to_rna('hjloko12'),
            'test_actual_5': convert_dna_to_rna('')
        }

        expected_answer = {
            'expected_1': 'UACCCGU',
            'expected_2': 'A',
            'expected_3': "Please input correct sequence that contain only 'ATGC' letters",
            'expected_4': "Please input correct sequence that contain only 'ATGC' letters",
            'expected_5': "",
        }

        # actual_1 = convert_dna_to_rna(data_dna['test_actual_1'])

        self.assertEqual(data_dna['test_actual_1'], expected_answer['expected_1'])
        self.assertEqual(data_dna['test_actual_2'], expected_answer['expected_2'])
        self.assertEqual(data_dna['test_actual_3'], expected_answer['expected_3'])
        self.assertEqual(data_dna['test_actual_4'], expected_answer['expected_4'])
        self.assertEqual(data_dna['test_actual_5'], expected_answer['expected_5'])

    def test_convert_rna_to_protein(self):
        data_dna = {
            'test_actual_1': convert_rna_to_protein('Uagcca'),
            'test_actual_2': convert_rna_to_protein('uua'),
            'test_actual_3': convert_rna_to_protein(123.0),
            'test_actual_4': convert_rna_to_protein('uuuaaag'),
            'test_actual_5': convert_rna_to_protein('')
        }

        expected_answer = {
            'expected_1': '.P',
            'expected_2': 'L',
            'expected_3': "Please input correct sequence of the form 'AUUCG'",
            'expected_4': "For translation to protein your sequence should be multiple by 3",
            'expected_5': "",
        }

        # actual_1 = convert_dna_to_rna(data_dna['test_actual_1'])

        self.assertEqual(data_dna['test_actual_1'], expected_answer['expected_1'])
        self.assertEqual(data_dna['test_actual_2'], expected_answer['expected_2'])
        self.assertEqual(data_dna['test_actual_3'], expected_answer['expected_3'])
        self.assertEqual(data_dna['test_actual_4'], expected_answer['expected_4'])
        self.assertEqual(data_dna['test_actual_5'], '')


if __name__ == '__main__':
    unittest.main()

