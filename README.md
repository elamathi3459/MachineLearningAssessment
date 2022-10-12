# MachineLearningAssessment

### Input
Input is the corner points and it can be given in any order. But it only takes the rectangular points as input. Followed by Total nuber of rows and columns.

[(1.5, 1.5),(4.0, 1.5),(1.5, 8.0),(4.0, 8.0)]

2

3

Tech stack Used:
Front end: HTML 
Back end: Python


### Data Flow:

1. Here the given input is taken from the user end. The given co-ordinates are taken from the POST method API.
2. All the calculations and logic flows are written in the python. 
3. Finally the web based application is containarized in the docker. 

### Output

[[[1.5, 8.0], [2.8, 8.0], [4.0, 8.0]]

[[1.5, 1.5], [2.8, 1.5], [4.0, 1.5]]]

## Test case1
### Input
[(1.5, 1.5),(4.0, 3.0),(1.5, 8.0),(4.0, 8.0)]

2

3
### Output

Error in the Points


### Steps to Run the code

step 1: Open command Prompt and type docker to check whether docker is installed in your system or not. And then follow the below steps.

Go to Basic directory structure
Our application directory structure will look like this:

python-docker
├── app.py
├── Dockerfile
├── requirements.txt

step 2: Now, we can build our image. Using docker build, we can now enlist Docker's help in building the image. You can combine the build command with other tags, such as the "-t" flag, to specify the image name.

>> docker build -t <new-image-name> . 

For example, If I take my image name as flaskapp, then the command becomes

>> docker build -t flaskapp:latest .

Step 3: Run an image as container

Running an image inside a container is as simple as building one. But before we do so, we'd like to see what other images are available in our environment. To view images from the command line, execute the following:

>> docker images

Using the docker run command, we can run an image by passing the image's name as a parameter.

>> docker run

If you run the above command, you'll notice that on the command line it indicates that the application is running. But when you enter http://localhost:5000/ on the browser, the greeting will be:

This site can’t be reached localhost refused to connect.

Regardless of whether the container is running, it is doing so in isolation mode and cannot connect to localhost:5000.

Solution for the above problem is to run the image in the detached mode.

>> docker run -d -p 5000:5000 python-docker

Because we need to view this application in the browser rather than the container, we'll modify our docker run and add two additional tags: "-d" to run it in detached mode and "-p" to specify the port to be exposed.

step 4: We can use the following command to see which containers are currently running:

>> docker ps

step 5: To stop the currently running container,

>> docker stop <container-name>

For Example: Your container-name is the container ID. You can get this if you run >> docker ps 

Other useful command for removing unused resources, freeing up space and keeping your system clean.

>> docker container prune

References:

1. https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/


