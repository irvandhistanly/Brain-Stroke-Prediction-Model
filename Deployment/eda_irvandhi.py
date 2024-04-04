# import libraries
import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

def run():
    # Set title and page configuration
    st.title('BRAIN STROKE DATASET VISUALIZATION')

    # Load data
    data = pd.read_csv('P1M2_Irvandhi_stanly_dataset.csv')

    # Display dataframe
    st.markdown('## Dataframe')
    st.write(data)

    # Display EDA
    st.markdown('## Exploratory Data Analysis (EDA)')

    # Pie Chart for Brain Stroke Patients Distribution
    st.markdown('### Brain Stroke Patients Distribution')
    st.write('''The pie chart below suggests that the majority of people that participated in the sampling ended up being healthy, while only 5% of the people actually had a brain stroke. We can observe the imbalance within our data in which the percentage of people that didn’t have a stroke is way bigger than the one that got a brain stroke.''')    
    stroke_colors = ['#FF69B4', '#FFB3DE']
    stroke_count = data['stroke'].value_counts()
    labels = ['Non stroke', 'Stroke']
    fig, ax = plt.subplots()
    ax.pie(stroke_count, labels=labels, autopct='%1.1f%%', colors=stroke_colors)
    ax.axis('equal')  
    st.pyplot(fig)

    # Histogram and BoxPlot of age
    st.markdown('### Age Distribution And Box Plot')
    st.write('''It can be seen from the visualization below that the distribution of the age column is normal. It generally has the same amount of low and high value data, indicating a non-skewed distribution. We can conclude that our data is mostly comprised of people with varying ages, with a slight peak at the ages of 50 and 80. We can also observe the box plot and see that there are no outliers present within this column as it has a normal distribution.''')   
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    sns.histplot(data['age'], bins=30, color='#FF69B4', ax=axes[0])
    axes[0].set_title('Age Histogram')
    sns.boxplot(y=data['age'], color='#FF69B4', ax=axes[1])
    axes[1].set_title('Age Boxplot')
    fig.tight_layout()
    st.pyplot(fig)

    # Histogram and BoxPlot of avg_glucose_level
    st.markdown('### Average Glucose Level Distribution And Box Plot')
    st.write('''In contrast to the age column, it can be seen from the visualization below that the distribution of the average glucose level column is not normal. It has more low-value data compared to high ones, indicating a positively skewed distribution. Moreover, the very low number of extremely high values are present, indicating potential outliers within the data.''')
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    sns.histplot(data['avg_glucose_level'], bins=30, color='#FF69B4', ax=axes[0])
    axes[0].set_title('Average Glucose Level Histogram')
    sns.boxplot(y=data['avg_glucose_level'], color='#FF69B4', ax=axes[1])
    axes[1].set_title('Average Glucose Level Boxplot')
    fig.tight_layout()
    st.pyplot(fig)

    # Plotting Whether or Not Someone Will Have a Brain Stroke Based On Categorical Features
    st.markdown('### Plotting Whether or Not Someone Will Have a Brain Stroke Based On Categorical Features')
    st.write('''Although the number of people with a stroke is smaller among the people with hypertension and heart disease, we can see that the number of people that did not get a stroke in the hypertension and heart disease class is also small. Indicating people with hypertension and heart disease are more likely to get a stroke.
    As for the marital status, work type, and smoking status, the pattern is more apparent with people that have been married, working in a private sector, and regular smokers tend to have strokes. As for the living area, there are no differences between rural and urban areas. However, we need to conduct further analysis to determine which features will be included in our model in the feature selection section.''')
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    categorical_columns = ['gender', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
    for i, ax in zip(categorical_columns[1:], axes.flatten()):
        sns.countplot(x=i ,hue='stroke', data=data, palette='RdPu', ax=ax)
        ax.set_xlabel(i, fontsize=14)
    fig.tight_layout()
    st.pyplot(fig)

    # Plotting Age vs Average Glucose Level
    st.markdown('### Plotting Age vs Average Glucose Level')
    st.write('''The graph below demonstrates that generally, when someone is older than 50 years old, they are more prone to having a brain stroke. A high average blood glucose level also showed to correlate with more stroke cases, even though there are people with normal blood sugar who ended up having a stroke. This finding is aligned with the basic knowledge that older people are more prone to stroke, however, the importance of blood glucose level needs to be analyzed further in feature selection.''')
    plt.figure(figsize=(15, 6))
    for stroke in data['stroke'].unique():
        subset = data[data['stroke'] == stroke]
        plt.scatter(subset['age'], subset['avg_glucose_level'], color='hotpink' if stroke == 1 else 'black', label=stroke)
    plt.title('Scatterplot Age vs Average Glucose Level')
    plt.xlabel('Age')
    plt.ylabel('Average Glucose Level')
    plt.legend()
    plt.grid(True)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

    # Plotting Age vs BMI
    st.markdown('### Plotting Age vs BMI')
    st.write('''The graph below demonstrates that generally, when someone is older than 50 years old, they are more prone to having a brain stroke. A high average blood glucose level also showed to correlate with more stroke cases, even though there are people with normal blood sugar who ended up having a stroke. This finding is aligned with the basic knowledge that older people are more prone to stroke, however, the importance of blood glucose level needs to be analyzed further in feature selection.''')
    plt.figure(figsize=(15, 6))
    for stroke in data['stroke'].unique():
        subset = data[data['stroke'] == stroke]
        plt.scatter(subset['age'], subset['bmi'], color='hotpink' if stroke == 1 else 'black', label=stroke)
    plt.title('Scatterplot Age vs BMI')
    plt.xlabel('Age')
    plt.ylabel('BMI')
    plt.legend()
    plt.grid(True)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

if __name__ == "__main__":
    run()
