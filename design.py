nrp1_24 = 'data/nrp1_nrp2/norm/nrp1_24h.txt'
nrp1_48 = 'data/nrp1_nrp2/norm/nrp1_48h.txt'
nrp2_24 = 'data/nrp1_nrp2/norm/nrp2_24h.txt'
nrp2_48 = 'data/nrp1_nrp2/norm/nrp2_48h.txt'

contrasts_tb = {
    'NRP1 24h vs. NRP1 48h': [nrp1_24, nrp1_48],
    'NRP2 24h vs. NRP2 48h': [nrp2_24, nrp2_48],

    'NRP1 24h vs. NRP2 24h': [nrp1_24, nrp2_24],
    'NRP1 48h vs. NRP2 48h': [nrp1_48, nrp2_48],

# pending inter-array normalization
#    'NPR1 24h vs. LOG 24h': [],
#    'NPR1 48h vs. LOG 48h': [],

#    'LOG 24h vs. LOG 48h': [],

}
