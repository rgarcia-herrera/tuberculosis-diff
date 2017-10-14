nrp1_24_tb = {'path': 'data/nrp1_nrp2/norm/nrp1_24h_tb.tsv',
           'title': 'NRP1 24h'}
nrp1_48_tb = {'path': 'data/nrp1_nrp2/norm/nrp1_48h_tb.tsv',
           'title': 'NRP1 48h'}
nrp2_24_tb = {'path': 'data/nrp1_nrp2/norm/nrp2_24h_tb.tsv',
           'title': 'NRP2 24h'}
nrp2_48_tb = {'path': 'data/nrp1_nrp2/norm/nrp2_48h_tb.tsv',
           'title': 'NRP2 48h'}

contrasts_tb = {
    'TB NRP1 24h vs. NRP1 48h': [nrp1_24_tb, nrp1_48_tb],
    'TB NRP2 24h vs. NRP2 48h': [nrp2_24_tb, nrp2_48_tb],

    'TB NRP1 24h vs. NRP2 24h': [nrp1_24_tb, nrp2_24_tb],
    'TB NRP1 48h vs. NRP2 48h': [nrp1_48_tb, nrp2_48_tb],

# pending inter-array normalization
#    'NPR1 24h vs. LOG 24h': [],
#    'NPR1 48h vs. LOG 48h': [],

#    'LOG 24h vs. LOG 48h': [],

}


nrp1_24_mo = {'path': 'data/nrp1_nrp2/norm/nrp1_24h_macrophage.tsv',
              'title': 'NRP1 24h'}
nrp1_48_mo = {'path': 'data/nrp1_nrp2/norm/nrp1_48h_macrophage.tsv',
              'title': 'NRP1 48h'}
nrp2_24_mo = {'path': 'data/nrp1_nrp2/norm/nrp2_24h_macrophage.tsv',
              'title': 'NRP2 24h'}
nrp2_48_mo = {'path': 'data/nrp1_nrp2/norm/nrp2_48h_macrophage.tsv',
              'title': 'NRP2 48h'}

contrasts_macrophage = {
    'Macrophage NRP1 24h vs. NRP1 48h': [nrp1_24_mo, nrp1_48_mo],
    'Macrophage NRP2 24h vs. NRP2 48h': [nrp2_24_mo, nrp2_48_mo],

    'Macrophage NRP1 24h vs. NRP2 24h': [nrp1_24_mo, nrp2_24_mo],
    'Macrophage NRP1 48h vs. NRP2 48h': [nrp1_48_mo, nrp2_48_mo],
}
