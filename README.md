**PROJECT TITLE**

This project combines a neural network model with a simple graphical user interface (GUI) built using Tkinter to predict the stage of sciatica based on user-provided answers to specific questions. The prediction is then used to recommend appropriate treatment options.

**FEATURES**
- Neural Network Model: Trained using TensorFlow/Keras to classify input data into one of five sciatica severity stages (I, II, III, IV, V).
  Predicts the stage of sciatica based on user-provided answers.

- Graphical User Interface (GUI): Developed using Tkinter, providing an interactive environment for users to answer questions and receive predictions.
  Simple and intuitive GUI for user interaction.

- Recommendations: Based on the predicted stage, the application provides treatment recommendations sourced from a CSV file.
  Displays recommendations corresponding to the predicted stage.


**PROJECT DESCRIPTION**

This project helps predict the severity stage of sciatica, a condition causing pain in the lower back and legs, based on how someone answers specific questions about their symptoms. There are 8 set of questions that a customer must answer based on their condition's symptoms. Upon answering the multiple choice questions, the model will assign a condition stage to the customer and recommend appropriate treatment options using a different product kits. The stages range from Stage 1 to Stage 5 in the order of increasing severity and each stage has a product kit assigned to it.

**USING THE GUI**
- Interface: The GUI window titled "Sciatica Stage Predictor" will display a series of questions related to sciatica symptoms.
- Answering Questions: For each question, select one of the provided answers ('A', 'B', 'C', 'D') using radio buttons.
- Predicting Stage: Click the "Predict" button after answering all questions. The application will predict the severity stage based on your responses.
- Viewing Recommendations: Based on the predicted stage, the application will display treatment recommendations fetched from recommendations.csv.

Images attached (Output):
![Screenshot 2024-06-18 171953](https://github.com/maheekabangroo/Sciatica-Product-Prediction-using-Neural-Networks/assets/100994133/9ade9366-0d03-453d-a8e1-5639b609ac3e)







