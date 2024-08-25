import streamlit as st
import plotly.express as px
import pandas as pd

def plot_visualizations(df, device_option):
    if df.empty:
        st.warning("No data to visualize. Please select specific data and ensure the time range is correct.")
        return

    # Visualize section
    st.write('### Data Visualization')
    df = df.sort_values('timestamp')
    fig = px.line(df, x='timestamp', y='value', color='name', title=f'{device_option} Data Visualization')
    st.plotly_chart(fig)

    # Frequency Bar Chart
    st.write('### Frequency Visualization')
    frequency_data = df['name'].value_counts().reset_index()
    frequency_data.columns = ['name', 'count']
    fig_freq = px.bar(frequency_data, x='name', y='count', title='Frequency of Specific Names', color='name', labels={'count': 'Frequency'})
    st.plotly_chart(fig_freq)          

    # Box Plot for Values
    st.write('### Box Plot Visualization for Values')
    fig_box = px.box(df, x='name', y='value', title=f'{device_option} Box Plot Visualization for Values')
    st.plotly_chart(fig_box)

    # Calculate Time Differences for Each Sensor in Minutes
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values(['name', 'timestamp'])  # Sort by name and then timestamp

    # Calculate time differences for each submission in minutes
    df['time_diff'] = df.groupby(['name'])['timestamp'].transform(lambda x: x.diff().dt.total_seconds() / 60)

    # Take the absolute value
    df['time_diff'] = df['time_diff'].abs()

    # Drop the NaN value
    df = df.dropna(subset=['time_diff'])

    # Box Plot for Time Differences in Minutes
    st.write('### Time Interval Box Plot Visualization for Each Sensor')
    fig_time_diff = px.box(df, x='name', y='time_diff', title='Time Interval Between Submissions for Each Sensor (in Minutes)', labels={'time_diff': 'Time Interval (Minutes)'})
    st.plotly_chart(fig_time_diff)
