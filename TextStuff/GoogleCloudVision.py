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

    def __detect_handwritten_ocr(self, path):
        from google.cloud import vision_v1p3beta1 as vision
        client = vision.ImageAnnotatorClient()

        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)

        image_context = vision.types.ImageContext(
            language_hints=['de-t-i0-handwrit'])

        response = client.document_text_detection(image=image,
                                                  image_context=image_context)

        return response.full_text_annotation.text

    def detectTextInImage(self, path):
        return self.__detect_handwritten_ocr(path)
