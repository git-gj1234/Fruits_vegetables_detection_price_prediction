ion in making healthier choices, saving money, and gaining a deeper understanding of the world of fruits and vegetables. It's not just an app; it's a journey through nature's finest, enhanced by the Streamlit experience.")
st.write("Begin your FreshHarvest adventure today and savor the beauty, flavors, and wisdom of fresh produce like never before! 🌿🛒")

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