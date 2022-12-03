import unittest
from Bio import SeqIO

from qpa_final_project.utils_old.misc.plot_for_test import gc_content_plot
from qpa_final_project.data.config import PATH_TO_DOCS_FROM_NCBI


class ScriptTest(unittest.TestCase):
    def test_gc_content_plot(self):
        dict_to_test = {}
        for fasta in SeqIO.parse(f"{PATH_TO_DOCS_FROM_NCBI}sequences_test.fasta", "fasta"):
            dict_to_test[fasta.id] = str(fasta.seq)

        sequences = {
            'test_actual_1': gc_content_plot(dict_to_test['Nucleotide_sequence'], 'Nucleotide_sequence'),
            'test_actual_2': gc_content_plot(dict_to_test['Protein_sequence'], 'Protein_sequence'),
            'test_actual_3': gc_content_plot(dict_to_test['Short_nucleotide'], 'Short_nucleotide'),
            'test_actual_4': gc_content_plot(dict_to_test['Nucleotide_with_N'], 'Nucleotide_with_N'),
            'test_actual_5': gc_content_plot(dict_to_test['Unreal_with_numbers'], 'Unreal_with_numbers')
        }

        expected_answer = {
            'expected_1': f"{PATH_TO_DOCS_FROM_NCBI}Nucleotide_sequence.png",
            'expected_2': "Invalid string! It should contain only 'ATGC' letters and be longer than 100",
            'expected_3': "Invalid string! It should contain only 'ATGC' letters and be longer than 100",
            'expected_4': "Invalid string! It should contain only 'ATGC' letters and be longer than 100",
            'expected_5': "Invalid string! It should contain only 'ATGC' letters and be longer than 100",
        }

        self.assertEqual(sequences['test_actual_1'], expected_answer['expected_1'])
        self.assertEqual(sequences['test_actual_2'], expected_answer['expected_2'])
        self.assertEqual(sequences['test_actual_3'], expected_answer['expected_3'])
        self.assertEqual(sequences['test_actual_4'], expected_answer['expected_4'])
        self.assertEqual(sequences['test_actual_5'], expected_answer['expected_5'])


if __name__ == '__main__':
    unittest.main()
