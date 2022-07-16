"""
Hello World in the Enclave!

A simple GET handle that returns the users name and role.

Copyright: Oblivious Software Ltd, 2022.
"""

from fastapi import APIRouter, Header, HTTPException

router = APIRouter(
    tags=["hello_world"]
    )

@router.get("", tags=["oblv-role:admin"])
def hello(
    x_oblv_user_name: str = Header(default=None),
    x_oblv_user_role: str = Header(default=None)
):
    if x_oblv_user_name is None:
        raise HTTPException(401, "No X-OBLV-User-Name provided.")
    elif x_oblv_user_role is None:
        raise HTTPException(401, "No X-OBLV-User-Role provided.")
    
    return f"Hello {x_oblv_user_name}, your role is {x_oblv_user_role}"
