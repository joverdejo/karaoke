import requests
data = {
    'url': 'https://audd.tech/example1.mp3',
    'return': 'timecode,apple_music,deezer,spotify',
    'api_token': 'test'
}
result = requests.post('https://api.audd.io/', data=data)
print(result.text)