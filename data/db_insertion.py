from qpa_final_project.data.db_creation import Dna, Rna, Triplet, Aminoacid, session, session2
from qpa_final_project.Constants import AMINOACID_DICT

dna_nucleotides = ('T', 'G', 'C', 'A')
rna_nucleotides = ('A', 'C', 'G', 'U')

with session() as session:
    for d_nucl, r_nucl in zip(dna_nucleotides, rna_nucleotides):
        insert_dna = Dna(nucleotide=d_nucl)
        insert_rna = Rna(nucleotide=r_nucl, dna=insert_dna)
        session.add_all([insert_dna, insert_rna])
        session.commit()


triplets = tuple(AMINOACID_DICT.keys())
aminoacids = tuple(AMINOACID_DICT.values())

with session2() as session2:
    for tripl, amino in zip(triplets, aminoacids):
        insert_triplet = Triplet(triplet=tripl)
        insert_amino = Aminoacid(aminoacid=amino, triplet=insert_triplet)
        session2.add_all([insert_triplet, insert_amino])
        session2.commit()


