import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_comments(client, mocker):
    # Mocking the fetch_comments_from_subfeddit function
    mocker.patch('app.routes.fetch_comments_from_subfeddit', return_value=[
        {'id': 1, 'text': 'Great post!'},
        {'id': 2, 'text': 'I disagree.'}
    ])
    
    response = client.get('/comments/test_subfeddit')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2
    assert data[0]['text'] == 'Great post!'
    assert data[1]['text'] == 'I disagree.'
    assert 'polarity' in data[0]
    assert 'sentiment' in data[0]
