# Where FastAPI becomes FastEnclaves: MPC in Minutes 🦹‍♀️ 🦸‍♂️ 👩‍🚀 

[![](https://img.shields.io/badge/-OBLV:_Made%20for%20Enclaves-93228f?style=for-the-badge&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAQAAADZc7J%2FAAAABGdBTUEAALGPC%2FxhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAAmJLR0QA%2F4ePzL8AAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAHdElNRQfmBRQLNCJ5TUB1AAACu0lEQVRIx42VTWhdVRDHf7mxJe%2BlTWqVSlKJbZCGIib1iSGLbCq4aKkQlJagATdulFKEQMStduHGEHCRViW6EVwJQhBCqaYgih8YkxQhUluhxGIDMU2TmPhe%2BnNx7n339eV9OHcxd2bO%2F3%2FnnJkzt4EKYiunOE43h9gHrPAHs3zNZMMq9cWjfuyGlWTDCbtqg7OOmbeW5B01Uw3e7g%2F%2BH5mxoxI855%2Fpmiu%2BYa8PibjfPof9xntpeNFcOfzRFP65T0qF55iTKcVtj5TCM34f%2FHc8LeIuB%2FzAb73mb172XZ%2BOSV72bkJx1WxKMBZ8S%2FaIeMrfd2x8Oo4943LiOp8WLq%2B6aZ%2BII6W7LZEtXxGx363gWLc9EHwS7GERB2sc%2F7ZnRHwrcVwEbAlts%2BADYrN%2F1azgigfEXV5Lctgb8TwZgPcoAEMcqNlqrbwG5BkNZpaT%2BJHqv%2B4XcapuF03HvRE37MWIHoCfWQYgRz1pBWCZmWD2RBwCuApAEw%2FXJViI9a9BHY5oAbgNwO66cPgw1rfihKKg7wHwD9aBX%2BBy%2FFaIdcQqwIMA5FmqAZb3OVu04s3eibgBkNyM%2Barwm5zgHNtF%2B2hQ1yNmAfpoAuBSFfg0TzFVYmfoDS9z%2BFIoaGjSxyxUqP2PZsqu9lASOoMtrqv%2BZCTiZxUIesvgkTNJK%2B8BnAjWqyJ2uFIG39gxWl5PQuPhdLtCX655TMSBsm0UbL4Pngsp65ptSYFGg%2BeWT4j4Yjp3Ss4nPN3pfX07rXBTMtL%2B9gURO%2F3UzSLBcBE%2B6GrinC8ZaeBBF5PIF%2FHwarbf0z5nZzH1%2B4bq4%2BV9lnMpjX%2FniP0%2BYqONttnvm0mKCbzStfWI83XHgercjq8XKbKeT464iqz5TtVfW0zS7oUqJOuOFwtXlIaKJHs5ybP00EkrsMINfuErvmxY27n2P7cF8FI7UOqVAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDIyLTA1LTIwVDExOjUyOjM0KzAwOjAwh4HVcwAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyMi0wNS0yMFQxMTo1MjozNCswMDowMPbcbc8AAAAZdEVYdFNvZnR3YXJlAHd3dy5pbmtzY2FwZS5vcmeb7jwaAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4%2FIMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)](https://oblivious.ai) [![](https://img.shields.io/badge/-FastAPI-1D9385?style=for-the-badge&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAABVlBMVEUAAAAAkpIGmIwFmYoFmYsFmYsFmYsFmIsGmosAnYkHmo0FmYwFmYsFmosHmIoAjo4FmYoFmYsGmYsAn4AFmYsFmIoAmY8Fl40EmYsGm4sAlYoFmYsFmYsGmIoFmYsFmYsFmYsGmIoFmYoFmYsFmYsFmYsFmYsFmYsGmYoAlZUIlo8GmYwFmYsAkpIFmYsEmYsJl44GmY4AnoYFmYsGmIsFmYsFmooGmosFmYsGmYtOt60Vn5Kz4NyN0cqy39skppr3%2FPuc19Go29f%2F%2F%2F%2BHzsc6r6T%2B%2F%2F9zxr6%2B5eFevbRTua9KtasJm43W7uw0rKFtw7t9ysJpwrkcopUSnpHo9vXX7%2ByIz8hMtqwfpJf1%2B%2Fqk2tX9%2Fv42raJnwbjy%2Bvmh2dP6%2Ff32%2B%2FshpZgXoJOEzcYrqZ3p9vUTn5FBsadrw7pVurDY7%2B1qwrpQt66Ay8TB5uKS0804rqOQZtRSAAAAOHRSTlMADlmbyur6mlgNJp31nCUJjPuKCNPHGTHjLhjQzIHzlvRXmevp%2BfiYVQwih8YH4uUbLRXBhsiXVsnIqF0AAAFRSURBVHjaVdLTop1BDAXgdWyb27bXrtvUtm3j%2FS%2Fanh%2FJzHc7CGFGRsfGJyYnJ8anpmeg1OzcPNX8wiJ8S8sr9EyursGxuM7YkJGNTaitCapjjG3v6PsJquMnqLZ3EVjbozl5imZ%2FCUeWaU6fOUvHQVDfCs05OU%2FH4S6AOZoLF%2BUSXQlgZJ7mssgVupIzGKW5KiLX6ElhjOr6DRG5SU8a41S35L%2FbdwJ3GdpAhrF790U9uM5QFjnGHop5xEjeLjx%2BIuoy9YKFeCrq2XPGsprk9Rd3Ai9F5BXVBqboGb4WefOWqoBpet6JyHuaIkpJuj6IfPxElSwBC3R9FvlCMwVgcZKOr%2FLtOlWujP9W6fguP2gqOLK2QfPzF021hsBuner3H6pGE5GdbWfrVb0F1e5oo%2Bz%2FXThqB0l6ct0afLuJJFUyXYZSpVShl83lsr3%2BoAT1D8WptzmcHWvkAAAAAElFTkSuQmCC)](https://fastapi.tiangolo.com/)

<sup><sub>Need some help? Reach us at:</sub></sup> </br>
[![Slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)](https://oblivious-community.slack.com)

[**FastAPI**](https://fastapi.tiangolo.com/) is the hottest API framework for rapid and secure API development in Python. In this repo we provide tutorials and walkthroughs so that you can use FastAPI to build powerful multipart computation (MPC) applications. MPC is a class of protocol that enable multiple users to collaborate without directly seeing one anothers inputs. It traditionally relied on distributed encryption protocols like secret sharing or homomorphic encryption. While these are super cool technologies, they are also very low level and often extremely slow due to rounds of communication, network latency and bandwidth issues. However, over the last few years every major cloud provider have adopted secure enclaves (sometimes called confidential compute or trusted exectution environments). These are isolated VMs that prove to users what software and OS is running inside. You can use this proof to enable trust between clients connecting to a server. In this repo we'll get you up and started with secure enclaves using Oblivious and give you tons of examples of practical implementations with step-by-step tutorials of how to design and build them yourself.

### Table of Contents 📚
- [Enclaves for Multiparty Computation](#enclave-mpc)
  - [Governance](#governance)
  - [Collaboration](#collaboration)
  - [Query Privacy](#query-privacy)
- [MPC with FastAPI](#fastapi)
  - [General Principles](#principles)
  - [User Names & Roles](#users)
  - [Outbound Calls](#outbound)
  - [Unit Testing](#tests)
- [Creating a Service](#service)
- [Creating a Deployment](#deploy)
- [Example Applications](#example)
- [Awesome MPC with FastAPI & OBLV](#awesome)
- [Contributing & Code Structure](#contribute)
- [Disclaimer](#disclaimer)

<a name="enclave-mpc"/>

## Enclaves for Secure Multiparty Computation (MPC): 🤼

Secure multiparty computation is a long standing topic in computer security. It revolves around the challenge of having multiple "parties", ie servers and client computers, who collaborate to perform some form of computation in a collaborative manner. Right now you are probably reading this from the GitHub readme, so in a sense you are collaborating with one (or multiple) of GitHub's servers. Challenge is it's not secure, at least in the sense that you've no idea how GitHub is participating in this collaboration - are they logging your IP address? Selling your details to Evil Corp? Well, probably not - but you don't have any proof they aren't.

Secure multiparty computation (abrv to MPC or SMPC) is the class of cryptography that leverages advanced cryptographic protocols to gaurentee exactly what each party is doing in and interaction and typically that your inputs are kept confidential, only used for their intended purposes.

You may have heard of "hot" topics like Homomorphic Encryption, Secret Sharing and so on. The challenge with these are a few fold but to summarize they lack standards currently, they tend to be very slow to run and they operate at a very low level. 

An alternative approach is to use secure enclaves. These are isolated virtual machines that are now supported on every major cloud provider. They have extremely limitted IO and the infrastructure of the cloud [attests](https://docs.aws.amazon.com/enclaves/latest/user/set-up-attestation.html) the software that runs inside. 

[Oblivious (OBLV) ](https://oblivious.ai) provides a easy-to-use abstraction for you to leverage secure enclaves for multiparty computation, with a focus on data science applications. It's free to use (at least you get monthly free credits for a few hours worth of compute) and you can get started in seconds by signing up with your GitHub account [here](https://console.oblivious.ai).

<a name="governance"/>

### Governance: 🏛️

These enclaves applications can be pretty useful if you are looking to have an iron-clad history of how you've used data throughout its life cycle. Every connection to an enclave with OBLV requires client authentication and PCR hashes which prove what's running in the enclave. Whitelisting these can be used to limit how data is allowed to be processed.

<a name="collaboration"/>

### Collaboration: 🤝

By creating an enclave and proving what's running inside, you can broker trust between multiple clients. Each client who is connecting can validate the exact processing being performed and that there data can not be used outside of that context.

<a name="query-privacy"/>

### Query Privacy: 🙈

When you query a normal API, what happens to you data. Maybe you are using Google Translate on some important legal docs, what does Google do with that data. Can Google employees ever see that information? Hopefully not, but it can be near impossible to enforce. Leveraging enclaves you can offer and connect to enclaves with a gaurentee that no one will see the inputs or outputs of the queries being performed. 

<a name="fastapi"/>

## FastAPI with OBLV: :trophy:

When you start your enclave journey usually it involves a lot of pain, libraries suddenly don't work, you have to deal with virtual sockets, manage networks, systems, security engineering... it's a pain. That's where OBLV tries to help. It let's you write normal webservers in your favourite framework (eg FastAPI) and patches all the gaps so you can focus on the important stuff -> the application logic.

<a name="principles"/>

### General Principles:

We typically encourage the development of reusable (ideally open source) applications. The idea is that you build once and can deploy for many circumstances but the PCR code (used to establish trust) can be whitelisted as they'll be the same for each application. We do this by letting you define runtime args that get after the build phase and thus don't effect the PCR codes. These include specific user details or configuration relivent to _a_ particular deployment. So try build app with this in mind - how can I solve my problem in a reusable and generic fashion.

- Avoid hard coding user details
- Use runtime configuration to specify particular parameters that slightly modify behaviour or switch between cases.

<a name="users"/>

### User Names & User Roles:

When a user connects to your API, the proxy will put their user name in the `X-OBLV-User-Name` headed field and `X-OBLV-User-Role` of the request. FastAPI has a neat way to recieve these in your application like:

```python
@app.get(/)
def home(
    x_oblv_user_name: str = Header(default=None),
    x_oblv_user_role: str = Header(default=None)
):
  if x_oblv_user_name is None:
    raise HTTPException(401, "No X-OBLV-User-Name provided.")
  elif x_oblv_user_role is None:
    raise HTTPException(401, "No X-OBLV-User-Role provided.")
    
  pass
```

More details on the [FastAPI docs](https://fastapi.tiangolo.com/tutorial/header-params/).

<a name="outbound"/>

### Outbound Calls:

All outbound calls are blocked by default (to keep the data being processed secure and safe). However, you can you can whitelist url endpoints while configure the servive. This is fully-qualified domain name (FQDN) gets whitelisted, so basically `http://example.com` will allow `http://example.com/test` but not `http://test.example.com`. This is because the whitelisting is on the TCP layer, not the HTTP layer (so it doesn't break your TLS privacy).

<a name="tests"/>

### Unit Testing:

When unit testing in FastAPI remember to add the header fields (`X-OBLV-User-Name` and `X-OBLV-User-Role`) to simulate the behavious of the OBLV proxies. This can easily be done like this:

```python
from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

def test_example_accept():
    response = client.get("/", headers={"X-OBLV-User-Name": "Alice", "X-OBLV-User-Role": "Admin"})
    assert response.status_code == 200
    
def test_example_fail():
    response = client.get("/", headers={"X-OBLV-User-Name": "Not Alice", "X-OBLV-User-Role": "Admin"})
    assert response.status_code == 401
```

More details on the [FastAPI docs](https://fastapi.tiangolo.com/tutorial/testing/).


<a name="service"/>

## Configuring a Service: 🪛

<a name="deploy"/>

## Creating a Deployment: ⚙️


<a name="example"/>

## Example Application: 📖

This repository is actually a valid enclave service with OBLV. It uses FastAPI routes to host 4 simple applications which showcase some of the functionalities and hopefully inspires you to start building your own:

**Example 1:** [Hello World](/docs/hello.md)

**Example 2:** [Outbound Calls](/docs/outbound.md)

**Example 3:** [Yao's Millionaire Problem](/docs/hello.md)

**Example 4:** [Private Set Intersection](/docs/psi.md)

<a name="awesome"/>

## Awesome MPC with FastAPI & OBLV: 🙌

(Coming Soon! 🙌)

<a name="contribute"/>

## Contributing & Code Structure: 🧑‍💻

This repo was designed to be built upon, allowing great developers like you to help others get on board the OBLV enclave train. We highly encourage contributions on pull request.

<a name="disclaimer"/>

## Disclaimer: ⚠️

This is code is in Beta, please treat it as such.

