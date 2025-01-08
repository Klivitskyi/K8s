from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json
import base64

app = FastAPI()

@app.post("/mutate")
async def mutate(request: Request):
    admission_review_request = await request.json()

    print(admission_review_request)

    if admission_review_request['request']['resource']['resource'] != "pods":
        return JSONResponse(content={"response": {"allowed": True}})
    
    pod = admission_review_request['request']['object']
    patch = []

    for i, container in enumerate(pod['spec']['containers']):
        patch.append({
            "op": "replace",
            "path": f"/spec/containers/{i}/imagePullPolicy",
            "value": "Always"
        })

    patch.append({
        "op": "add",
        "path": "/metadata/annotations/mutated",
        "value": "true"
    })

    patch_base64 = base64.b64encode(json.dumps(patch).encode("utf-8")).decode("utf-8")

    admission_review_response = {
        "apiVersion": "admission.k8s.io/v1",
        "kind": "AdmissionReview",
        "response": {
            "uid": admission_review_request["request"]["uid"],
            "allowed": True,
            "patch": patch_base64,
            "patchType": "JSONPatch"
        }
    }
    
    return JSONResponse(content=admission_review_response)