# Speak No Evil 🙊

Enclaves intensionally minimize IO which is important to establish trust in the services confidentiality. 
However, occasionally you need to make outbound calls from the enclave to a secure endpoint.
To do this the endpoint of interest has to be hardcoded during the service configuration steps. 

Whitelisting is performed at the TCP layer based on fully-qualified domain names (FQDNs) ie IP addresses or typically what you think of as a route domain name.
As an example, if `http://example.com` is allowed then associated paths such as `http://example.com/test` will also be approved, but not `http://test.example.com` which uses a subdomain.

This example service is simply made so you can test the funcaitonality of outbound connections and uses the standard  Python `requests` library.

Full code is available [here](../src/routes/outbound.py).
