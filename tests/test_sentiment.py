from app.sentiment import analyze_comments

def test_analyze_comments():
    comments = [
        {'id': 1, 'text': 'Great post!'},
        {'id': 2, 'text': 'I disagree.'}
    ]
    analyzed_comments = analyze_comments(comments)
    
    assert len(analyzed_comments) == 2
    assert analyzed_comments[0]['id'] == 1
    assert analyzed_comments[0]['text'] == 'Great post!'
    assert 'polarity' in analyzed_comments[0]
    assert 'sentiment' in analyzed_comments[0]
    assert analyzed_comments[0]['sentiment'] == 'positive'

    assert analyzed_comments[1]['id'] == 2
    assert analyzed_comments[1]['text'] == 'I disagree.'
    assert 'polarity' in analyzed_comments[1]
    assert 'sentiment' in analyzed_comments[1]
    assert analyzed_comments[1]['sentiment'] == 'negative'
