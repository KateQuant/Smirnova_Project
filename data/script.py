import re
# from Constants import AMINOACID_DICT
from db_query import get_rna_string, get_protein_string


def convert_dna_to_rna(dna_string: str) -> str:
    """Function that convert DNA to RNA"""

    dna_to_convert = str(dna_string).upper()
    dna_pattern = '^[ACTG]*$'

    if re.findall(dna_pattern, dna_to_convert):
        # rna = dna_to_convert.replace('T', 'U')
        rna = get_rna_string(dna_to_convert)
        return rna
    return "Please input correct sequence that contain only 'ATGC' letters"


def convert_rna_to_protein(rna_string: str) -> str:
    """Function that convert RNA to protein"""

    rna_to_convert = str(rna_string).upper()
    # rna_pattern = '^[ACUG]*$'

    try:
        # codon_step = range(0, len(rna_to_convert), 3)
        # aminoacids_list = [AMINOACID_DICT[rna_to_convert[i:i + 3]] for i in codon_step]
        # protein = ''.join(aminoacids_list)
        protein = get_protein_string(rna_to_convert)

        return protein

    except AttributeError:
        print("Incorrect RNA format. For translation to protein your sequence should be multiple by 3 and "
              "contain only 'AUUCG' letters.")

        # if len(rna_to_convert) % 3 != 0:
        #     print("For translation to protein your sequence should be multiple by 3")
        # else:
        #     print("Please input correct sequence of the form 'AUUCG'")


print(convert_dna_to_rna('ATTGATG'))
print(convert_rna_to_protein('AUGGGCAA'))
