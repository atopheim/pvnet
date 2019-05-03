
import matplotlib.pyplot as plt
import csv

x_train = []
y_train = []

x_val = []
y_val = []

x_occ = []
y_occ = []

with open('/home/volvomlp2/python-envs/pvnet/data/record/cat_linemod_train.log','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=' ')
    for idx, row in enumerate(plots):
        if idx%3 == 0:
            x_train.append(int(row[2])) # num epoch
            y_train.append(float(row[15])) # metric
        elif idx%3 ==1:
            x_val.append(int(row[2]))
            y_val.append(float(row[15]))
        elif idx%3 ==2:
            x_occ.append(int(row[2]))
            y_occ.append(float(row[15]))
        else:
            print("Went to else")
        
# 6 - segmentation , 9 - verifiaction, 12 - precision, 15 - recall 

plt.plot(x_train,y_train, 'r',label='Training metrics')
plt.plot(x_val,y_val, 'b', label='Validation metrics')
plt.plot(x_occ,y_occ, 'g', label='Occlusion metrics')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.title('X-Graph\ncat')
plt.legend()
plt.show()

