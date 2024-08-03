def mRna_to_protein(mRNA):
    protein = ''
    index = 0
    for idx, i in enumerate(mRNA):
        if i == 'A':
            if mRNA[idx+1] == 'U':
                if mRNA[idx+2] == 'G':
                    index = idx
                    break
                else:
                    continue
            else:
                continue
        else:
            continue

    amino = {
        'UUU': 'Phe', 'UUC': 'Phe',
        'UUA': 'Leu', 'UUG': 'Leu',
        'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser', 'AGU': 'Ser', 'AGC': 'Ser',
        'UAU': 'Tyr', 'UAC': 'Tyr',
        'UGU': 'Cys', 'UGC': 'Cys',
        'UGG': 'Trp',
        'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
        'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
        'CAU': 'His', 'CAC': 'His',
        'CAA': 'Gin', 'CAG': 'Gin',
        'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg', 'AGA': 'Arg', 'AGG': 'Arg',
        'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile',
        'AUG': 'Met',
        'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
        'AAU': 'Asn', 'AAC': 'Asn',
        'AAA': 'Lys', 'AAG': 'Lys',
        'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
        'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
        'GAU': 'Asp', 'GAC': 'Asp',
        'GAA': 'Glu', 'GAG': 'Glu',
        'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly',
        'UAA': 'Stop', 'UAG': 'Stop', 'UGA': 'Stop',
        '\n': ''
    }

    codon = mRNA[index:]
    codon_tri = []
    i = 0
    j = 3
    size = len(codon)
    while i < size:
        tri = codon[i:j]
        i = j
        j += 3
        codon_tri += [tri]
        protein += amino[tri] + '-'
        if tri == 'UAG' or tri == 'UAA' or tri == 'UGA':
            break
    print(protein)
