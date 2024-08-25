import streamlit as st
import pandas as pd

def display_dataframe(df, device_option, selected_names, data_units, height=400):
    if not selected_names:
        st.warning("Please select specific data to display.")
        return

    # Filter by selected names
    df = df[df['name'].isin(selected_names)]

    # Round the values to 2 decimal places
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    df['value'] = df['value'].round(2)

    # Add units to the data names
    df['name'] = df['name'].apply(lambda x: f"{x} ({data_units[x]})" if x in data_units else x)

    # Rename columns for better readability
    df.rename(columns={
        'timestamp': 'Timestamp',
        'name': 'Sensor Data',
        'value': 'Value',
        'meta.vsn': 'Node'
    }, inplace=True)

    # Display data as a dataframe along with the device name and count in the header
    entry_count = len(df.index)
    st.subheader(f"{device_option} Data - {entry_count} Entries")
    if 'Node' in df.columns:
        displayed_df = df[['Timestamp', 'Sensor Data', 'Value', 'Node']]
        st.dataframe(displayed_df, height=height)
    else:
        displayed_df = df[['Timestamp', 'Sensor Data', 'Value']]
        st.dataframe(displayed_df, height=height)

    # Export as CSV
    csv = displayed_df.to_csv(index=False).encode('utf-8')
    filename = f"data_{device_option.replace(' ', '_')}_{st.session_state.start_date.strftime('%Y%m%d')}_{st.session_state.end_date.strftime('%Y%m%d')}.csv"
    st.download_button(
        label="Export as CSV",
        data=csv,
        file_name=filename,
        mime='text/csv',
    )
