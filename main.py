import functions_framework
import io
import os
import warnings
import time
import base64

from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

stability_api = client.StabilityInference(
    key='DREAMSTUDIO_API_KEY', 
    verbose=True
)

# Register an HTTP function with the Functions Framework
@functions_framework.http
def my_http_function(request):
  # Your code here
  # Here the query parameters
  if request.args and 'draw' in request.args:

    stability_prompt = request.args.get('draw')

    # the object returned is a python generator
    answers = stability_api.generate(
        prompt=stability_prompt,
        # seed=34567, # if provided, specifying a random seed makes results deterministic
        steps=30,
        width=768,
        height=1024 # defaults to 50 if not specified
    )

    # iterating over the generator produces the api response
    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                warnings.warn(
                    "Your request activated the API's safety filters and could not be processed."
                    "Please modify the prompt and try again.")
            if artifact.type == generation.ARTIFACT_IMAGE:
                encoded_string = base64.b64encode(artifact.binary)
                return encoded_string

  # Return an HTTP response
  return 'OKs'
