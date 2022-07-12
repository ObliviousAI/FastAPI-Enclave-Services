"""
Private Set Intersection!

An MPC classic: given two lists of unique values values, returns how many values are in common 
from the two sets.

There are 2 GET handls:
    /submit_list :: accepts a csv file with 1 column from each party (can only be run once by each party)
    /compare     :: returns the number of common values from the two lists

Copyright: Oblivious Software Ltd, 2022.
"""

from fastapi import (
    APIRouter, 
    Header, 
    HTTPException, 
    UploadFile, 
    File
)
import pandas as pd

router = APIRouter(
    tags=["psi"]
    )

router.uploaded = {}

@router.post("/submit_list", tags=["oblv-role:admin"])
def submit_list(
    csv_file: UploadFile = File(...),
    x_oblv_user_name: str = Header(default=None)
):
    if x_oblv_user_name is None:
        raise HTTPException(401, "No X-OBLV-User-Name provided.")
    
    if x_oblv_user_name in router.uploaded.keys():
        raise HTTPException(401, f"Path only available for one time use. Value already uploaded by {x_oblv_user_name}.")

    try:
        # now create a temperary dataframe
        tmp_df = pd.read_csv(csv_file.file)
        
        # confirm only 1 column
        if len(tmp_df.columns) != 1:
            raise ValueError(f"Only 1 column is allowed in the CSV uploaded.")
        
        # confirm column values are unique
        col_names = list(tmp_df.columns.values)
        col_vals = tmp_df[col_names[0]].astype("str")
        values = col_vals.values
        if not col_vals.is_unique:
            raise ValueError(f"All values in the id column must be unique. This is important for the differential privacy budget.", 400)
        
    except Exception as err:
        raise HTTPException(500, str(err))
    
    router.uploaded[x_oblv_user_name] = set(values)

    return f"Successfully saved {len(values)} values uloaded by {x_oblv_user_name}."

@router.get("/compare", tags=["oblv-role:admin"])
def compare(
    x_oblv_user_name: str = Header(default=None)
):
    if x_oblv_user_name is None:
        raise HTTPException("No X-OBLV-User-Name provided.", 401)
    
    if len(router.uploaded) != 2:
        raise HTTPException(f"Path only available after both parties have uploaded their value. Currently {len(router.uploaded)} upload.", 401)
    
    values = list(router.uploaded.values())
    user_names = list(router.uploaded.keys())
    set_intersection = len(values[0].intersection(values[1]))

    return f"{user_names[0]} and {user_names[1]} have {set_intersection} values in common"
