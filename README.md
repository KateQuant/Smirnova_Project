# Smirnova_Project

Telegram Bot "QuantBot" (@Smirnova_test_bot).

### QuantBot Functionality

Available Bot commands:

1. /start - start dialog with the Bot
2. /help - get information about Bot functionality
3. /transcribe - take as input string that contain only "ATGC" letters (not case-sensitive) and return string of RNA. Available inline button, where you could choose "Coding template" or "Noncoding template".
4. /translate - take as input string that multiply by 3 and contain only "AUGC" letters and return string translated to protein.
5. /accession - retrieve FASTA file by sequence accession number from NCBI “nucleotide“ database and build the gc-contenet plot on basis of it file.

## Project architecture and description
Main repository contain folders and files of the project.

### Files in qpa_final_project:
- requirements.txt - contain necessary requirements for the project
- app.py - Telegram bot run file
- loader.py - contain necessary settings for bot modules import
- Constants.py - contain dictionaries with the key-values that is necessary for RNA and DNA database infill (data/db_insertion.py)
- Dockerfile and docker-compose.yml - contain settings for Docker
- .gitignore - contain gitignore information
- LICENSE - MIT License
- setup.py - file that makes import inside project easier
- README.md - description file

### Folders in qpa_final_project:

- #### /data/:

  - config.py - configuration bot settings
  - db_creation.py - postgresql database creation file
  - db_insertion.py - postgresql database infill file
  - db_query.py - file contain functions that make query to DNA and Triplet database 
  - script.py - contain functions "convert_dna_to_rna", "convert_rna_to_protein", "get_prefix", "fasta_creator" and code with sys.argv
  
- #### /handlers/errors/:

    - init.py and error_handler.py - should catch specific errors, but I forgot to modify it...

- #### /handlers/users/:

  - start.py - script that describe bot reaction to "start" command
  - help.py - script that describe bot reaction to "help" command
  - transcribe.py - script that describe bot reaction to "transcribe" command
  - translate.py - script that describe bot reaction to "translate" command
  - accession.py - script that describe bot reaction to "accession" command
  
- #### /keyboards/inline/:

    - callback_datas.py - data store for dna_inline and plot_inline buttons
    - dna_inline.py - script for inline button after usage "transcribe" command
    - plot_inline.py - script for inline button after usage "accession" command

- #### utils_old/:

    - notify_admins.py - script for admins notification after bot run
    - set_bot_commands.py - script for "hot buttons" in Telegram menu

- #### utils_old/misc/:

    - logging.py - file with logging format
    - plot_for_test.py - plot script for unittest
    - plot_gc.py - plot script for bot and sys.argv usage
    - ticks_gc.py - separate function for correct tips plot display 

- #### unittest/:

    - test_plot.py - unittests that test plot creation function
    - test_script.py - unittests that test functions in script.py

- #### Downloaded_docs_ncbi/:

    - filled - empty file, was added to save this folder in project
    - sequences_test.fasta - fasta file with the sequences to test plot function correctly


