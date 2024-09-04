import streamlit as st
import pandas as pd

def display_dataframe(df, device_option, selected_names, data_units, height=400):
    if not selected_names:
        st.warning("Please select specific data to display.")
        return

    # Filter by selected names
    df = df[df['name'].isin(selected_names)]

    # Round the values to 4 decimal places
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    df['value'] = df['value'].round(4)

    # Add units to the data names and handle empty units
    df['name'] = df['name'].apply(lambda x: f"{x} ({data_units.get(x, '')})" if data_units.get(x, '') else x)

    # Rename columns for better readability
    df.rename(columns={
        'timestamp': 'Timestamp',
        'name': 'Sensor Data',
        'value': 'Value',
        'meta.vsn': 'Node'
    }, inplace=True)

    # Checkbox to view all metadata columns
    view_metadata = st.sidebar.checkbox('View All Metadata')

    # Checkbox to display sensors as columns
    sensors_as_columns = st.sidebar.checkbox('Display Sensors as Columns')

    if sensors_as_columns:
        # Pivot the table to have sensors as columns
        displayed_df = df.pivot_table(index='Timestamp', columns='Sensor Data', values='Value').reset_index()
    else:
        # Display full or filtered dataframe based on the checkbox
        if view_metadata:
            displayed_df = df
        else:
            if 'Node' in df.columns:
                displayed_df = df[['Timestamp', 'Sensor Data', 'Value', 'Node']]
            else:
                displayed_df = df[['Timestamp', 'Sensor Data', 'Value']]

    # Display data as a dataframe along with the device name and entry count in the header
    entry_count = len(df.index)
    st.subheader(f"{device_option} Data - {entry_count} Entries")
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
