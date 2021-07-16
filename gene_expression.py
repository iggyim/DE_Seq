import pandas as pd
dat=pd.read_csv("file.csv")

filt_dat = dat[dat["fiBat1"]!=0]
filt_dat_1 = filt_dat[filt_dat["fiBat2"]!=0]
filt_dat_2 = filt_dat_1[filt_dat_1["fiBat3"]!=0]
filt_dat_3 = filt_dat_2[filt_dat_2["fiBat4"]!=0]
filt_dat_4 = filt_dat_3[filt_dat_3["Ome1"]!=0]
filt_dat_5 = filt_dat_4[filt_dat_4["Ome2"]!=0]
filt_dat_6 = filt_dat_5[filt_dat_5["Ome3"]!=0]
filt_dat_7 = filt_dat_6[filt_dat_6["Sub1"]!=0]
filt_dat_8 = filt_dat_7[filt_dat_7["Sub2"]!=0]
filt_dat_9 = filt_dat_8[filt_dat_8["Sub3"]!=0]

len(filt_dat_9)

filt_dat_9.to_csv('new.csv')
