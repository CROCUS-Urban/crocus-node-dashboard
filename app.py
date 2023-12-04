import streamlit as st
import pandas as pd
import sage_data_client
import plotly.express as px
import datetime
import base64
import time

# Set the page title & icon
st.set_page_config(
    page_title="CROCUS Node Dashboard",
    page_icon="📊",
)

# Removes streamlit hyperlink at the bottom of the page
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Metric Measurement Dictionary
METRIC_MEASUREMENT = {
    'soil_moisture': "",
    'solar_voltage': "V",
    'frequency': "ns/pulse",
    'voltage_adc': "uV",
    'target_temperature': "C",
    'sensor_body_temperature': "C",
    'soil_permitivity': "%",
    'soil_temperature': "C",
    'par': "umol/m2/s",
    'heat_flux': "w/m2",
    'signal.rssi': "",
    'signal.snr': "",
    'signal.spreadingfactor': "",
    'battery_voltage': "V",
    'external_power_supply_voltage': "V",
    'uncorrected_outer': "cm/hr",
    'uncorrected_inner': "cm/hr",
    'corrected_outer': "cm/hr",
    'corrected_inner': "cm/hr",
    'vs_factor': "",
    'outer_area': "cm^2",
    'inner_area': "cm^2"
}

# Include the 3 devices on the Waggle Node, along with each of the data available within those devices.
DEVICE_SPECIFIC_NAMES = {
    'MFR Node': [
        "battery_voltage", "signal.rssi", "sensor_body_temperature", "voltage_adc",
        "par", "heat_flux", "frequency", "target_temperature", "solar_voltage",
        "external_power_supply_voltage", "soil_temperature", "soil_permitivity",
        "soil_moisture", "signal.spreadingfactor", "signal.snr"
    ],
    'SFM1x Sap Flow': [
        "uncorrected_outer", "uncorrected_inner", "corrected_outer", "corrected_inner",
        "vs_factor", "outer_area", "inner_area", "signal.rssi", "signal.snr",
        "signal.spreadingfactor", "battery_voltage", "external_power_supply_voltage"
    ],
    'Waggle Node': [
        "env.pressure", "env.relative_humidity", "env.temperature",
        "iio.in_humidityrelative_input", "iio.in_pressure_input",
        "iio.in_resistance_input", "iio.in_temp_input"
    ]
}

def fetch_data(start, end, device_name, selected_names):
    if device_name == 'MFR Node':
        plugin = "registry.sagecontinuum.org/flozano/lorawan-listener:0.0.7.*"
        filters = {
            "plugin": plugin,
            "deviceName": device_name,
            "vsn": "W039",
            "name": "|".join(selected_names)
        }
    elif device_name == 'SFM1x Sap Flow':
        plugin = "registry.sagecontinuum.org/flozano/lorawan-listener:0.0.7.*"
        filters = {
            "plugin": plugin,
            "deviceName": device_name,
            "vsn": "W039",
            "name": "|".join(selected_names)
        }
    elif device_name == 'Waggle Node':
        plugin = "waggle/plugin-iio:0.7.0.*"
        filters = {
            "plugin": plugin,
            "vsn": "W039",
            "name": "|".join(selected_names)
        }

    df_data = sage_data_client.query(
        start=start,
        end=end, 
        filter=filters
    )
    
    return pd.DataFrame(df_data)

def main():
    # Title
    st.title('CROCUS Node Dashboard 📊')
    # Description under the title
    st.write("This is an interface to visualize and analyze data from various sensors on the W039 Waggle Node which can be viewed [here](https://portal.sagecontinuum.org/node/W039). Select your desired device, specific names, date, and time range to display the results. Additionally, users have the option to view and download all the data as a CSV file and the graphs as a PNG file.")

    # Display the logo at the top of the sidebar
    st.sidebar.image('images/crocus_logo.png', use_column_width=True)

    # Choose device to fetch
    device_option = st.sidebar.selectbox('Select Device', ['MFR Node', 'SFM1x Sap Flow', 'Waggle Node'])

    # Multi-select for names so users can view multiple names and values
    unique_names = DEVICE_SPECIFIC_NAMES[device_option]
    selected_names = st.sidebar.multiselect('Select specific names', unique_names, default=unique_names)

    # Date and Time picker, along with an option for real time, which will keep updating every 60 seconds to show real time results starting from a specific start date & time
    real_time = st.sidebar.toggle("Real-time")

    # Toggle for removing potential outliers
    remove_outliers = st.sidebar.toggle('Remove Potential Outliers')    

    # Quick Conversion Table in Sidebar
    if st.sidebar.toggle("Quick Metrics"):
        st.sidebar.write("### Metrics")
        conversion_df = pd.DataFrame.from_dict(METRIC_MEASUREMENT, orient='index', columns=['Measurement'])
        st.sidebar.table(conversion_df) 
    
    if real_time:
        start_date = st.sidebar.date_input('Select start date', datetime.datetime.now().date())
        start_time = st.sidebar.time_input('Select start time')
        start = f"{start_date}T{start_time.hour}:{start_time.minute}:{start_time.second}Z"
        end = datetime.datetime.now().isoformat()
        end_date = datetime.datetime.now().date()
    else:
        start_date = st.sidebar.date_input('Select start date')
        start_time = st.sidebar.time_input('Select start time')
        start = f"{start_date}T{start_time.hour}:{start_time.minute}:{start_time.second}Z"
        
        end_date = st.sidebar.date_input('Select end date')
        end_time = st.sidebar.time_input('Select end time')
        end = f"{end_date}T{end_time.hour}:{end_time.minute}:{end_time.second}Z"

    # Stop users from choosing the same start and end time & date
    if start == end:
        st.warning('Start and end times cannot be exactly the same.')
        return

    if st.sidebar.button('Submit'):
        # Fetch and display data
        with st.spinner('Fetching data...'):
            df = fetch_data(start, end, device_option, selected_names)

        # Filter by selected names
        df = df[df['name'].isin(selected_names)]

        # Remove potential outliers if toggle is checked with values less than -10k and more than 10k
        if remove_outliers:
            df = df[(df['value'] < 10000) & (df['value'] > -10000)]

        # # Convert 'timestamp' column to datetime dtype and sort
        # df['timestamp'] = pd.to_datetime(df['timestamp'])
        # df = df.sort_values(by='timestamp')

        # Round the values to 2 decimal places to prevent long decimal values
        df['value'] = pd.to_numeric(df['value'], errors='coerce')
        df['value'] = df['value'].round(2)

        # Add metric measurements to the names
        df['name'] = df.apply(lambda row: f"{row['name']} {('(' + METRIC_MEASUREMENT.get(row['name'], '') + ')') if METRIC_MEASUREMENT.get(row['name']) else ''}".strip(), axis=1)

        # Display data as a dataframe along with the device name and entry count in the header
        if not df.empty:
            entry_count = len(df.index)  # Gets the number of entries
            st.subheader(f"{device_option} Data - {entry_count} Entries")
            if 'meta.deviceName' in df.columns:
                st.write(df[['timestamp', 'name', 'value', 'meta.deviceName']])
            else:
                st.write(df[['timestamp', 'name', 'value']])

        # Export as CSV
        if not df.empty:
            csv = df.to_csv(index=False).encode('utf-8')
            filename = f"data_{device_option.replace(' ', '_')}_{start_date.strftime('%Y%m%d')}_{end_date.strftime('%Y%m%d')}.csv"
            st.download_button(
                label="Export as CSV",
                data=csv,
                file_name=filename,
                mime='text/csv',
            )            
        
        # Visualize section
        if not df.empty:
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

            # Heatmap
            st.write('### Heatmap Visualization')
            heatmap_data = df.pivot_table(index='timestamp', columns='name', values='value', aggfunc='mean').reset_index()
            fig_heatmap = px.imshow(heatmap_data.corr(), title=f'{device_option} Heatmap Visualization')
            st.plotly_chart(fig_heatmap)              

        # If real-time is selected, rerun the app after 60 seconds
        if real_time:
            time.sleep(60)
            st.experimental_rerun()

if __name__ == "__main__":
    main()

st.markdown("---")
st.markdown("")
st.markdown("<p style='text-align: center'><a href='https://github.com/Kaludii'>Github</a> | <a href='https://huggingface.co/Kaludi'>HuggingFace</a></p>", unsafe_allow_html=True)