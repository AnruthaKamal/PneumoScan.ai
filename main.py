import streamlit as st
import pickle 
from PIL import Image
import torch
import torchvision.transforms as transforms
def preprocess_image(image):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])
    return transform(image).unsqueeze(0)

def make_prediction(model,test_image): 
    output = model(test_image)     
    _, prediction =  torch.max(output,1)
    #return prediction.cpu().detach().numpy() 
    return prediction.item()
def main():
    st.title("PneumoScan.ai")
    
    # Sidebar navigation
    navigation = st.sidebar.radio("Navigation", ["About PneumoScan.ai", "Pneumonia Detection"])
    
    if navigation == "About PneumoScan.ai":
        st.write("""
        Hello! I'm PneumoScan.ai, your advanced tool for detecting pneumonia from chest X-ray images. 
        Using cutting-edge artificial intelligence and deep learning algorithms, I help healthcare professionals 
        quickly and accurately diagnose pneumonia, ensuring timely and effective treatment for patients.
        """)
        
        st.header("What is Pneumonia?")
        st.write("""
        Pneumonia is an infection that inflames the air sacs in one or both lungs. The air sacs may fill with fluid or pus, 
        causing symptoms such as cough, fever, chills, and difficulty breathing. It can range in seriousness from mild to life-threatening, 
        especially in infants, young children, the elderly, and people with underlying health conditions.
        """)
        
        st.header("Significance of Identifying Pneumonia Early")
        st.write("""
        Early identification of pneumonia is crucial for effective treatment and better patient outcomes. Pneumonia can lead to severe complications if not treated promptly. 
        By utilizing me, PneumoScan.ai, healthcare providers can:
        - Quickly screen and diagnose patients
        - Reduce the risk of complications
        - Provide timely and appropriate treatment
        - Improve overall patient care and outcomes
        """)

    elif navigation == "Pneumonia Detection":
        st.write("Upload an image of the chest xray , and PneumoScan.ai will classify it for you.")
        uploaded_file = st.file_uploader("Choose an image...", type="jpeg")
        if uploaded_file is not None:
            pic = Image.open(uploaded_file).convert("RGB")
            input_tensor = preprocess_image(pic)
            st.image(pic, caption='Uploaded Image.', width=300)
            st.write("")
            # Load the model
            model = pickle.load(open('model.pkl', 'rb'))    
            # Make prediction
            prediction = make_prediction(model, input_tensor)
            # Display prediction result
            if prediction == 1:
                st.write("Pneumonia detected.")
            else:
                st.write("No pneumonia detected. X-ray is normal.")

if __name__ == "__main__":
    main()

