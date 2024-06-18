# Loading relevant libraries
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Load the dataset
data = pd.read_csv('sciatica_data.csv')

# Encode the answers and stages
answer_encoding = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
stage_encoding = {'I': 0, 'II': 1, 'III': 2, 'IV': 3, 'V': 4}
data_encoded = data.replace(answer_encoding)
data_encoded['Stage'] = data_encoded['Stage'].replace(stage_encoding)

# Split the dataset into features (X) and labels (y)
X = data_encoded.iloc[:, :-1].values
y = data_encoded['Stage'].values

# Define the neural network model
model = Sequential()
model.add(Dense(64, input_dim=8, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(5, activation='softmax'))  # 5 stages, hence 5 output neurons

# Compile the model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=100, batch_size=10)

# Function to predict stage
def predict_stage(answers):
    encoded_answers = np.array([answer_encoding[answer] for answer in answers]).reshape(1, -1)
    prediction = model.predict(encoded_answers)
    predicted_stage = np.argmax(prediction)
    for stage, code in stage_encoding.items():
        if code == predicted_stage:
            return stage

# Function to handle button click (prediction and result display)
def predict():
    answers = [var.get() for var in answer_vars]
    final_stage = predict_stage(answers)
    if final_stage in recommendations_dict:
        result_label.config(text=f"Based on your answers, your predicted stage is {final_stage}.\nYou are recommended: {recommendations_dict[final_stage]}")
    else:
        result_label.config(text=f"Your predicted stage is {final_stage}, but no recommendation was found for this stage.")

# Create the GUI
root = tk.Tk()
root.title("Sciatica Stage Predictor")

# Load questions and options from CSV
questions_df = pd.read_csv('questions.csv')
questions = questions_df['Question'].tolist()
options = questions_df.iloc[:, 1:].values.tolist()

# Load recommendations from CSV
recommendations_df = pd.read_csv('recommendations.csv')
recommendations_dict = recommendations_df.set_index('Stage')['Recommendation'].to_dict()

# GUI elements
question_frame = tk.Frame(root)
question_frame.pack(pady=20, padx=10)

answer_vars = []
for i, question in enumerate(questions):
    tk.Label(question_frame, text=question, wraplength=600, justify='left').grid(row=i, column=0, sticky='w')
    var = tk.StringVar()
    answer_vars.append(var)
    for j, option in enumerate(options[i]):
        tk.Radiobutton(question_frame, text=option, variable=var, value=option[0], wraplength=600, justify='left').grid(row=i, column=j+1, sticky='w')

# Predict button
predict_button = tk.Button(root, text="Predict", command=predict)
predict_button.pack()

# Result label
result_label = tk.Label(root, text="", wraplength=600, justify='left')
result_label.pack(pady=20)

root.mainloop()
