from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

from qpa_final_project.data.config import PG_USER, PG_PASSWORD, IP, PORT

# engine = create_engine("sqlite:///dna_rna.db")  # sqlight version
url_1 = f"postgresql://{PG_USER}:{PG_PASSWORD}@{IP}:{PORT}/dna_rna"
engine = create_engine(url_1)  # echo=True

# engine2 = create_engine("sqlite:///rna_protein.db")  # sqlight version
url_2 = f"postgresql://{PG_USER}:{PG_PASSWORD}@{IP}:{PORT}/rna_protein"
engine2 = create_engine(url_2)  # echo=True

Base = declarative_base()


class Dna(Base):
    __tablename__ = "dna_table"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    nucleotide = Column(String(1))
    rna = relationship("Rna", back_populates="dna")

    def __str__(self):
        return f"{self.nucleotide}"


class Rna(Base):
    __tablename__ = "rna_table"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    nucleotide = Column(String(1))
    dna_id = Column(Integer, ForeignKey("dna_table.id"))
    dna = relationship("Dna", back_populates="rna")

    def __str__(self):
        return f"{self.nucleotide}"


class Triplet(Base):
    __tablename__ = "triplet_table"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    triplet = Column(String(3))
    aminoacid = relationship("Aminoacid", back_populates="triplet")

    def __str__(self):
        return f"{self.triplet}"


class Aminoacid(Base):
    __tablename__ = "aminoacid_table"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    aminoacid = Column(String(1))
    triplet_id = Column(Integer, ForeignKey("triplet_table.id"))
    triplet = relationship("Triplet", back_populates="aminoacid")

    def __str__(self):
        return f"{self.aminoacid}"


Base.metadata.create_all(engine)
Base.metadata.create_all(engine2)

session = sessionmaker(bind=engine)
session2 = sessionmaker(bind=engine2)
