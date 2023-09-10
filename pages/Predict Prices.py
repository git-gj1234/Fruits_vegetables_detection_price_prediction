import math
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

path = './final_df'
df = clean_filled = pd.read_csv(path, index_col=0) 
def Model(N):
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=(N, 1)),
        LSTM(58, return_sequences=False),
        Dense(25),
        Dense(1)
    ])
    return model

def plotter(t, v, p):
    plt.title('Model')
    plt.plot(t)
    plt.plot(v)
    plt.plot(v.index, p)
    plt.legend(['Train', 'Val', 'Predictions'], loc='lower right')
    st.pyplot(plt)

def predictor(veggie):
    st.write(f"Predicting for {veggie}...")
     # reading data

    # data formatting
    data = df.loc[veggie]
    dataset = np.array([[i] for i in data.values])

    # training data
    training_data_len = math.ceil(len(dataset) * .8)
    training_data_len = math.ceil(len(dataset) * .8)

    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(dataset)

    x_train = []
    y_train = []
    train_data = scaled_data[0: training_data_len]
    for i in range(60, len(train_data)):
        x_train.append(train_data[i - 60:i, 0])
        y_train.append(train_data[i, 0])
    x_train, y_train = np.array(x_train), np.array(y_train)
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

    # model assignment
    model = Model(x_train.shape[1])
    # model compilation
    model.compile(optimizer='adam', loss='mean_squared_error')
    
    # Add a progress bar
    progress_bar = st.progress(0)
    
    # Training loop with multiple epochs
    num_epochs = 2
    for epoch in range(num_epochs):
        model.fit(x_train, y_train, batch_size=1, epochs=1, verbose=1)
        
        # Update progress bar after each epoch
        progress = (epoch + 1) / num_epochs
        progress_bar.progress(progress)

    # formatting test data
    test_data = scaled_data[training_data_len - 60:, :]
    x_test = []
    y_test = dataset[training_data_len:, :]
    for i in range(60, len(test_data)):
        x_test.append(test_data[i - 60:i, 0])
    x_test = np.array(x_test)
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

    # prediction from model
    predictions = model.predict(x_test)
    predictions = scaler.inverse_transform(predictions)

    # values for graphs
    train = data[:training_data_len]
    valid = data[training_data_len:]

    return train, valid, predictions  # training data, validation data, prediction data directly plot

st.title('Veggie Price Prediction App')
l = df.index.tolist()
veggie = st.selectbox('Select the vegetable name (e.g., tomato):',l)

if st.button('Predict'):
    train, valid, predictions = predictor(veggie)
    st.write("Plotting...")
    plotter(train, valid, predictions)
