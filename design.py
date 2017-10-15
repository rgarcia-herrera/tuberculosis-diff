nrp1_24_tb = {'path': 'data/nrp1_nrp2/norm/nrp1_24h_tb.tsv',
           'title': 'NRP1 24h'}
nrp1_48_tb = {'path': 'data/nrp1_nrp2/norm/nrp1_48h_tb.tsv',
           'title': 'NRP1 48h'}
nrp2_24_tb = {'path': 'data/nrp1_nrp2/norm/nrp2_24h_tb.tsv',
           'title': 'NRP2 24h'}
nrp2_48_tb = {'path': 'data/nrp1_nrp2/norm/nrp2_48h_tb.tsv',
           'title': 'NRP2 48h'}

nrp_tb = {
    'TB NRP1 24h vs. NRP1 48h': [nrp1_24_tb, nrp1_48_tb],
    'TB NRP2 24h vs. NRP2 48h': [nrp2_24_tb, nrp2_48_tb],

    'TB NRP1 24h vs. NRP2 24h': [nrp1_24_tb, nrp2_24_tb],
    'TB NRP1 48h vs. NRP2 48h': [nrp1_48_tb, nrp2_48_tb],
}


nrp1_24_mo = {'path': 'data/nrp1_nrp2/norm/nrp1_24h_macrophage.tsv',
              'title': 'NRP1 24h'}
nrp1_48_mo = {'path': 'data/nrp1_nrp2/norm/nrp1_48h_macrophage.tsv',
              'title': 'NRP1 48h'}
nrp2_24_mo = {'path': 'data/nrp1_nrp2/norm/nrp2_24h_macrophage.tsv',
              'title': 'NRP2 24h'}
nrp2_48_mo = {'path': 'data/nrp1_nrp2/norm/nrp2_48h_macrophage.tsv',
              'title': 'NRP2 48h'}

nrp_macrophage = {
    'Macrophage NRP1 24h vs. NRP1 48h': [nrp1_24_mo, nrp1_48_mo],
    'Macrophage NRP2 24h vs. NRP2 48h': [nrp2_24_mo, nrp2_48_mo],

    'Macrophage NRP1 24h vs. NRP2 24h': [nrp1_24_mo, nrp2_24_mo],
    'Macrophage NRP1 48h vs. NRP2 48h': [nrp1_48_mo, nrp2_48_mo],
}



# lavado 0
ctrl_4h_macrophage = {'path': 'data/log_ctrl_lavado0/norm/ctrl_4h_macrophage.tsv',
                      'title': 'Ctrl 4h'}
ctrl_24h_macrophage = {'path': 'data/log_ctrl_lavado0/norm/ctrl_24h_macrophage.tsv',
                       'title': 'Ctrl 24h'}
ctrl_48h_macrophage = {'path': 'data/log_ctrl_lavado0/norm/ctrl_48h_macrophage.tsv',
                       'title': 'Ctrl 48h'}
log_24h_macrophage = {'path': 'data/log_ctrl_lavado0/norm/log_24h_macrophage.tsv',
                      'title': 'Log 24h'}
log_48h_macrophage = {'path': 'data/log_ctrl_lavado0/norm/log_48h_macrophage.tsv',
                      'title': 'Log 48h'}

log_macrophage_l0 = {
    'Macrophage Log 24h vs. 48h': [log_24h_macrophage, log_48h_macrophage],
    'Macrophage Log 24h vs. Ctrl 24h': [log_24h_macrophage, ctrl_24h_macrophage],
    'Macrophage Log 48h vs. Ctrl 48h': [log_48h_macrophage, ctrl_48h_macrophage],
    'Macrophage Ctrl 4h vs. 24h': [ctrl_4h_macrophage, ctrl_24h_macrophage],
    'Macrophage Ctrl 24h vs. 48h': [ctrl_24h_macrophage, ctrl_48h_macrophage],
}



ctrl_4h_tb = {'path': 'data/log_ctrl_lavado0/norm/ctrl_4h_tb.tsv',
              'title': 'Ctrl 4h'}
ctrl_24h_tb = {'path': 'data/log_ctrl_lavado0/norm/ctrl_24h_tb.tsv',
               'title': 'Ctrl 24h'}
ctrl_48h_tb = {'path': 'data/log_ctrl_lavado0/norm/ctrl_48h_tb.tsv',
               'title': 'Ctrl 48h'}
log_24h_tb = {'path': 'data/log_ctrl_lavado0/norm/log_24h_tb.tsv',
              'title': 'Log 24h'}
log_48h_tb = {'path': 'data/log_ctrl_lavado0/norm/log_48h_tb.tsv',
              'title': 'Log 48h'}
log_tb_l0 = {
    'TB Log 24h vs. 48h': [log_24h_tb, log_48h_tb],
    'TB Log 24h vs. Ctrl 24h': [log_24h_tb, ctrl_24h_tb],
    'TB Log 48h vs. Ctrl 48h': [log_48h_tb, ctrl_48h_tb],
    'TB Ctrl 4h vs. 24h': [ctrl_4h_tb, ctrl_24h_tb],
    'TB Ctrl 24h vs. 48h': [ctrl_24h_tb, ctrl_48h_tb],
}



# lavado 1
ctrl_4h_macrophage = {'path': 'data/log_ctrl_lavado1/norm/ctrl_4h_macrophage.tsv',
                      'title': 'Ctrl 4h'}
ctrl_24h_macrophage = {'path': 'data/log_ctrl_lavado1/norm/ctrl_24h_macrophage.tsv',
                       'title': 'Ctrl 24h'}
ctrl_48h_macrophage = {'path': 'data/log_ctrl_lavado1/norm/ctrl_48h_macrophage.tsv',
                       'title': 'Ctrl 48h'}
log_24h_macrophage = {'path': 'data/log_ctrl_lavado1/norm/log_24h_macrophage.tsv',
                      'title': 'Log 24h'}
log_48h_macrophage = {'path': 'data/log_ctrl_lavado1/norm/log_48h_macrophage.tsv',
                      'title': 'Log 48h'}

log_macrophage_l1 = {
    'Macrophage Log 24h vs. 48h': [log_24h_macrophage, log_48h_macrophage],
    'Macrophage Log 24h vs. Ctrl 24h': [log_24h_macrophage, ctrl_24h_macrophage],
    'Macrophage Log 48h vs. Ctrl 48h': [log_48h_macrophage, ctrl_48h_macrophage],
    'Macrophage Ctrl 4h vs. 24h': [ctrl_4h_macrophage, ctrl_24h_macrophage],
    'Macrophage Ctrl 24h vs. 48h': [ctrl_24h_macrophage, ctrl_48h_macrophage],
}



ctrl_4h_tb = {'path': 'data/log_ctrl_lavado1/norm/ctrl_4h_tb.tsv',
              'title': 'Ctrl 4h'}
ctrl_24h_tb = {'path': 'data/log_ctrl_lavado1/norm/ctrl_24h_tb.tsv',
               'title': 'Ctrl 24h'}
ctrl_48h_tb = {'path': 'data/log_ctrl_lavado1/norm/ctrl_48h_tb.tsv',
               'title': 'Ctrl 48h'}
log_24h_tb = {'path': 'data/log_ctrl_lavado1/norm/log_24h_tb.tsv',
              'title': 'Log 24h'}
log_48h_tb = {'path': 'data/log_ctrl_lavado1/norm/log_48h_tb.tsv',
              'title': 'Log 48h'}
log_tb_l1 = {
    'TB Log 24h vs. 48h': [log_24h_tb, log_48h_tb],
    'TB Log 24h vs. Ctrl 24h': [log_24h_tb, ctrl_24h_tb],
    'TB Log 48h vs. Ctrl 48h': [log_48h_tb, ctrl_48h_tb],
    'TB Ctrl 4h vs. 24h': [ctrl_4h_tb, ctrl_24h_tb],
    'TB Ctrl 24h vs. 48h': [ctrl_24h_tb, ctrl_48h_tb],
}




# lavado 2
ctrl_4h_macrophage = {'path': 'data/log_ctrl_lavado2/norm/ctrl_4h_macrophage.tsv',
                      'title': 'Ctrl 4h'}
ctrl_24h_macrophage = {'path': 'data/log_ctrl_lavado2/norm/ctrl_24h_macrophage.tsv',
                       'title': 'Ctrl 24h'}
ctrl_48h_macrophage = {'path': 'data/log_ctrl_lavado2/norm/ctrl_48h_macrophage.tsv',
                       'title': 'Ctrl 48h'}
log_24h_macrophage = {'path': 'data/log_ctrl_lavado2/norm/log_24h_macrophage.tsv',
                      'title': 'Log 24h'}
log_48h_macrophage = {'path': 'data/log_ctrl_lavado2/norm/log_48h_macrophage.tsv',
                      'title': 'Log 48h'}

log_macrophage_l2 = {
    'Macrophage Log 24h vs. 48h': [log_24h_macrophage, log_48h_macrophage],
    'Macrophage Log 24h vs. Ctrl 24h': [log_24h_macrophage, ctrl_24h_macrophage],
    'Macrophage Log 48h vs. Ctrl 48h': [log_48h_macrophage, ctrl_48h_macrophage],
    'Macrophage Ctrl 4h vs. 24h': [ctrl_4h_macrophage, ctrl_24h_macrophage],
    'Macrophage Ctrl 24h vs. 48h': [ctrl_24h_macrophage, ctrl_48h_macrophage],
}



ctrl_4h_tb = {'path': 'data/log_ctrl_lavado2/norm/ctrl_4h_tb.tsv',
              'title': 'Ctrl 4h'}
ctrl_24h_tb = {'path': 'data/log_ctrl_lavado2/norm/ctrl_24h_tb.tsv',
               'title': 'Ctrl 24h'}
ctrl_48h_tb = {'path': 'data/log_ctrl_lavado2/norm/ctrl_48h_tb.tsv',
               'title': 'Ctrl 48h'}
log_24h_tb = {'path': 'data/log_ctrl_lavado2/norm/log_24h_tb.tsv',
              'title': 'Log 24h'}
log_48h_tb = {'path': 'data/log_ctrl_lavado2/norm/log_48h_tb.tsv',
              'title': 'Log 48h'}
log_tb_l2 = {
    'TB Log 24h vs. 48h': [log_24h_tb, log_48h_tb],
    'TB Log 24h vs. Ctrl 24h': [log_24h_tb, ctrl_24h_tb],
    'TB Log 48h vs. Ctrl 48h': [log_48h_tb, ctrl_48h_tb],
    'TB Ctrl 4h vs. 24h': [ctrl_4h_tb, ctrl_24h_tb],
    'TB Ctrl 24h vs. 48h': [ctrl_24h_tb, ctrl_48h_tb],
}





# pending inter-array normalization
#    'NPR1 24h vs. LOG 24h': [],
#    'NPR1 48h vs. LOG 48h': [],
