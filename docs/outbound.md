# Speak No Evil 🙊

Enclaves intensionally minimize IO, which is essential to establish trust in the confidentiality of the service. 
However, occasionally you need to make outbound calls from the enclave to a secure endpoint.
To do this, the endpoint of interest has to be hardcoded during the service configuration steps. 

Allowlisting is performed at the TCP layer based on fully-qualified domain names (FQDNs), i.e. IP addresses or typically what you think of as a route domain name.
For example, if `http://example.com` is allowed, associated paths such as `http://example.com/test` will also be approved, but not `http://test.example.com`, which uses a subdomain.

This example service is made so you can test outbound connections' functionality and use the standard  Python `requests` library.

Full code is available [here](../src/routes/outbound.py).
