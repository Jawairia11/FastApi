import os
import cv2
import uuid
import numpy as np

# Function to process an uploaded image and save it as grayscale
def do_gray_image(image_bytes):
    try:
        # Read the uploaded image
        image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)

        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Generate a unique filename
        unique_filename = str(uuid.uuid4()) + ".jpg"
        output_path = os.path.join("C:\\zztemp", unique_filename)

        # Save the grayscale image to a specific directory
        cv2.imwrite(output_path, gray_image)

        return output_path
    except Exception as e:
        return None

# Averging Filter image using python
def do_avg_image(image_bytes):
    try:
        # Read the uploaded image
        image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)

        # Convert the image to grayscale
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        
        kernel = np.ones((8,8), np.float32)/32
        avg_image = cv2.filter2D(rgb_image, -1, kernel)

        # Generate a unique filename
        unique_filename = str(uuid.uuid4()) + ".jpg"
        output_path = os.path.join("C:\\zztemp", unique_filename)

        # Save the grayscale image to a specific directory
        cv2.imwrite(output_path, avg_image)

        return output_path
    except Exception as e:
        return None


# Gaussian Blur Filter image
def do_gaussian_image(image_bytes):
    try:
        # Read the uploaded image
        image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)

        # Convert the image to grayscale
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        blur_image = cv2.GaussianBlur(rgb_image,(25,25),200)

        # Generate a unique filename
        unique_filename = str(uuid.uuid4()) + ".jpg"
        output_path = os.path.join("C:\\zztemp", unique_filename)

        # Save the grayscale image to a specific directory
        cv2.imwrite(output_path, blur_image)

        return output_path
    except Exception as e:
        return None 

# Edge Detection Filter image
def do_edge_image(image_bytes):
    try:
        # Read the uploaded image
        image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)

        # Convert the image to grayscale
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        edge_image = cv2.Canny(rgb_image,100,200)

        # Generate a unique filename
        unique_filename = str(uuid.uuid4()) + ".jpg"
        output_path = os.path.join("C:\\zztemp", unique_filename)

        # Save the grayscale image to a specific directory
        cv2.imwrite(output_path, edge_image)

        return output_path
    except Exception as e:
        return None       
 
# Sharpening Filter image
def do_sharpen_image(image_bytes):
    try:
        # Read the uploaded image
        image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)

        # Convert the image to grayscale
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        kernel = np.array([[-1,-1,-1], [-1,16,-1], [-1,-1,-1]])
        sharpen_image = cv2.filter2D(rgb_image, -3, kernel)

        # Generate a unique filename
        unique_filename = str(uuid.uuid4()) + ".jpg"
        output_path = os.path.join("C:\\zztemp", unique_filename)

        # Save the grayscale image to a specific directory
        cv2.imwrite(output_path, sharpen_image)

        return output_path
    except Exception as e:

        return print("exception")