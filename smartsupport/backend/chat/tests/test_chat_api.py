import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


User = get_user_model()


@pytest.mark.django_db
def test_chat_flow(monkeypatch):
    # create user
    user = User.objects.create_user(username='testuser', password='pass123')
    client = APIClient()
    # obtain token
    resp = client.post('/api/auth/token/', data={'username': 'testuser', 'password': 'pass123'})
    assert resp.status_code == 200
    token = resp.data['access']
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')


    # monkeypatch OpenAI client to avoid real API call
    class DummyClient:
        def ask(self, prompt, max_tokens=500, temperature=0.2):
            return 'This is a dummy AI response.'


    monkeypatch.setattr('services.openai_client.OpenAIClient', lambda *a, **k: DummyClient())


    # send chat
    r = client.post('/api/chat/', data={'text': 'Hello, I need help.'})
    assert r.status_code == 200
    data = r.data
    assert 'messages' in data[0] or 'messages' in data # serializer returns conversation