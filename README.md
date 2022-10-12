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
