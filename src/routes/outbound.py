"""
Enclave outbound connection demo.

A few examples of accepted and rejected outbound connection calls. It is assumed that
the enclave is configured to make outbound connections to https://example.com/.

Copyright: Oblivious Software Ltd, 2022.
"""

from fastapi import APIRouter, Header, HTTPException
import requests
import validators

router = APIRouter(
    tags=["outbound"]
    )

@router.get("", tags=["oblv-role:admin"])
def reach_out(
    url: str,
    x_oblv_user_name: str = Header(default=None)
):
    if x_oblv_user_name is None:
        raise HTTPException(401, "No X-OBLV-User-Name provided.")
    
    if not validators.url(url):
        raise HTTPException(401, "URL provided is not a valid address.")

    # request from specified url [should return correctly]
    r = requests.get(url)

    return f"Request returned status code {r.status_code}"