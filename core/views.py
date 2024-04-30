import cv2
import numpy as np
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .eye_tracking import EyeTracker

class ImageView(APIView):
    def post(self, request):
        # Check if 'image' file is in the request
        if 'image' not in request.FILES:
            return Response({'error': 'No image file uploaded'}, status=status.HTTP_400_BAD_REQUEST)

        # Read and validate the image using OpenCV
        image_file = request.FILES['image']
        try:
            image_array = np.frombuffer(image_file.read(), np.uint8)
            frame = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        except Exception as e:
            return Response({'error': 'Failed to read the image file'}, status=status.HTTP_400_BAD_REQUEST)

        if frame is None:
            return Response({'error': 'Uploaded file is not a valid image'}, status=status.HTTP_400_BAD_REQUEST)

        # Process the image frames using EyeTracker
        eye_tracker = EyeTracker()
        eye_tracker.process_frames(frame)

        # Get the current state from the EyeTracker
        response =  {'state': eye_tracker.get_current_state()}

        # Return the response with eye tracking data
        return Response(response, status=status.HTTP_201_CREATED)
