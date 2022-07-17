# Private Set Intersection Cardinality :eyes:

PSI-CA, as it's abbreviated, usually involves two parties having two sets of values, and the question is, "how many items do we have in common?".
Of course, the caveat is that they do not want to reveal their list to the other party, only the cardinality of the intersection.

In this example, we let the two parties upload CSV files containing a single data column. 
We extract the column data, confirm the values are unique and save it in memory once the other party has uploaded their data.
Like Yao's Millionaire Problem, we don't want either party to abuse the system, so we only allow them to upload their data once.
This core functionality is captured in the upload API handle:

```python
@router.post("/submit_list")
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
```

:warning: **Note**: PSI is an input privacy constraint, but you may also require output privacy in some cases.
For example, if I wanted to test if "Charlie" was on the other parties' list, I could upload a siingle value and learn about Charlie specifically (not super private from Charlie's perspective!).
PSI is good if you want to prevent the other party from scraping all of your data, i.e. when one value isn't so significant, but many values become highly sensitive.
Of course, you can add nuances to this code base to deal with all of these constraints, but worth thinking through for any specific application :bowtie:

The full code is available [here](../src/routes/psi.py).
