import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("Air Crashes Data Analysis Dashboard")
df = pd.read_csv("aircrashesFullDataUpdated_2024.csv")
st.write(df.columns.tolist())
st.subheader("Dataset Preview")
st.dataframe(df.head())
st.subheader("Top 10 Countries With Most Air Crashes")
fig,ax = plt.subplots()
df['Country/Region'].value_counts().head(10).plot(kind='bar', ax=ax)
st.pyplot(fig)
st.subheader("Air Crash Trend Over Time")
fig2, ax2 = plt.subplots()
df['Year'].value_counts().sort_index().plot(kind='line', ax=ax2)
st.pyplot(fig2)
st.subheader("Year with the Highest Number of Air Crashes")
fig3, ax3 = plt.subplots()
df['Year'].value_counts().sort_values(ascending=False).head(10).plot(kind='bar', ax=ax3)
st.pyplot(fig3)
st.subheader("Top Operators Involved in Air Crashes?")
fig4, ax4 = plt.subplots()
df['Operator'].value_counts().head(10).plot(kind='bar', ax=ax4)
st.pyplot(fig4)
st.subheader("Fatalities Over the Years")
fatalities_year = df.groupby('Year')['Fatalities (air)'].sum()
fig5, ax5 = plt.subplots(figsize=(10,5))
fatalities_year.plot(kind='line', ax=ax5)
ax5.set_title('Air Crash Fatalities Over Time')
ax5.set_xlabel('Year')
ax5.set_ylabel('Total Fatalities')
st.pyplot(fig5)
st.subheader("Key Findings")
st.markdown("""
- Some years recorded significantly more air crashes than others.
- Certain operators appear repeatedly in crash records.
- Air crash occurrences show clear historical trends rather than remaining constant.
- Fatalities fluctuate over time and tend to increase during years with more crashes.
- A few countries account for a large proportion of recorded crashes.
""")
st.subheader("Recommendations")
st.markdown("""
1. Strengthen aviation safety regulations.
2. Increase aircraft maintenance inspections.
3. Improve pilot training and certification programs.
4. Invest in modern air traffic monitoring systems.
5. Conduct regular safety audits for high-risk operators.
""")
st.markdown("---")
st.write("Created by Esther Essien")
