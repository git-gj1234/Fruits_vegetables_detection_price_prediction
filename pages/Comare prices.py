import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt

def page(parsed_item):
    df = pd.read_csv("final_df", index_col=0)
    st.set_page_config(page_title="Price Comparison and Analysis", page_icon="📊")
    st.title("Price Comparison and Analysis")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    items = df.index.tolist()
    df = df.rename_axis('Item_name')
    dates = df.columns.tolist()

    selected_items = st.multiselect(
        "Choose items", items, [parsed_item]
    )
    if not selected_items:
        st.error("Please select at least one country.")
    else:
        date1 = st.selectbox("Select the start date", dates)
        date2 = st.selectbox("Select end date", dates)
        start = df.columns.get_loc(date1)
        stop = df.columns.get_loc(date2)
        data = df.loc[selected_items].iloc[:, start: stop + 1]
        st.write("### Item prices (Rs)", data.sort_index())
        data = data.T.reset_index()
        data = pd.melt(data, id_vars=["index"]).rename(
            columns={"index": "day", "value": "Price in Rs"}
        )
        
        # Add a radio button to select the graph type
        graph_type = st.radio("Select Graph Type:", ["Altair", "Matplotlib"])
        if graph_type == "Altair":
            show_altair_chart(data)
        elif graph_type == "Matplotlib":
            show_matplotlib_graph(data)

def show_altair_chart(data):
    chart = (
        alt.Chart(data)
        .mark_area(opacity=0.3)
        .encode(
            x="day:T",
            y=alt.Y("Price in Rs:Q", stack=None),
            color="Item_name:N",
        )
    )
    st.altair_chart(chart, use_container_width=True)

def show_matplotlib_graph(data):
    plt.figure(figsize=(10, 6))
    for item in data["Item_name"].unique():
        subset = data[data["Item_name"] == item]
        plt.plot(subset["day"], subset["Price in Rs"], label=item)

    plt.xlabel("Date")
    plt.ylabel("Price in Rs")
    plt.title("Price Comparison Over Time")
    plt.legend()
    st.pyplot()

parsed_item = "tomato"  # Define a default value
page(parsed_item)  # Call the page function with the default value
