import sage_data_client
import pandas as pd
from config import CROCUS_NODES

def fetch_data(start, end, node, device, selected_names):
    # Get the available device types for the node
    devices = CROCUS_NODES[node]
    device_info = devices[device]
    plugin = device_info['plugin']
    vsn = node.split('(')[-1][:-1]

    if device == 'MFR Nodes':
        selected_sensor = st.session_state.get('selected_sensor', None)
        if selected_sensor:
            measurements = device_info['sensors'][selected_sensor]
            filtered_names = [name for name in selected_names if name in measurements]
        else:
            filtered_names = selected_names

        query_filter = {
            "plugin": plugin,
            "vsn": vsn,
            "name": "|".join(filtered_names)
        }

        # Fetch data using sage_data_client
        df_data = sage_data_client.query(
            start=start,
            end=end,
            filter=query_filter
        )
        df = pd.DataFrame(df_data)
        return df

    else:
        # For other devices
        filtered_names = selected_names
        query_filter = {
            "plugin": plugin,
            "vsn": vsn,
            "name": "|".join(filtered_names)
        }

        # Fetch data using sage_data_client
        df_data = sage_data_client.query(
            start=start,
            end=end,
            filter=query_filter
        )
        df = pd.DataFrame(df_data)
        return df

def filter_data_by_serial(df, serial):
    # Create an empty DataFrame to hold filtered results
    filtered_df = pd.DataFrame()

    # List of possible metadata keys for serial numbers
    serial_keys = [
        'meta.Serial Number_tag',
        'meta.serial_number_tag'
    ]

    # Iterate over possible keys to filter data
    for key in serial_keys:
        if key in df.columns:
            filtered_df = pd.concat([filtered_df, df[df[key] == serial]])

    if filtered_df.empty and not df.empty:
        st.warning(f"No data found matching the serial number {serial}.")
        st.write("Available serial numbers in data:")
        available_serials = set()
        for key in serial_keys:
            if key in df.columns:
                available_serials.update(df[key].unique())
        st.write(available_serials)

    return filtered_df
