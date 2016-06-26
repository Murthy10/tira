# tira
An easy to use tensorflow image recognition api (still in development)

## How it works
![Overview](/tira.png)

1. Send a http multipart request with an image to tira
2. Get a JSON response with the classified objects of image

To improve further learning tira stores the images in folders based on the best classified result.

### Example
Send an image with to tira:
```python
url = '/recognition/images'
data = {'image': open('/images/blume.jpg', 'rb')}
response = self.client.post(url, data, format='multipart')
print(response.content)
```

Response:
```
b'{"4": {"score": "0.0331435", "label": "snapdragon"}, "2": {"score": "0.139561", "label": "sweet william"}, "0": {"score": "0.507734", "label": "garden phlox"}
```