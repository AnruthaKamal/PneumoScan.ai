# PneuomoScan.ai

## Overview
PneuomoScan.ai is a Streamlit application designed for detecting pneumonia from X-ray images.

## Dataset Details
The [dataset](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia) used for training and testing the PneuomoScan.ai application is sourced from Kaggle. It comprises a collection of X-ray images labeled with pneumonia and normal

## Models Used
During the development phase, several CNN variants were experimented with , specifically variants like AlexNet, VGG, and ResNet18. Among them, ResNet18 emerged as the top performer, achieving an accuracy of 0.89 on the test dataset. This indicates its robustness and effectiveness in accurately identifying pneumonia from X-ray images.

## Application Demo and Screenshots
![image](https://github.com/AnruthaKamal/PneumoScan.ai/assets/107014168/70310397-dc72-414f-9c57-195960803bf1)
![image](https://github.com/AnruthaKamal/PneumoScan.ai/assets/107014168/ea1e7248-77f8-4799-af20-de072370fe1f)
![image](https://github.com/AnruthaKamal/PneumoScan.ai/assets/107014168/7d45c1ef-9fb3-4172-8cc5-2b2d32951116)

## Usage
1. **Clone Repository:** Clone the PneuomoScan.ai repository to your local machine.
2. **Install Dependencies:** - pip install -r requirements.txt
3. **Run the Application:** - streamlit run main.py

