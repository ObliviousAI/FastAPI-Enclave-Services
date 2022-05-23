# Where FastAPI becomes FastEnclaves: MPC in Minutes 🦹‍♀️ 🦸‍♂️ 👩‍🚀 

[![](https://img.shields.io/badge/-OBLV:_Made%20for%20Enclaves-93228f?style=for-the-badge&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAQAAADZc7J%2FAAAABGdBTUEAALGPC%2FxhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAAmJLR0QA%2F4ePzL8AAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAHdElNRQfmBRQLNCJ5TUB1AAACu0lEQVRIx42VTWhdVRDHf7mxJe%2BlTWqVSlKJbZCGIib1iSGLbCq4aKkQlJagATdulFKEQMStduHGEHCRViW6EVwJQhBCqaYgih8YkxQhUluhxGIDMU2TmPhe%2BnNx7n339eV9OHcxd2bO%2F3%2FnnJkzt4EKYiunOE43h9gHrPAHs3zNZMMq9cWjfuyGlWTDCbtqg7OOmbeW5B01Uw3e7g%2F%2BH5mxoxI855%2Fpmiu%2BYa8PibjfPof9xntpeNFcOfzRFP65T0qF55iTKcVtj5TCM34f%2FHc8LeIuB%2FzAb73mb172XZ%2BOSV72bkJx1WxKMBZ8S%2FaIeMrfd2x8Oo4943LiOp8WLq%2B6aZ%2BII6W7LZEtXxGx363gWLc9EHwS7GERB2sc%2F7ZnRHwrcVwEbAlts%2BADYrN%2F1azgigfEXV5Lctgb8TwZgPcoAEMcqNlqrbwG5BkNZpaT%2BJHqv%2B4XcapuF03HvRE37MWIHoCfWQYgRz1pBWCZmWD2RBwCuApAEw%2FXJViI9a9BHY5oAbgNwO66cPgw1rfihKKg7wHwD9aBX%2BBy%2FFaIdcQqwIMA5FmqAZb3OVu04s3eibgBkNyM%2Barwm5zgHNtF%2B2hQ1yNmAfpoAuBSFfg0TzFVYmfoDS9z%2BFIoaGjSxyxUqP2PZsqu9lASOoMtrqv%2BZCTiZxUIesvgkTNJK%2B8BnAjWqyJ2uFIG39gxWl5PQuPhdLtCX655TMSBsm0UbL4Pngsp65ptSYFGg%2BeWT4j4Yjp3Ss4nPN3pfX07rXBTMtL%2B9gURO%2F3UzSLBcBE%2B6GrinC8ZaeBBF5PIF%2FHwarbf0z5nZzH1%2B4bq4%2BV9lnMpjX%2FniP0%2BYqONttnvm0mKCbzStfWI83XHgercjq8XKbKeT464iqz5TtVfW0zS7oUqJOuOFwtXlIaKJHs5ybP00EkrsMINfuErvmxY27n2P7cF8FI7UOqVAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDIyLTA1LTIwVDExOjUyOjM0KzAwOjAwh4HVcwAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyMi0wNS0yMFQxMTo1MjozNCswMDowMPbcbc8AAAAZdEVYdFNvZnR3YXJlAHd3dy5pbmtzY2FwZS5vcmeb7jwaAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4%2FIMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)](https://oblivious.ai) [![](https://img.shields.io/badge/-FastAPI-1D9385?style=for-the-badge&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAABVlBMVEUAAAAAkpIGmIwFmYoFmYsFmYsFmYsFmIsGmosAnYkHmo0FmYwFmYsFmosHmIoAjo4FmYoFmYsGmYsAn4AFmYsFmIoAmY8Fl40EmYsGm4sAlYoFmYsFmYsGmIoFmYsFmYsFmYsGmIoFmYoFmYsFmYsFmYsFmYsFmYsGmYoAlZUIlo8GmYwFmYsAkpIFmYsEmYsJl44GmY4AnoYFmYsGmIsFmYsFmooGmosFmYsGmYtOt60Vn5Kz4NyN0cqy39skppr3%2FPuc19Go29f%2F%2F%2F%2BHzsc6r6T%2B%2F%2F9zxr6%2B5eFevbRTua9KtasJm43W7uw0rKFtw7t9ysJpwrkcopUSnpHo9vXX7%2ByIz8hMtqwfpJf1%2B%2Fqk2tX9%2Fv42raJnwbjy%2Bvmh2dP6%2Ff32%2B%2FshpZgXoJOEzcYrqZ3p9vUTn5FBsadrw7pVurDY7%2B1qwrpQt66Ay8TB5uKS0804rqOQZtRSAAAAOHRSTlMADlmbyur6mlgNJp31nCUJjPuKCNPHGTHjLhjQzIHzlvRXmevp%2BfiYVQwih8YH4uUbLRXBhsiXVsnIqF0AAAFRSURBVHjaVdLTop1BDAXgdWyb27bXrtvUtm3j%2FS%2Fanh%2FJzHc7CGFGRsfGJyYnJ8anpmeg1OzcPNX8wiJ8S8sr9EyursGxuM7YkJGNTaitCapjjG3v6PsJquMnqLZ3EVjbozl5imZ%2FCUeWaU6fOUvHQVDfCs05OU%2FH4S6AOZoLF%2BUSXQlgZJ7mssgVupIzGKW5KiLX6ElhjOr6DRG5SU8a41S35L%2FbdwJ3GdpAhrF790U9uM5QFjnGHop5xEjeLjx%2BIuoy9YKFeCrq2XPGsprk9Rd3Ai9F5BXVBqboGb4WefOWqoBpet6JyHuaIkpJuj6IfPxElSwBC3R9FvlCMwVgcZKOr%2FLtOlWujP9W6fguP2gqOLK2QfPzF021hsBuner3H6pGE5GdbWfrVb0F1e5oo%2Bz%2FXThqB0l6ct0afLuJJFUyXYZSpVShl83lsr3%2BoAT1D8WptzmcHWvkAAAAAElFTkSuQmCC)](https://fastapi.tiangolo.com/)

<sup><sub>Need some help? Reach us at:</sub></sup> </br>
[![Slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)](https://oblivious-community.slack.com)

**FastAPI** is the hottest API framework for rapid and secure API development in Python. In this repo we provide tutorials and walkthroughs so that you can use FastAPI to build powerful multipart computation (MPC) applications. MPC is a class of protocol that enable multiple users to collaborate without directly seeing one anothers inputs. It traditionally relied on distributed encryption protocols like secret sharing or homomorphic encryption. While these are super cool technologies, they are also very low level and often extremely slow due to rounds of communication, network latency and bandwidth issues. However, over the last few years every major cloud provider have adopted secure enclaves (sometimes called confidential compute or trusted exectution environments). These are isolated VMs that prove to users what software and OS is running inside. You can use this proof to enable trust between clients connecting to a server. In this repo we'll get you up and started with secure enclaves using Oblivious and give you tons of examples of practical implementations with step-by-step tutorials of how to design and build them yourself.

### Table of Contents 📚
- [Quick Start Guide](#Quick-Start)
  - [Client's Key Generation & Sharing](#Key-Gen)
  - [Launch the Enclave](#Launch)
  - [Clients Connect](#Connect)
- [Dependancies](#Dependancies)
- [An Overview of DP Synthetic Data](#Overview)
- [Enclaves for Multiparty Computation](#EnclaveMPC)
- [Contributing & Code Structure](#Contribute)
- [Disclaimer](#Disclaimer)

TODO: This is just a template from the Synthetic Data service:

<a name="Quick-Start"/>

## Quick Start Guide:

👀 Watch the YouTube tutorial to deploy this service to an enclave now (for FREE!), click below:

[![Get Start with Oblivious Youtube](https://img.youtube.com/vi/P3pTY3jC258/0.jpg)](https://www.youtube.com/watch?v=P3pTY3jC258)

<a name="Key-Gen"/>

### 1. Client's Key Generation & Sharing 🔑

The two clients of the service need to download the Oblivious secure proxy from [here](https://docs.oblivious.ai/cli/binaries) for their respective devices (Windows, Mac & Linux supported). Once downloaded they can open a terminal and create a public key using the key generate (based on OpenSSL) like so:

```
$ cd <name-of-downloaded folder>/keygen
$ ./oblv_keygen_gnu_mac <prefered_key_name>
Generated private key in location:
/home/oblivious/<prefered_key_name>_private.der
Generated public key in location:
/home/oblivious/<prefered_key_name>_public.der
Public key in base64 format:
MIIBCgKCAQEAyFsL4ElhKSuCo5LEDttgm9y+AajR+/LIqMhxeE2N/ZLKTQERRIIdgFkAFD+lqgq+SK1dP2gCmg++FQUm39Xm0AHrcLoigwKwllPak/n9VGVLff7GG0ZMazg7K9zdhIot7Xf/RHOVlZLymZmLI5vrmNcvKYYwfBKejKuxsTpcW5nNPlhauQIjc1SvvU9leXH+segiATrU/ktR3jPsGcAWa3Cm6dXoHA39kkIpNJE2UWfYT8jVAhhJId5rm4o6gOIg+VOeSPBSjGLLF5F/7+EMEVt6sWBKQPWwK4w2KY//6Nw2i8+q6VbW/RC/a9JItLEBtDS+K9IztxTsJfkWE4ksgQIDAQAB 
```

They can now copy the base64 key (starting with `MIIB...` and ending with `...AQAB` in the previous example) and share it with the person launching the enclave. 

<a name="Launch"/>

### 2. Launch the Enclave 🚀

To get started, head over to [Oblivious](https://oblivious.ai) and sign up/sign in to the console.

Once logged in, you will see on the left-hand menu a "Services" tab. Clicking on it will take you to the services you have created and those developed by the Oblivious team (this is one of them).

Hit the ▶️ button next to "synthetic-data-service" and you'll be presented with a form that looks like this:

(add image...)

Add the clients' names and public keys, and select a enclave server with enough memory that you'd require (at least 8GB for everything to run smoothly).

It can take a few mins for your enclave to come online as a full CFT is created just for you, including load balancer, NAT, well-engineered architecture. Once it is live though, you will find it in you "Deployments" tab. Simply click on the deployment and you will get the connection string to share with your clients. The URL and public/private keys will change, but the PCR codes will look like:

```
$ ./oblv connect \
--pcr0 2f1123456789518cec817daa741547d049d6150d73b05492eeb0337da35c3a43b7e05ec64dc2252c4f73e783a19c6aed \
--pcr1 5c01976a1234567890353189afd3bf5fe29df96328887111e7c802cf2ff5ad636deed2ab8254e7a51a45fca01d0ae062 \
--pcr2 84c493eaabfd6ec623123456789e56f203fc2925a5873b2b387cbc854842bacab9ddf7f9e12d2df82f3a903b62291ee \
--private-key "oblv_private.der" \
--public-key "oblv_public.der" \
--url https://example.oblivious.ai/ \
--port 443 \
--lport 3030
```

<a name="Connect"/>

### 3. Clients Connect 🔌

To connect to the enclave, go back to your downloded oblvious proxy folder and run the proxy to connect to the aforementioned enclave:

```
$ cd <name-of-downloaded folder>/bin
$ ./oblv connect \
--pcr0 2f1123456789518cec817daa741547d049d6150d73b05492eeb0337da35c3a43b7e05ec64dc2252c4f73e783a19c6aed \
--pcr1 5c01976a1234567890353189afd3bf5fe29df96328887111e7c802cf2ff5ad636deed2ab8254e7a51a45fca01d0ae062 \
--pcr2 84c493eaabfd6ec623123456789e56f203fc2925a5873b2b387cbc854842bacab9ddf7f9e12d2df82f3a903b62291ee \
--private-key "oblv_private.der" \
--public-key "oblv_public.der" \
--url https://example.oblivious.ai/ \
--port 443 \
--lport 3030
```

The connection will only be made if the source code with the above PCR code is running inside the enclave. Once a connection is made, all payloads (ie the bode of the POST requests) to the enclave will be end-to-end encrypted, so not even the person who set up the enclave will see what data you are uploading. To send taffic from your computer, simply send it to the port specified by the `--lport` flag (in the above example it would be 3030).

🚨 *Important:* Make sure the PCR codes are the same as those above. This will gaurentee that you are connecting to the service unmodified.

<a name="Dependancies"/>

## Dependancies:

To run this as an enclave service to broker multiparty computation, you need to register for [Oblivious](https://oblivious.ai) using either an email/password or your GitHub login. 

<a name="Overview"/>

## An Overview of DP Synthetic Data:

(Coming soon...)

<a name="EnclaveMPC"/>

## Enclaves for Multiparty Computation:

Yes, yes, of course we are giving you another YouTube video as an explainer:

[![Enclaves with Oblivious Youtube](https://img.youtube.com/vi/9Z9FqtIr6go/0.jpg)](https://www.youtube.com/watch?v=9Z9FqtIr6go)

For more information, check out the docs [here](https://docs.oblivious.ai/).

<a name="Contribute"/>

## Contributing & Code Structure:

This repo was designed to be built upon, allowing great developers like you to add more differentially private synthetic data libraries as they become available. We highly encourage contributions on pull request.

To add a new differentially private synthetic data model, follow the guide [here](). <-- TODO

<a name="Disclaimer"/>

## Disclaimer:

This is code is in Beta, please treat it as such.

