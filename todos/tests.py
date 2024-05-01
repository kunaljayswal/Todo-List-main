from django.test import TestCase
from .models import Todo
import unittest
from django.utils import timezone
import time
from django.utils import timezone

class TodoModelTestCase(TestCase):
    def test_todo_creation(self):
        # Create a new Todo object
        todo = Todo.objects.create(title="Test Todo")

        # Check if the title is set correctly
        self.assertEqual(todo.title, "Test Todo")

        # Check if the created_at field is auto-set
        self.assertIsNotNone(todo.created_at)

        # Check if the update_at field is auto-set
        self.assertIsNotNone(todo.update_at)

        # Check if isCompleted is False by default
        self.assertFalse(todo.isCompleted)
  

    def test_todo_update(self):
        # Create a new Todo object
        todo = Todo.objects.create(title="Test Todo")

        # Update the title
        todo.title = "Updated Todo"
        todo.save()  # Save the changes explicitly

        # Check if the title is updated correctly
        self.assertEqual(todo.title, "Updated Todo")

        # Fetch the object from the database again to ensure we have the latest data
        updated_todo = Todo.objects.get(pk=todo.pk)

        # Print the values for debugging
        print("Created At:", updated_todo.created_at)
        print("Updated At:", updated_todo.update_at)

        # Check if the update_at field is updated
        self.assertTrue(updated_todo.update_at > updated_todo.created_at)



    def test_todo_completion(self):
        # Create a new Todo object
        todo = Todo.objects.create(title="Test Todo")

        # Mark the todo as completed
        todo.isCompleted = True
        todo.save()

        # Check if isCompleted is True
        self.assertTrue(todo.isCompleted)

    def test_todo_string_representation(self):
        # Create a new Todo object
        todo = Todo.objects.create(title="Test Todo")

        # Check if the string representation is correct
        self.assertEqual(str(todo), "Test Todo")

if __name__ == '__main__':
    unittest.main()
