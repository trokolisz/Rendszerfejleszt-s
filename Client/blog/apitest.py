from rest_framework.test import APIRequestFactory
from login.models import Comment  # Import your Comment model
from login.serializers import CommentSerializer  # Import your Comment serializer

# Create a test request

factory = APIRequestFactory()
request = factory.post('/api/comments/', {'body': 'Test comment'}, format='json')

# Make sure to authenticate the request if needed
# force_authenticate(request, user=my_user)

# Process the request using your view
# response = my_comment_create_view(request)

# Assert the response status code and other relevant data
# self.assertEqual(response.status_code, 201)
# ...

# Deserialize the response data (if applicable)
# comment_data = response.data
# comment = Comment.objects.get(pk=comment_data['id'])
# serializer = CommentSerializer(comment)

# Perform additional assertions as needed
# self.assertEqual(serializer.data['body'], 'Test comment')
# ...

# Clean up (if necessary)
# comment.delete()
