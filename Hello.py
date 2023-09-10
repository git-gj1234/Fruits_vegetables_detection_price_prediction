import streamlit as st
import pandas as pd
import math
from PIL import Image
import matplotlib.pyplot as plt

data = pd.read_csv('final_df', index_col=0)
# print(data.index.tolist())
# Create a DataFrame with one Label of each category
train_df = pd.read_csv('train_df')
df_unique = train_df.copy().drop_duplicates(subset=["Label"]).reset_index()

st.set_page_config(
    page_title="FreshHarvest: Your Ultimate Fruits and Vegetables Companion!",
    page_icon="🍏"
)

# Header
st.title("Welcome to FreshHarvest: Your Ultimate Fruits and Vegetables Companion!")
st.markdown("🍏🥕🍅🌽")

# Introduction
st.write("Step into a world of freshness and innovation with FreshHarvest, your go-to hub for all things fruits and vegetables, thoughtfully crafted with Streamlit. Here, we blend the beauty of nature's bounty with the power of cutting-edge technology to offer you a delightful and informative experience.")

# Features
st.subheader("With FreshHarvest, you can:")
st.write("🍎 Explore Freshness: Dive into our virtual marketplace to discover an array of fresh, vibrant fruits and vegetables. Get up-close with their textures, colors, and nutritional profiles as if you were strolling through your favorite farmer's market.")
st.write("🔍 Compare Prices: Make informed decisions effortlessly. Compare prices, find the best deals, and ensure you get the freshest produce without breaking the bank.")
st.write("🚀 Predict the Future: Harness the power of data and machine learning to foresee price trends. Our predictive tools provide you with insights that help you plan your purchases wisely.")
st.write("📷 Scan and Identify: Wondering what that unique-looking fruit or veggie is? Simply scan and upload an image, and our advanced image recognition technology will reveal its identity in an instant.")

# Conclusion
st.write("FreshHarvest is your companion in making healthier choices, saving money, and gaining a deeper understanding of the world of fruits and vegetables. It's not just an app; it's a journey through nature's finest, enhanced by the Streamlit experience.")
st.write("Begin your FreshHarvest adventure today and savor the beauty, flavors, and wisdom of fresh produce like never before! 🌿🛒")

st.write("Available items: ")
# Display each item with its image in columns
# st.title("Fruits and vegetables dataset")
index_names = df_unique["Label"].tolist()

# Define the number of columns for your layout
num_columns = 3

# Calculate the number of rows required
num_rows = math.ceil(len(index_names) / num_columns)

# Set the desired image size
image_size = (244, 244)

# Create a grid layout
for i in range(num_rows):
    columns = st.columns(num_columns)
    for j in range(num_columns * i, min(num_columns * (i + 1), len(index_names))):
        with columns[j % num_columns]:
            # Open the image and resize it to the desired size
            image = Image.open(df_unique.Filepath[j])
            image = image.resize(image_size)
            date = data.columns[-1]
            price = data.loc[df_unique.Label[j], date]
            # Display the resized image with its label
            st.image(image, caption=df_unique.Label[j], use_column_width=True)
            st.write("Last recoreded date: ",date)
            st.write("Price: ",price)
