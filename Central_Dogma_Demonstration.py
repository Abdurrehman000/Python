def central_dogma():
    # 1. Get Input and Standardize
    dna_sequence = input("Enter DNA sequence: ")
    dna_upper = dna_sequence.upper() 
    valid_bases = ["A", "T", "G", "C"]
    is_valid = True
    
    # 2. Validation check
    for base in dna_upper:
        if base not in valid_bases:
            is_valid = False
            break
            
    if is_valid:
        print("Sequence is Valid.")
        
        # 3. Transcription (DNA -> RNA) decision
        rna_choice = input("Do you want to convert DNA sequence to RNA? (yes/no): ")
        
        # We use .lower() so "Yes", "YES", and "yes" all work
        if rna_choice.lower() == "yes":
            
            # Create RNA
            rna_sequence = dna_upper.replace("T", "U")
            print(f"RNA sequence is: {rna_sequence}")
            print(f"Total length of sequence is: {len(dna_upper)}")
            print("-" * 20)
            
            # 4. Translation (RNA -> Protein)
            # The dictionary is defined here so it's ready for translation
            codon_table = {
            # Phenylalanine
            "UUU": "Phenylalanine", "UUC": "Phenylalanine",
            # Leucine
            "UUA": "Leucine", "UUG": "Leucine", "CUU": "Leucine", "CUC": "Leucine", "CUA": "Leucine", "CUG": "Leucine",
            # Isoleucine
            "AUU": "Isoleucine", "AUC": "Isoleucine", "AUA": "Isoleucine",
            # Methionine (Start Codon)
            "AUG": "Methionine",
            # Valine
            "GUU": "Valine", "GUC": "Valine", "GUA": "Valine", "GUG": "Valine",
            # Serine
            "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine", "AGU": "Serine", "AGC": "Serine",
            # Proline
            "CCU": "Proline", "CCC": "Proline", "CCA": "Proline", "CCG": "Proline",
            # Threonine
            "ACU": "Threonine", "ACC": "Threonine", "ACA": "Threonine", "ACG": "Threonine",
            # Alanine
            "GCU": "Alanine", "GCC": "Alanine", "GCA": "Alanine", "GCG": "Alanine",
            # Tyrosine
            "UAU": "Tyrosine", "UAC": "Tyrosine",
            # Histidine
            "CAU": "Histidine", "CAC": "Histidine",
            # Glutamine
            "CAA": "Glutamine", "CAG": "Glutamine",
            # Asparagine
            "AAU": "Asparagine", "AAC": "Asparagine",
            # Lysine
            "AAA": "Lysine", "AAG": "Lysine",
            # Aspartic Acid
            "GAU": "Aspartic Acid", "GAC": "Aspartic Acid",
            # Glutamic Acid
            "GAA": "Glutamic Acid", "GAG": "Glutamic Acid",
            # Cysteine
            "UGU": "Cysteine", "UGC": "Cysteine",
            # Tryptophan
            "UGG": "Tryptophan",
            # Arginine
            "CGU": "Arginine", "CGC": "Arginine", "CGA": "Arginine", "CGG": "Arginine", "AGA": "Arginine", "AGG": "Arginine",
            # Glycine
            "GGU": "Glycine", "GGC": "Glycine", "GGA": "Glycine", "GGG": "Glycine",
            # Stop Codons
            "UAA": "STOP", "UAG": "STOP", "UGA": "STOP"
        }
            

            protein_sequence = ""
            
            print("Processing Codons...")
            
            # Loop through the DNA in steps of 3
            for i in range(0, len(dna_upper), 3):
                codon = dna_upper[i:i+3]
                
                # Check if we have a full codon (3 bases)
                if len(codon) == 3:
                    # Convert that specific DNA codon to RNA for the dictionary lookup
                    rna_codon = codon.replace("T", "U")
                    
                    if rna_codon in codon_table:
                        print(rna_codon)
                        amino_acid = codon_table[rna_codon]
                        
                        if amino_acid == "STOP":
                            print("Stop codon found. Translation ending.")
                            break # Exit the loop immediately
                        
                        protein_sequence += amino_acid + "-"
                    else:
                        # Handle unknown codons
                        protein_sequence += "?" + "-"
            
            # Print final result removing the last dash
            print(f"Final Protein sequence is: {protein_sequence.strip('-')}")

        else:
            # If user said "no"
            print("RNA conversion skipped. Program finished.")

    else:
        # If is_valid was False
        print("Sequence is Invalid. Program has finished.")

# Run the function
central_dogma()