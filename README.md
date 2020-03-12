# ImageProcessorAPI
CPSC 5200 Software Architecture and Design Individual Project - A simple image processor

**Activate virtual env**<br />
cd venv <br />
source bin/activate

**Start app.py**<br />
python3 app.py 

**Assignment Spec**

Given the following specification, design the overall architecture and APIs necessary to support this application. You will be responsible for submitting architectural models, API specifications (as interface definitions, swagger, or any other reasonable format such that a developer would be able to figure out how code against your product's API).<br />

The architecture should include:

* a high level overview of the full system
* a write-up describing any details that can't be presented in a diagram
* a discussion of how any components and connectors are built and deployed
* a discussion of any communication protocols needed
* sample code for calling your application (pick a language and show you have thought through the API usage)
* justification for your architecture
* the API specification from the client perspective
* any internal details necessary to explain how you might have implemented the service itself (ie. design patterns)

The specification
The application that we're creating is a simple image processor. The end user provides an image in some format (your API will need to take this into account somehow) and allows the user to perform combinations of the following operations:

* Flip horizontal and vertical
* Rotate +/- n degrees
* Convert to grayscale
* Resize
* Generate a thumbnail
* Rotate left
* Rotate right
