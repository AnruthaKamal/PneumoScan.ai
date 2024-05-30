# PneuomoScan.ai

## Overview
PneuomoScan.ai is a Streamlit web application for pneumonia detection from X-rays. Various CNN variants including AlexNet, VGG, and ResNet18 were experimented with, with ResNet18 achieving the highest accuracy of 0.89. Additionally, techniques such as early stopping callbacks were incorporated to improve model training efficiency. The model training workflow was visualized using TensorBoard, and optimization techniques like pruning and quantization were implemented to enhance model inference time.

## Dataset Details
The [dataset](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia) used for training and testing the PneuomoScan.ai application is sourced from Kaggle. It comprises a collection of X-ray images labeled with pneumonia and normal

## Models Used
During the development phase, several CNN variants were experimented with , specifically variants like AlexNet, VGG, and ResNet18. Among them, ResNet18 emerged as the top performer, achieving an accuracy of 0.89 on the test dataset. This indicates its robustness and effectiveness in accurately identifying pneumonia from X-ray images.

## VGG Train Accuracy 
![WhatsApp Image 2024-05-30 at 22 04 10_25eea659](https://github.com/AnruthaKamal/PneumoScan.ai/assets/107014168/104683a0-d9ff-4441-8b7d-ed1ce3f82d8b)

## ResNet Train Accuracy 
![image](https://github.com/AnruthaKamal/PneumoScan.ai/assets/107014168/f91362f0-9d0b-4a76-8877-2f4bb43a489a)

## Application Demo and Screenshots
![image](https://github.com/AnruthaKamal/PneumoScan.ai/assets/107014168/70310397-dc72-414f-9c57-195960803bf1)
![image](https://github.com/AnruthaKamal/PneumoScan.ai/assets/107014168/ea1e7248-77f8-4799-af20-de072370fe1f)
![image](https://github.com/AnruthaKamal/PneumoScan.ai/assets/107014168/7d45c1ef-9fb3-4172-8cc5-2b2d32951116)

## Usage
1. **Clone Repository:** Clone the PneuomoScan.ai repository to your local machine.
2. **Install Dependencies:** - pip install -r requirements.txt
3. **Run the Application:** - streamlit run main.py

