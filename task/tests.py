from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Task

class TaskAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task_url = reverse('task-list')  # Assuming you're using a router in urls.py
        self.task_data = {
            "title": "Sample Task",
            "description": "This is a sample task description.",
            "status": "todo",
            "priority": "medium",
            "due_date": "2024-10-08"
        }
        self.task = Task.objects.create(**self.task_data)
        self.detail_url = reverse('task-detail', kwargs={'pk': self.task.id})

    def test_create_task(self):
        response = self.client.post(self.task_url, data=self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)  # One created in setUp, one by this test

    def test_retrieve_task_list(self):
        response = self.client.get(self.task_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_task_detail(self):
        response = self.client.get(self.detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.task_data['title'])

    def test_update_task(self):
        update_data = {
            "title": "Updated Task",
            "description": "Updated description.",
            "status": "in_progress",
            "priority": "high",
            "due_date": "2024-12-01"
        }
        response = self.client.put(self.detail_url, data=update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, update_data['title'])
        self.assertEqual(self.task.status, update_data['status'])

    def test_delete_task(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

