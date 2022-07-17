# Runtime 🏃

In many enclave applications, you will likely want to use some environment variables or configurations that modify the application's inside behaviour. For example, perhaps you want to limit the number of queries made by each party to `n`, where `n` is a variable that is fixed but different in each deployment of the service. If this were hard-coded, the PCR hashes would change every time. This wouldn't be great if you intended to allowlist enclave applications based on PCR hashes.

The OBLV approach lets the administrator pass in a YAML file right after a deployment has been launched and before it begins to accept inbound traffic. This YAML file gets stored in `/usr/runtime.yaml`.

This runtime configuration YAML file can be loaded into your FastAPI application by combining `PyYaml` and `Pydantic BaseSettings`.

Complete code is available [here](../src/settings/settings.py), and the API example to get the config settings and return them is [here](../src/routes/config.py). 