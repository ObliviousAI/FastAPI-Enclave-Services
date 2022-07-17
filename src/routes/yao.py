"""
Yao's Millionaire Problem!

An MPC classic: given two numbers, output which is larger without sharing either
parties inputs directly.

There are 2 GET handls:
    /submit_value :: accepts an int from each party (can only be run once by each party)
    /compare      :: returns whose value is large (on equal returns the user with first alphanumeric name)

Copyright: Oblivious Software Ltd, 2022.
"""

from fastapi import APIRouter, Header, HTTPException

router = APIRouter(
    tags=["yao"]
    )

router.uploaded = {}

@router.get("/submit_value")
def submit_value(
    value: int,
    x_oblv_user_name: str = Header(default=None)
):
    if x_oblv_user_name is None:
        raise HTTPException(401, "No X-OBLV-User-Name provided.")
    
    if x_oblv_user_name in router.uploaded.keys():
        raise HTTPException(401, f"Path only available for one time use. Value already uploaded by {x_oblv_user_name}.")

    router.uploaded[x_oblv_user_name] = value

    return f"Successfully saved {value} as value for {x_oblv_user_name}."

@router.get("/compare")
def compare(
    x_oblv_user_name: str = Header(default=None)
):
    if x_oblv_user_name is None:
        raise HTTPException("No X-OBLV-User-Name provided.", 401)
    
    if len(router.uploaded) != 2:
        raise HTTPException(f"Path only available after both parties have uploaded their value. Currently {len(router.uploaded)} upload.", 401)
    
    # sort to always be alphabetical
    user_names = list(router.uploaded.keys())
    user_names.sort()

    result = "<"
    if router.uploaded[user_names[0]] >= router.uploaded[user_names[1]]:
        result = ">="

    return f"{user_names[0]} {result} {user_names[1]}"
