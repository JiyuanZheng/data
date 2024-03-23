import pandas as pd

birth_rate_df = pd.read_csv("birth.csv")
pm25_df = pd.read_csv("pm25-air-pollution.csv")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


# Preprocess data: Merge datasets on 'Entity' and 'Year' columns
merged_df = pd.merge(pm25_df, birth_rate_df, how='inner', on=['Entity', 'Year'])

# Streamlit UI
st.title('Global Birth Rate and PM2.5 Visualization')

# Select country
country_options = merged_df['Entity'].unique()
country = st.selectbox('Select a country', options=country_options)

# Filter data for the selected country
country_data = merged_df[merged_df['Entity'] == country]

# Plot
st.subheader(f'Trends for {country}')
fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
line1, = ax1.plot(country_data['Year'], country_data['PM2.5 air pollution, mean annual exposure (micrograms per cubic meter)'], color='#377eb8', linestyle='-', linewidth=2, label='PM2.5')
line2, = ax2.plot(country_data['Year'], country_data['Birth rate - Sex: all - Age: all - Variant: estimates'], color='#4daf4a', linestyle='--', linewidth=2, label='Birth Rate (per 1,000)')

ax1.set_xlabel('Years')
ax1.set_ylabel('PM2.5 (micrograms per cubic meter)', color='#377eb8')
ax2.set_ylabel('Birth Rate (per 1,000 people)', color='#4daf4a')

# Adjust x-axis to show label every 5 years
ax1.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(1))
plt.xticks(rotation=45)

# Adding a legend
lines = [line1, line2]
labels = [line.get_label() for line in lines]
fig.legend(lines, labels, loc='upper center', ncol=2)

# Beautifying the plot
ax1.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray', alpha=0.5)
ax1.tick_params(axis='y', colors='#377eb8')
ax2.tick_params(axis='y', colors='#4daf4a')
fig.tight_layout()

st.pyplot(fig)
