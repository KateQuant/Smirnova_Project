from db_creation import Dna, Triplet, session, session2


def get_rna_string(dna_string: str, session=session) -> str:
    """A function that sends a query to a database to retrieve RNA nucleotides corresponding to DNA"""

    rna_string = ''
    with session() as session:
        for letter in dna_string:
            basis = session.query(Dna).filter(Dna.nucleotide == letter).first()
            rna_string += str(basis.rna[0])

    return rna_string


def get_protein_string(rna_string: str, session=session2) -> str:
    """A function that sends a query to a database to retrieve aminoacids corresponding to RNA"""

    protein = ''
    index = 0

    with session2() as session:
        while index < len(rna_string):
            codon = rna_string[index: index + 3]
            aminoacid = session.query(Triplet).filter(Triplet.triplet == codon).first()
            protein += str(aminoacid.aminoacid[0])
            index += 3

    return protein


# print(get_rna_string('TTTAGC'))
# print(get_protein_string('UUGGGCAAU'))
