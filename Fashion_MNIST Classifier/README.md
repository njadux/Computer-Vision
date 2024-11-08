# Image Classification with Custom Callbacks in TensorFlow/Keras

This project demonstrates the classification of images from the Fashion MNIST dataset using a neural network built with TensorFlow/Keras. It implements custom callbacks to control the training process and employs early stopping when the model achieves an accuracy of 60%.

## Project Description
- **Goal**: Classify images into different categories efficiently while preventing overfitting.
- **Key Feature**: Custom callback to halt training when a specific accuracy threshold is reached.

## Dataset
The Fashion MNIST dataset is a collection of grayscale images of size 28x28, representing 10 different categories of fashion items.

## Code Overview
- The code loads the dataset, visualizes some images, and sets up a neural network model.
- A custom callback class `myCallback` is defined to stop training when the accuracy reaches 60%.
- The model is trained with early stopping, and results are printed.

## Instructions
- Run the Python script `Fashion_MNIST_classifier.py` to train the model.
- Modify the number of epochs or accuracy threshold as needed to observe overfitting behavior.

## Dependencies
- `tensorflow`
- `numpy`
- `matplotlib`

