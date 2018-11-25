import io
import os

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

DISCOVERY_URL = 'https://{api}.googleapis.com/$discovery/rest?version={apiVersion}'  # noqa

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '../Configs/gcloud_prod.json'


class GoogleCloudVision:
    """Construct and use the Google Vision API service."""

    def __init__(self, api_discovery_file='vision_api.json'):
        self.credentials = GoogleCredentials.get_application_default()
        self.service = discovery.build(
            'vision', 'v1', credentials=self.credentials,
            discoveryServiceUrl=DISCOVERY_URL)

    def __detect_handwritten_ocr(self, data):
        from google.cloud import vision_v1p3beta1 as vision
        client = vision.ImageAnnotatorClient()

        image = vision.types.Image(content=data)

        image_context = vision.types.ImageContext(
            language_hints=['de-t-i0-handwrit'])

        response = client.document_text_detection(image=image,
                                                  image_context=image_context)

        return response.full_text_annotation.text

    def detectTextInImageFile(self, path):
        with io.open(path, 'rb') as image_file:
            content = image_file.read()
        return self.__detect_handwritten_ocr(content)

    def detectTextInBase64Image(self, data):
        return self.__detect_handwritten_ocr(data)
