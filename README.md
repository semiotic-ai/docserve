# Task

This is a psuedo-coding exercise, your solution does not have to work or even run properly. Our goal is simply to see how you think. 

Your goal is to create an API Server for automating the documentation of GraphQL schemas. See `main.py` as your starting point. Feel free to use any implementation approach as you see fit. You may utilize any external package. You can modify any file, unless otherwise specified. 

Here are some assumptions: 

- [ ] You can assume that a function name properly completes it's implied goal (i.e. validate_user_schema(gold, pred))
- [ ] You can assume that your prompts work for a given goal (don't worry about "prompt engineering")

Here are some goals: 

- [ ] The API should serve a selectable LLM model
- [ ] The API should ensure the user's schema is not corrupted
- [ ] Please consider how you would hanlde adding new tools and features in the future

Here are some thoughts: 

- [ ] How will we evaluate model performance? 
- [ ] How will we ensure the system is self improving? 
- [ ] What are we not thinking about that would be nice to have (whether in development or production)? 