# tira
An easy to use tensorflow image recognition api (still in development)

## How it works
![Overview](/tira.png)

1. Send a http multipart request with an image to tira
2. Get a JSON response with the classified objects of the image

To improve further learning tira stores the images in folders based on the best classified result.

### Example
Send an image with to tira.
```
curl -i -F image=@blume.jpg http://localhost:8000/recognition/images
```

Response:
```
{"4": {"score": "0.0331435", "label": "snapdragon"}, "2": {"score": "0.139561", "label": "sweet william"}, "0": {"score": "0.507734", "label": "garden phlox"}
```

### Use your own trained model
Tira works with a trained tensorflow model and simply uses the graph and labels files.
So if you'd like to use your own trained model just overwrite the graph.pb and the labels.txt flies in the /tira/tira/apps/recognition/graph/ directory.

## Usage
The easiest way to use tira is to pull the dockercontainer from dockerhub.

```
docker pull murthy10/tira
```

And finally run the container:

```
docker run -d -p 8000:8000 murthy10/tira:latest
```

To check if everything went okey navigate to http://localhost:8000

### Copy stored images
For further training of the neural network you can copy the images from tira to your local machine.
```
docker cp <containerId>:/tira/tira/media /host/path/target
```