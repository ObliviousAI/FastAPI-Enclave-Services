# Yao's Millionaire Problem 💵

This is a really clasic MPC problem posed by [Andrew Yao in 1982](https://en.wikipedia.org/wiki/Yao%27s_Millionaires%27_problem). 
The premise is that there are two millionaires who wish to identify who is richest, but do not wish to disclose their wealth to one another.
Traditionally, this is solved using a varient of oblivious transfer (*FYI:* where our company got it's name), but in our setting we'll use an enclave.

In settings like this we have to be really careful of who inputs what and who recieves what. 
Input validation, the frequency which a party can call an API end point, the time it takes to respond and more should all be taken into account.

We give a simple demonstration of this, where the path `/submit_value` can only be called once by each party (ensured by their username not being in the dictionary keys of the `uploaded` dictionary):

```python
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
```

Give it a go yourself with a friend if you like! The code can be seen [here](../src/routes/yao.py).
