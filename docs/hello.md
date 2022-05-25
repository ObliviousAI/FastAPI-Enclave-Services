# Oh, Hello There :wave:

This API is the most simple - it simply returns to you a greating followed by your name and role. The OBLV enclave proxy adds the header fields `X-OBLV-User-Name` and `X-OBLV-User-Role` during the authentication and authorization of traffic into the enclave. You can read from them in FastAPI easily like this:

```python
@router.get("/")
def hello(
    x_oblv_user_name: str = Header(default=None),
    x_oblv_user_role: str = Header(default=None)
):
  # main logic
```

:warning: Note: you'll see in the example code we validate the are not `None`. While this should never be the case for incoming traffic, it's best to minimize the trust dependancies when possible.

The full code can be found [here](../../src/routes/hello.py).
