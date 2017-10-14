cd data/nrp1_nrp2/norm
paste ng_nrp1_24h_l1.txt ng_nrp1_24h_l2.txt  | awk '{print $1,($2+$4)/2}' > nrp1_24h.txt
paste ng_nrp1_48h_l1.txt ng_nrp1_48h_l2.txt  | awk '{print $1,($2+$4)/2}' > nrp1_48h.txt

paste ng_nrp2_24h_l1.txt ng_nrp2_24h_l2.txt  | awk '{print $1,($2+$4)/2}' > nrp2_24h.txt
paste ng_nrp2_48h_l1.txt ng_nrp2_48h_l2.txt  | awk '{print $1,($2+$4)/2}' > nrp2_48h.txt
cd ../../../


cd data/log_ctrl_lavado0/norm/
paste ng_log_24h_l1.txt ng_log_24h_l2.txt | awk '{print $1,($2+$4)/2}' > log_24h.txt
paste ng_log_48h_l1.txt ng_log_48h_l2.txt ng_log_48h_l3.txt | awk '{print $1,($2+$4+$6)/3}' > log_48h.txt
cd ../../../


cd data/log_ctrl_lavado1/norm/
paste ng_log_24h_l1.txt ng_log_24h_l2.txt | awk '{print $1,($2+$4)/2}' > log_24h.txt
paste ng_log_48h_l1.txt ng_log_48h_l2.txt ng_log_48h_l3.txt | awk '{print $1,($2+$4+$6)/3}' > log_48h.txt
cd ../../../


cd data/log_ctrl_lavado2/norm/
paste ng_log_24h_l1.txt ng_log_24h_l2.txt | awk '{print $1,($2+$4)/2}' > log_24h.txt
paste ng_log_48h_l1.txt ng_log_48h_l2.txt ng_log_48h_l3.txt | awk '{print $1,($2+$4+$6)/3}' > log_48h.txt
cd ../../../
