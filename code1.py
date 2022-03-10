import csv
import plotly.figure_factory as pf
import plotly.graph_objects as ap
import pandas as pd
import statistics as st

df = pd.read_csv("StudentsPerformance.csv")
math_list=df["math score"].to_list()
reading_list=df["reading score"].to_list()
writing_list=df["writing score"].to_list()

math_mean= st.mean(math_list)
reading_mean= st.mean(reading_list)
writing_mean= st.mean(writing_list)

math_mode= st.mode(math_list)
reading_mode= st.mode(reading_list)
writing_mode= st.mode(writing_list)

math_median= st.median(math_list)
reading_median= st.median(reading_list)
writing_median= st.median(writing_list)

print("mean,median,mode of math is {},{},{} respectively".format(math_mean,math_median,math_mode))
print("mean,median,mode of reading is {},{},{} respectively".format(reading_mean,reading_median,reading_mode))
print("mean,median,mode of writing is {},{},{} respectively".format(writing_mean,writing_median,writing_mode))

math_std_deviation=st.stdev(math_list)
reading_std_deviation=st.stdev(reading_list)
writing_std_deviation=st.stdev(writing_list)

math_first_std_deviation_start,math_first_std_deviation_end=math_mean-math_std_deviation,math_mean+math_std_deviation
math_second_std_deviation_start,math_second_std_deviation_end=math_mean-(2*math_std_deviation),math_mean+(2*math_std_deviation)
math_third_std_deviation_start,math_third_std_deviation_end=math_mean-(3*math_std_deviation),math_mean+(3*math_std_deviation)

reading_first_std_deviation_start,reading_first_std_deviation_end=reading_mean-reading_std_deviation,reading_mean+reading_std_deviation
reading_second_std_deviation_start,reading_second_std_deviation_end=reading_mean-(2*reading_std_deviation),reading_mean+(2*reading_std_deviation)
reading_third_std_deviation_start,reading_third_std_deviation_end=reading_mean-(3*reading_std_deviation),reading_mean+(3*reading_std_deviation)

writing_first_std_deviation_start,writing_first_std_deviation_end=writing_mean-writing_std_deviation,writing_mean+writing_std_deviation
writing_second_std_deviation_start,writing_second_std_deviation_end=writing_mean-(2*writing_std_deviation),writing_mean+(2*writing_std_deviation)
writing_third_std_deviation_start,writing_third_std_deviation_end=writing_mean-(3*writing_std_deviation),writing_mean+(3*writing_std_deviation)

list_of_data_within_1_std_deviation=[result for result in math_list if result>math_first_std_deviation_start and result<math_first_std_deviation_end]
list_of_data_within_2_std_deviation=[result for result in math_list if result>math_second_std_deviation_start and result<math_second_std_deviation_end]
list_of_data_within_3_std_deviation=[result for result in math_list if result>math_third_std_deviation_start and result<math_third_std_deviation_end]

print("{}% of data lies within 1 std_deviation of math".format(len(list_of_data_within_1_std_deviation)*100/len(math_list)))
print("{}% of data lies within 2 std_deviation of math".format(len(list_of_data_within_2_std_deviation)*100/len(math_list)))
print("{}% of data lies within 3 std_deviation of math".format(len(list_of_data_within_3_std_deviation)*100/len(math_list)))

list_of_data_within_1_std_deviation=[result for result in reading_list if result>reading_first_std_deviation_start and result<reading_first_std_deviation_end]
list_of_data_within_2_std_deviation=[result for result in reading_list if result>reading_second_std_deviation_start and result<reading_second_std_deviation_end]
list_of_data_within_3_std_deviation=[result for result in reading_list if result>reading_third_std_deviation_start and result<reading_third_std_deviation_end]

print("{}% of data lies within 1 std_deviation of reading".format(len(list_of_data_within_1_std_deviation)*100/len(reading_list)))
print("{}% of data lies within 2 std_deviation of reading".format(len(list_of_data_within_2_std_deviation)*100/len(reading_list)))
print("{}% of data lies within 3 std_deviation of reading".format(len(list_of_data_within_3_std_deviation)*100/len(reading_list)))

list_of_data_within_1_std_deviation=[result for result in writing_list if result>writing_first_std_deviation_start and result<writing_first_std_deviation_end]
list_of_data_within_2_std_deviation=[result for result in writing_list if result>writing_second_std_deviation_start and result<writing_second_std_deviation_end]
list_of_data_within_3_std_deviation=[result for result in writing_list if result>writing_third_std_deviation_start and result<writing_third_std_deviation_end]

print("{}% of data lies within 1 std_deviation of writing".format(len(list_of_data_within_1_std_deviation)*100/len(writing_list)))
print("{}% of data lies within 2 std_deviation of writing".format(len(list_of_data_within_2_std_deviation)*100/len(writing_list)))
print("{}% of data lies within 3 std_deviation of writing".format(len(list_of_data_within_3_std_deviation)*100/len(writing_list)))


fig = pf.create_distplot([df["math score"].tolist()],["math"],show_hist=False)
fig.add_trace(ap.Scatter(x = [math_mean,math_mean], y = [0,0.17],mode="lines",name="mean")) 
fig.add_trace(ap.Scatter(x = [math_first_std_deviation_start,math_first_std_deviation_start], y = [0,0.17],mode="lines",name="math_std_deviation1 start"))
fig.add_trace(ap.Scatter(x = [math_first_std_deviation_end,math_first_std_deviation_end], y = [0,0.17],mode="lines",name="math_std_deviation1 end"))
fig.add_trace(ap.Scatter(x = [math_second_std_deviation_start,math_second_std_deviation_start], y = [0,0.17],mode="lines",name="math_std_deviation2 start"))
fig.add_trace(ap.Scatter(x = [math_second_std_deviation_end,math_second_std_deviation_end], y = [0,0.17],mode="lines",name="math_deviation2 end"))
fig.show()
