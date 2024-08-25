import sage_data_client
import pandas as pd

def fetch_data(start, end, node, device, selected_names):
    # Define plugins and the corresponding filters
    plugin_filters = []

    if device == 'Sap Flow Sensors':
        plugin_filters.append({
            "plugin": "registry.sagecontinuum.org/flozano/lorawan-listener:*.*",
            "vsn": node.split('(')[-1][:-1],
            "name": "|".join(selected_names)
        })

    if any(name.startswith("aqt") for name in selected_names):
        plugin_filters.append({
            "plugin": "registry.sagecontinuum.org/jrobrien/waggle-aqt:*.*",
            "vsn": node.split('(')[-1][:-1],
            "name": "|".join([name for name in selected_names if name.startswith("aqt")])
        })

    if any(name.startswith("co2") or name.startswith("h2o") or name.startswith("sonic") for name in selected_names):
        plugin_filters.append({
            "plugin": "registry.sagecontinuum.org/bhupendraraut/licor-smartflux:*.*",
            "vsn": node.split('(')[-1][:-1],
            "name": "|".join([name for name in selected_names if name.startswith("co2") or name.startswith("h2o") or name.startswith("sonic")])
        })

    if any("raingauge" in name for name in selected_names):
        plugin_filters.append({
            "plugin": "waggle/plugin-raingauge:*.*",
            "vsn": node.split('(')[-1][:-1],
            "name": "|".join([name for name in selected_names if "raingauge" in name])
        })

    if any(name.startswith("env") for name in selected_names):
        plugin_filters.append({
            "plugin": "waggle/plugin-iio:*.*",
            "vsn": node.split('(')[-1][:-1],
            "name": "|".join([name for name in selected_names if name.startswith("env")])
        })

    # Query data for each plugin filter and combine results
    df_list = []
    for filters in plugin_filters:
        df_data = sage_data_client.query(
            start=start,
            end=end, 
            filter=filters
        )
        df_list.append(pd.DataFrame(df_data))

    # Combine all dataframes into one
    if df_list:
        df = pd.concat(df_list, ignore_index=True)
    else:
        df = pd.DataFrame()

    return df

def filter_data_by_serial(df, serial):
    # Create an empty DataFrame to hold filtered results
    filtered_df = pd.DataFrame()

    # Check if the 'meta.Serial Number_tag' column exists and filter by it
    if 'meta.Serial Number_tag' in df.columns:
        filtered_df = pd.concat([filtered_df, df[df['meta.Serial Number_tag'] == serial]])

    # Check if the 'meta.serial_number_tag' column exists and filter by it
    if 'meta.serial_number_tag' in df.columns:
        filtered_df = pd.concat([filtered_df, df[df['meta.serial_number_tag'] == serial]])

    return filtered_df
