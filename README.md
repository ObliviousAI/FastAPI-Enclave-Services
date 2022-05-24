# Where FastAPI becomes FastEnclaves: MPC in Minutes 🦹‍♀️ 🦸‍♂️ 👩‍🚀 

[![](https://img.shields.io/badge/-OBLV:_Made%20for%20Enclaves-93228f?style=for-the-badge&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAQAAADZc7J%2FAAAABGdBTUEAALGPC%2FxhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAAmJLR0QA%2F4ePzL8AAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAHdElNRQfmBRQLNCJ5TUB1AAACu0lEQVRIx42VTWhdVRDHf7mxJe%2BlTWqVSlKJbZCGIib1iSGLbCq4aKkQlJagATdulFKEQMStduHGEHCRViW6EVwJQhBCqaYgih8YkxQhUluhxGIDMU2TmPhe%2BnNx7n339eV9OHcxd2bO%2F3%2FnnJkzt4EKYiunOE43h9gHrPAHs3zNZMMq9cWjfuyGlWTDCbtqg7OOmbeW5B01Uw3e7g%2F%2BH5mxoxI855%2Fpmiu%2BYa8PibjfPof9xntpeNFcOfzRFP65T0qF55iTKcVtj5TCM34f%2FHc8LeIuB%2FzAb73mb172XZ%2BOSV72bkJx1WxKMBZ8S%2FaIeMrfd2x8Oo4943LiOp8WLq%2B6aZ%2BII6W7LZEtXxGx363gWLc9EHwS7GERB2sc%2F7ZnRHwrcVwEbAlts%2BADYrN%2F1azgigfEXV5Lctgb8TwZgPcoAEMcqNlqrbwG5BkNZpaT%2BJHqv%2B4XcapuF03HvRE37MWIHoCfWQYgRz1pBWCZmWD2RBwCuApAEw%2FXJViI9a9BHY5oAbgNwO66cPgw1rfihKKg7wHwD9aBX%2BBy%2FFaIdcQqwIMA5FmqAZb3OVu04s3eibgBkNyM%2Barwm5zgHNtF%2B2hQ1yNmAfpoAuBSFfg0TzFVYmfoDS9z%2BFIoaGjSxyxUqP2PZsqu9lASOoMtrqv%2BZCTiZxUIesvgkTNJK%2B8BnAjWqyJ2uFIG39gxWl5PQuPhdLtCX655TMSBsm0UbL4Pngsp65ptSYFGg%2BeWT4j4Yjp3Ss4nPN3pfX07rXBTMtL%2B9gURO%2F3UzSLBcBE%2B6GrinC8ZaeBBF5PIF%2FHwarbf0z5nZzH1%2B4bq4%2BV9lnMpjX%2FniP0%2BYqONttnvm0mKCbzStfWI83XHgercjq8XKbKeT464iqz5TtVfW0zS7oUqJOuOFwtXlIaKJHs5ybP00EkrsMINfuErvmxY27n2P7cF8FI7UOqVAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDIyLTA1LTIwVDExOjUyOjM0KzAwOjAwh4HVcwAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyMi0wNS0yMFQxMTo1MjozNCswMDowMPbcbc8AAAAZdEVYdFNvZnR3YXJlAHd3dy5pbmtzY2FwZS5vcmeb7jwaAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4%2FIMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)](https://oblivious.ai) [![](https://img.shields.io/badge/-FastAPI-1D9385?style=for-the-badge&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAABVlBMVEUAAAAAkpIGmIwFmYoFmYsFmYsFmYsFmIsGmosAnYkHmo0FmYwFmYsFmosHmIoAjo4FmYoFmYsGmYsAn4AFmYsFmIoAmY8Fl40EmYsGm4sAlYoFmYsFmYsGmIoFmYsFmYsFmYsGmIoFmYoFmYsFmYsFmYsFmYsFmYsGmYoAlZUIlo8GmYwFmYsAkpIFmYsEmYsJl44GmY4AnoYFmYsGmIsFmYsFmooGmosFmYsGmYtOt60Vn5Kz4NyN0cqy39skppr3%2FPuc19Go29f%2F%2F%2F%2BHzsc6r6T%2B%2F%2F9zxr6%2B5eFevbRTua9KtasJm43W7uw0rKFtw7t9ysJpwrkcopUSnpHo9vXX7%2ByIz8hMtqwfpJf1%2B%2Fqk2tX9%2Fv42raJnwbjy%2Bvmh2dP6%2Ff32%2B%2FshpZgXoJOEzcYrqZ3p9vUTn5FBsadrw7pVurDY7%2B1qwrpQt66Ay8TB5uKS0804rqOQZtRSAAAAOHRSTlMADlmbyur6mlgNJp31nCUJjPuKCNPHGTHjLhjQzIHzlvRXmevp%2BfiYVQwih8YH4uUbLRXBhsiXVsnIqF0AAAFRSURBVHjaVdLTop1BDAXgdWyb27bXrtvUtm3j%2FS%2Fanh%2FJzHc7CGFGRsfGJyYnJ8anpmeg1OzcPNX8wiJ8S8sr9EyursGxuM7YkJGNTaitCapjjG3v6PsJquMnqLZ3EVjbozl5imZ%2FCUeWaU6fOUvHQVDfCs05OU%2FH4S6AOZoLF%2BUSXQlgZJ7mssgVupIzGKW5KiLX6ElhjOr6DRG5SU8a41S35L%2FbdwJ3GdpAhrF790U9uM5QFjnGHop5xEjeLjx%2BIuoy9YKFeCrq2XPGsprk9Rd3Ai9F5BXVBqboGb4WefOWqoBpet6JyHuaIkpJuj6IfPxElSwBC3R9FvlCMwVgcZKOr%2FLtOlWujP9W6fguP2gqOLK2QfPzF021hsBuner3H6pGE5GdbWfrVb0F1e5oo%2Bz%2FXThqB0l6ct0afLuJJFUyXYZSpVShl83lsr3%2BoAT1D8WptzmcHWvkAAAAAElFTkSuQmCC)](https://fastapi.tiangolo.com/)

<sup><sub>Need some help? Reach us at:</sub></sup> </br>
[![Slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)](https://oblivious-community.slack.com)

[**FastAPI**](https://fastapi.tiangolo.com/) is the hottest API framework for rapid and secure API development in Python. In this repo we provide tutorials and walkthroughs so that you can use FastAPI to build powerful multipart computation (MPC) applications. MPC is a class of protocol that enable multiple users to collaborate without directly seeing one anothers inputs. It traditionally relied on distributed encryption protocols like secret sharing or homomorphic encryption. While these are super cool technologies, they are also very low level and often extremely slow due to rounds of communication, network latency and bandwidth issues. However, over the last few years every major cloud provider have adopted secure enclaves (sometimes called confidential compute or trusted exectution environments). These are isolated VMs that prove to users what software and OS is running inside. You can use this proof to enable trust between clients connecting to a server. In this repo we'll get you up and started with secure enclaves using Oblivious and give you tons of examples of practical implementations with step-by-step tutorials of how to design and build them yourself.

### Table of Contents 📚
- [Enclaves for Multiparty Computation](#enclave-mpc)
- [MPC with FastAPI](#fastapi)
  - [General Principles](#principles)
  - [User Names](#users)
  - [User Roles](#roles)
  - [Outbound Calls](#outbound)
  - [Unit Testing](#tests)
- [Creating a Service](#service)
- [Creating a Deployment](#deploy)
- [Awesome MPC with FastAPI & OBLV](#awesome)
- [Contributing & Code Structure](#contribute)
- [Disclaimer](#disclaimer)

<a name="enclave-mpc"/>

## Enclaves for Multiparty Computation:

<a name="fastapi"/>

## MPC with FastAPI:

<a name="principles"/>

### General Principles:

<a name="users"/>

### User Names:

`X-OBLV-User-Name`

<a name="roles"/>

### User Roles:

`X-OBLV-User-Role`

<a name="outbound"/>

### Outbound Calls:


<a name="testing"/>

### Unit Testing:


<a name="service"/>

## Creating a Service:

<a name="deploy"/>

## Creating a Deployment:


<a name="example"/>

## Example Application:

<a name="awesome"/>

## Awesome MPC with FastAPI & OBLV:

(Coming Soon! 🙌)

<a name="contribute"/>

## Contributing & Code Structure:

This repo was designed to be built upon, allowing great developers like you to add more differentially private synthetic data libraries as they become available. We highly encourage contributions on pull request.

<a name="disclaimer"/>

## Disclaimer:

This is code is in Beta, please treat it as such.

