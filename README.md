# stability_gcloud_function

Google Cloud Function for drawing Stability/DreamStudio.ai images.

## Description

I needed a way to programmaticly generate Stability/DreamStudio.ai images by simply making a call to a webservice. This GCF takes the URL request parameter 'draw' and returns a base64 encodes image.

## Getting Started

### Dependencies

* Google Cloud account with access to Cloud Functions
* DreamStudio.AI API key 

### Installing

* create a new Cloud Function with Pyhton 3.7 as the language
* define my_http_function as entry point
* define your API KEY in main.py

### Executing program

* call the URL with the urlencoded request parameter ie `?draw=a%20windmill%20on%20a%20hill%2C%20trending%20on%20artstation`
* decode the base64 images or display in HTML 

```
 <img src="data:image/png;base64, base64data />
```
