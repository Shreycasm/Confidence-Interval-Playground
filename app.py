import numpy as np
import streamlit as st
import scipy.stats as stats
import matplotlib.pyplot as plt



st.set_page_config(page_title="Confidence Interval Playground", layout="wide")
st.title("Confidence Interval Playground")

col1 , col2 = st.columns([0.2,0.8])
container1 = col1.container(border=True)
with container1:
    sample_size = st.number_input("Enter Sample Size (2-100)",min_value=2, max_value = 200, value=50)
    population_mean = st.number_input("Enter Population Mean",min_value=2, max_value = 1000, value=100)
    population_std  =st.number_input("Enter Population Standard Deviation (greater than 0)",min_value=1, max_value = 1000, value=25)
    iterations = st.number_input("Enter Number of Iterations",min_value=1, max_value = 1000, value=100)
    confidence_level = st.number_input("Enter Confidence Interval value (0-100)",min_value=0, max_value = 100, value=95)
    method = st.selectbox("choose method",["Z using σ"," Z using s"])

lower_interval = []
upper_interval = []
passing_thorugh_mean = 0
for i in range(int(iterations)):
    sample = np.random.normal(loc = (population_mean), scale = (population_std) , size = (sample_size))

    sample_mean = np.mean(sample)
    sample_std_dev = np.std(sample)

    critical_value = stats.norm.ppf((1 + confidence_level / 100) / 2)
    margin_of_error = critical_value * (population_std / np.sqrt(sample_size))

    lower_interval.append(sample_mean - margin_of_error)
    upper_interval.append(sample_mean + margin_of_error)

    if lower_interval[i] <= population_mean <= upper_interval[i]:
        passing_thorugh_mean += 1

percent_of_lines_passing = (passing_thorugh_mean / iterations) * 100

fig , ax = plt.subplots(figsize=(25,10.9))


container2 = col2.container(border=True)
with container2:
 
        for i in range(int(iterations)):
            color = "green" if lower_interval[i] <= population_mean <= upper_interval[i] else "red"
            plt.plot([i, i], [lower_interval[i], upper_interval[i]], color=color)


            plt.scatter(i, lower_interval[i], marker="_", color=color)
            plt.scatter(i, upper_interval[i], marker="_", color=color)

            plt.scatter(i, lower_interval[i], marker="_", color=color)
            plt.scatter(i, lower_interval[i], marker="_", color=color)

        plt.hlines(population_mean, 0-2, iterations+2, colors="black", label=f"Population Mean({population_mean})",linestyles="dashdot")


        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        for spine in ax.spines.values():
            spine.set_edgecolor('white')
        plt.legend(fontsize = "xx-large")
        st.pyplot(fig)
        st.write(f"Around {percent_of_lines_passing}% of times the Population mean falls in the Confidence interval of Sample mean")


