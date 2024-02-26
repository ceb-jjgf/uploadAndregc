from django.test import TestCase

# Create your tests here.
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

class FileUploadTests(TestCase):
    def test_file_upload(self):
        url = reverse('upload_video')  # 假设你的上传URL名称为'upload_video'
        # 这里open需要上传的文件
        with open('video.mp4', 'rb') as file:
            response = self.client.post(url, {'video': file}, format='multipart')
            self.assertEqual(response.status_code, 200)
            self.assertIn('上传成功', response.content.decode())
