import random
import statistics
import plotly.figure_factory as ff
dice_result = []
count = []
for i in range(0,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1+dice2)
    count.append(i)
mean = sum(dice_result)/len(dice_result)
std_deviation = statistics.stdev(dice_result)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)
print(mean)
print(std_deviation)
print(median)
print(mode)
fig = ff.create_distplot([dice_result],["result"],show_hist = False)
#fig.show()
first_std_deviation_start,first_std_deviation_end = mean-std_deviation,mean+std_deviation
second_std_deviation_start,second_std_deviation_end = mean-(2*std_deviation),mean+(2*std_deviation)
print("{}% of data lies within 1 standard deviation ".format(len(list_of_data_within_1_std_deviation)*100.0/len(dice_result)))

