# Fundamentals of Deep Learning Lab

## Course Information
- **Course Name:** Fundamentals of Deep Learning
- **Subject Code:** AI19541
- **Category:** Professional Core (PC)
- **Credits:** 4
- **Semester:** V (5th Semester)

## Course Objectives
- To introduce the different activation functions used in deep learning.
- To familiarize students with various training techniques for neural networks.
- To learn about Convolutional Neural Networks (CNNs).
- To explore different models of deep learning, including advanced architectures.
- To familiarize students with generative deep learning techniques and best practices.

## List of Experiments
1. **Handwritten Digit Classification** using neural networks.
2. **Image Classification Model** using the ImageNet dataset.
3. **Deep Learning Framework Study**: TensorFlow, Keras, and PyTorch.
4. **Basic CNN Model** for classification using the Dogs vs. Cats dataset.
5. **VGG-16 Model Implementation** for Dogs vs. Cats classification.
6. **Object Recognition** using YOLO.
7. **Time Series Analysis** for temperature forecasting with the Jena Weather dataset.
8. **Text Processing** for IMDB movie reviews dataset using TextVectorization.
9. **GAN-based Image Generation** for MNIST digits.

## Project: Brain Tumor Detection from MRI Scans using YOLOv11x

### Overview
In this project, we implement a **Brain Tumor Detection System** using the YOLOv11x (You Only Look Once) deep learning model. The model is trained to detect and classify brain tumors in MRI scans, providing a real-time detection system that can assist radiologists in identifying potential tumors.

### Objectives
- To detect the presence of brain tumors from MRI image scans.
- To implement the YOLOv11x object detection model for accurate and fast classification of brain tumors.
- To preprocess MRI image data and label them appropriately for YOLO training.

### Dataset
The dataset used for training consists of MRI brain images with labeled tumor regions. The data can be sourced from publicly available brain tumor MRI datasets like **Brats 2021** or any other relevant dataset.

### Steps Involved
1. **Data Preprocessing**:
   - Resize and normalize MRI images.
   - Annotate tumor regions (bounding boxes) for the YOLO model.
   
2. **Model Implementation**:
   - Set up YOLOv11x for object detection.
   - Train the model on the preprocessed MRI dataset.
   
3. **Model Evaluation**:
   - Test the model on unseen MRI images and evaluate its performance using metrics such as **Precision, Recall, and F1-score**.

4. **Real-time Detection**:
   - Implement real-time tumor detection on live MRI scans using the trained YOLOv11x model.

### Prerequisites
- Python 3.x
- TensorFlow or PyTorch
- OpenCV (for image processing)
- NumPy and Pandas
- YOLOv11x pre-trained weights and configuration files
