import streamlit as st
import pandas as pd

def display_dataframe(df, device_option, selected_names, data_units, height=400):
    if not selected_names:
        st.warning("Please select specific data to display.")
        return

    # Check if dataframe is empty
    if df.empty:
        st.warning("No data available for the selected time range. Please adjust your selection or the sensors may be offline.")
        return

    # Filter by selected names
    df = df[df['name'].isin(selected_names)]

    # Check if filtered dataframe is empty
    if df.empty:
        st.warning("No data found for the selected sensors. Please try a different time range or check sensor availability.")
        return

    # Round the values to 4 decimal places
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    df['value'] = df['value'].round(4)

    # Add units to the data names and handle empty units
    df['name'] = df['name'].apply(lambda x: f"{x} ({data_units.get(x, '')})" if data_units.get(x, '') else x)

    # Format the Timestamp column to remove the timezone information
    df['timestamp'] = df['timestamp'].apply(lambda x: str(x).split('.')[0])

    # Rename columns for better readability
    df.rename(columns={
        'timestamp': 'Timestamp',
        'name': 'Sensor Data',
        'value': 'Value',
        'meta.vsn': 'Node'
    }, inplace=True)

    # Create a container for the checkboxes and notes
    checkbox_container = st.sidebar.container()
    
    with checkbox_container:
        # Checkbox to view all metadata
        view_metadata = st.checkbox('View All Metadata')
        
        # Checkbox to display sensors as columns
        sensors_as_columns = st.checkbox('Display Sensors as Columns')
        
        # Show notes about mutual exclusivity
        if view_metadata and sensors_as_columns:
            st.caption("⚠️ **'View All Metadata'** and **'Display Sensors as Columns'** cannot be used simultaneously. Please uncheck one option.")

    if sensors_as_columns:
        try:
            # Pivot the table to have sensors as columns
            displayed_df = df.pivot_table(index='Timestamp', columns='Sensor Data', values='Value').reset_index()
        except Exception as e:
            st.error("Error creating columnar view. Please check your data selection.")
            displayed_df = df
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

    # Only show export button if there's data to export
    if not displayed_df.empty:
        # Export as CSV
        csv = displayed_df.to_csv(index=False).encode('utf-8')
        filename = f"data_{device_option.replace(' ', '_')}_{st.session_state.start_date.strftime('%Y%m%d')}_{st.session_state.end_date.strftime('%Y%m%d')}.csv"
        st.download_button(
            label="Export as CSV",
            data=csv,
            file_name=filename,
            mime='text/csv',
        )