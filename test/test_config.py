from bot.config import create_api


def test_create_api():
    """Test whether we can use the API"""
    api = create_api()
    assert api.me().screen_name == "AvondkIok"
