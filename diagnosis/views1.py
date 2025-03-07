# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt

# # Create your views here.
# import os
# import cv2
# import numpy as np
# import tensorflow as tf
# from django.shortcuts import render
# from django.core.files.storage import FileSystemStorage
# from django.http import JsonResponse
# from .models import UPLOAD_DIR

# # Load AI model (pre-trained TensorFlow model)
# MODEL_PATH = os.path.join(os.path.dirname(__file__), 'plant_disease_model.h5')
# model = tf.keras.models.load_model(MODEL_PATH)
# print(model.summary())
# # Class labels for plant diseases
# class_labels = [
#     "Apple Scab", "Apple Black Rot", "Cedar Apple Rust", "Apple Healthy",
#     "Blueberry Healthy", "Cherry Healthy", "Cherry Powdery Mildew",
#     "Corn Cercospora Leaf Spot", "Corn Common Rust", "Corn Healthy", "Corn Northern Leaf Blight",
#     "Grape Black Rot", "Grape Esca (Black Measles)", "Grape Healthy", "Grape Leaf Blight (Isariopsis Leaf Spot)",
#     "Orange Haunglongbing (Citrus Greening)", "Peach Bacterial Spot", "Peach Healthy",
#     "Pepper Bacterial Spot", "Pepper Healthy", 
#     "Potato Early Blight", "Potato Healthy", "Potato Late Blight",
#     "Raspberry Healthy", "Soybean Healthy", "Squash Powdery Mildew",
#     "Strawberry Healthy", "Strawberry Leaf Scorch",
#     "Tomato Bacterial Spot", "Tomato Early Blight", "Tomato Healthy",
#     "Tomato Late Blight", "Tomato Leaf Mold", "Tomato Septoria Leaf Spot",
#     "Tomato Spider Mites (Two-spotted Spider Mite)", "Tomato Target Spot",
#     "Tomato Mosaic Virus", "Tomato Yellow Curl Virus"
# ]

# class_recommendations = {
#     "Apple Scab": "Use fungicides like captan or mancozeb. Prune infected leaves and ensure good air circulation.",
#     "Apple Black Rot": "Remove and destroy infected fruit and branches. Use copper-based fungicides.",
#     "Cedar Apple Rust": "Apply fungicides like myclobutanil during early spring. Remove nearby cedar trees if possible.",
#     "Apple Healthy": "Maintain regular pruning, proper irrigation, and apply balanced fertilizers.",
    
#     "Blueberry Healthy": "Mulch around the base, maintain acidic soil (pH 4.5–5.5), and prune old branches.",
    
#     "Cherry Healthy": "Ensure proper watering and fertilization. Prune trees in winter to maintain structure.",
#     "Cherry Powdery Mildew": "Use sulfur or potassium bicarbonate sprays. Improve air circulation through pruning.",
    
#     "Corn Cercospora Leaf Spot": "Rotate crops, apply fungicides, and avoid overhead watering.",
#     "Corn Common Rust": "Plant resistant varieties, apply fungicides like azoxystrobin, and ensure proper nitrogen levels.",
#     "Corn Healthy": "Use proper spacing, nitrogen-rich fertilizers, and weed control.",
#     "Corn Northern Leaf Blight": "Rotate crops, plant resistant hybrids, and use fungicides if necessary.",
    
#     "Grape Black Rot": "Remove infected leaves and fruit. Use fungicides like mancozeb or myclobutanil.",
#     "Grape Esca (Black Measles)": "Avoid pruning in wet weather. Use copper-based sprays as a preventive measure.",
#     "Grape Healthy": "Maintain proper vineyard spacing, fertilize adequately, and prune vines regularly.",
#     "Grape Leaf Blight (Isariopsis Leaf Spot)": "Use organic copper sprays and remove infected leaves.",
    
#     "Orange Haunglongbing (Citrus Greening)": "Control psyllid insects with insecticides. Remove infected trees to prevent spread.",
    
#     "Peach Bacterial Spot": "Spray copper-based bactericides. Avoid overhead watering.",
#     "Peach Healthy": "Prune trees in late winter, provide potassium-rich fertilizers, and maintain good air circulation.",
    
#     "Pepper Bacterial Spot": "Use resistant varieties, apply copper fungicides, and avoid overhead irrigation.",
#     "Pepper Healthy": "Provide well-drained soil, fertilize with potassium-rich nutrients, and ensure proper sunlight.",
    
#     "Potato Early Blight": "Rotate crops, use fungicides like chlorothalonil, and avoid excessive nitrogen fertilizers.",
#     "Potato Healthy": "Hill up soil around plants, provide consistent watering, and use disease-free seeds.",
#     "Potato Late Blight": "Apply copper fungicides, avoid overhead watering, and remove infected plants immediately.",
    
#     "Raspberry Healthy": "Prune old canes after harvest, apply mulch, and protect against strong winds.",
    
#     "Soybean Healthy": "Use nitrogen-fixing bacteria inoculants, apply phosphorus fertilizers, and ensure proper spacing.",
    
#     "Squash Powdery Mildew": "Use neem oil or sulfur-based fungicides. Increase air circulation by spacing plants properly.",
    
#     "Strawberry Healthy": "Mulch with straw to prevent soil-borne diseases, fertilize regularly, and provide full sunlight.",
#     "Strawberry Leaf Scorch": "Use drip irrigation to prevent leaf wetness, prune old leaves, and apply copper-based fungicides.",
    
#     "Tomato Bacterial Spot": "Avoid planting tomatoes near peppers, apply copper fungicides, and use disease-free seeds.",
#     "Tomato Early Blight": "Mulch around plants, remove affected leaves, and use fungicides like chlorothalonil.",
#     "Tomato Healthy": "Provide calcium-rich soil, use stake support, and ensure 6–8 hours of sunlight daily.",
#     "Tomato Late Blight": "Remove infected plants immediately, apply copper fungicides, and avoid overhead watering.",
#     "Tomato Leaf Mold": "Ensure proper airflow, reduce humidity, and apply organic sulfur sprays.",
#     "Tomato Septoria Leaf Spot": "Mulch with straw, use fungicides, and prune lower infected leaves.",
#     "Tomato Spider Mites (Two-spotted Spider Mite)": "Use insecticidal soap, neem oil, or release predatory mites.",
#     "Tomato Target Spot": "Use copper-based fungicides and remove affected leaves promptly.",
#     "Tomato Mosaic Virus": "Avoid handling plants too much, remove infected plants, and disinfect tools.",
#     "Tomato Yellow Curl Virus": "Control whiteflies using neem oil or insecticidal soaps, and plant virus-resistant varieties."
# }



# @csrf_exempt 
# def upload_image(request):
#     print("---------")
#     print(request.method)
#     if request.method == 'POST' and request.FILES['image']:
#         image_file = request.FILES['image']
#         fs = FileSystemStorage(location=UPLOAD_DIR)
#         file_path = fs.save(image_file.name, image_file)
#         full_path = os.path.join(UPLOAD_DIR, file_path)

#         # Load image correctly in RGB format
#         img = cv2.imread(full_path, cv2.IMREAD_COLOR)  # Ensures 3-channel RGB
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Converts BGR to RGB (if needed)

#         # Resize image to match the model input size
#         img = cv2.resize(img, (254, 254))  # ✅ Updated to match model input

#         # Normalize pixel values (0 to 1)
#         img = img.astype(np.float32) / 255.0  

#         # Expand dimensions to match the model input shape (1, 254, 254, 3)
#         img = np.expand_dims(img, axis=0)  
#         print("hello")
#         # # Predict using AI model
#         prediction = model.predict(img)
#         print("hello1")
#         print("Prediction Output:", prediction)  # ✅ Debugging Step
#         print("Prediction Shape:", prediction.shape)  # ✅ Check if it matches expected output
#         predicted_index = np.argmax(prediction)
#         print("hello2")


#         if prediction.size == 0:  # ✅ Handle Empty Prediction Case
#             return JsonResponse({"error": "No prediction output. Please check input image processing."})

#         predicted_index = np.argmax(prediction)
#         print("Predicted Index:", predicted_index)  # ✅ Debugging Step

#         # if predicted_index >= len(CLASSES):  # ✅ Prevent IndexError
#         #     return JsonResponse({"error": "Prediction index out of range. Model might not be working correctly."})
#         print("hello3")
#         predicted_class = class_labels[predicted_index]
#         print("hello4")
#         print(predicted_class)
#         # Recommendations based on disease type
#         # recommendations = {
#         #     "Healthy": "Your plant is in great condition! Keep watering and provide proper sunlight.",
#         #     "Powdery Mildew": "Use a mixture of baking soda and water as a natural fungicide.",
#         #     "Rust": "Remove affected leaves and apply a copper-based fungicide.",
#         #     "Leaf Spot": "Avoid overhead watering and use a neem oil spray.",
#         #     "Blight": "Prune infected parts and apply an organic fungicide."
#         # }

#         return JsonResponse({
#             'status': 'success',
#             'diagnosis': predicted_class,
#             # 'diagnosis' : "Healthy",
#             # 'recommendation': recommendations["Healthy"]
#             'recommendation': class_recommendations[predicted_class]
#         })
    
#     return render(request, 'upload.html')
