#Loading the required libraries

import pandas as pd
import numpy as np

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Loading the dataset
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

# Compilation of the model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Training of the model
model.fit(X, y, epochs=100, batch_size=10)


# Function to predict stage
def predict_stage(answers):
    encoded_answers = np.array([answer_encoding[answer] for answer in answers]).reshape(1, -1)
    prediction = model.predict(encoded_answers)
    predicted_stage = np.argmax(prediction)
    for stage, code in stage_encoding.items():
        if code == predicted_stage:
            return stage


# Main function
def main():
    # Load questions and options from CSV
    questions_df = pd.read_csv('questions.csv')

    # Extract questions and options
    questions = questions_df['Question'].tolist()
    options = questions_df.iloc[:, 1:].values.tolist()  # Exclude the first column (Question)

    print("Please answer the following questions:")
    answers = []
    for i, question in enumerate(questions):
        print(question)
        for option in options[i]:
            print(option)
        answer = input("Enter your answer (A, B, C, D): ").strip().upper()
        answers.append(answer)

    final_stage = predict_stage(answers)
    recommendations = {
        'I': "Stage 1: 1 Veinocap + 2 Leglite, Duration: 1 month, MRP: 3240, Selling: 2574, Discount: 21%",
        'II': "Stage 2: 2 Veinocap + 3 Leglite, Duration: 2 months, MRP: 5490, Selling: 4356, Discount: 21%",
        'III': "Stage 3: 3 Veinocap + 4 Leglite, Duration: 3 months, MRP: 7740, Selling: 6138, Discount: 21%",
        'IV': "Stage 4: 4 Veinocap + 6 Leglite, Duration: 4 months, MRP: 10980, Selling: 8712, Discount: 21%",
        'V': "Stage 5: OPTM, Duration: to be decided on further consultation"
    }
    print(f"\nBased on your answers, you are recommended: {recommendations[final_stage]}")


if __name__ == "__main__":
    main()
