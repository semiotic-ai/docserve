# Task

This is a psuedo-coding exercise, your solution does not have to work or even run properly. Our goal is simply to see how you think. 

Your goal is to create an API Server for automating the documentation of GraphQL schemas. `main.py` is intended purely to help you get started, feel free to use any implementation approach as you see fit. The `config.json` and `example.graphql` are simply reference materials, you are not required to use them. 

Here are some assumptions: 

- [ ] You can assume that a function name properly completes it's implied goal (i.e. validate_user_schema(gold, pred))
- [ ] You can assume that you have a working prompt for a given goal (i.e. system_prompt)

Here are some goals: 

- [ ] The API should serve a selectable LLM model
- [ ] The API should ensure the user's schema is not corrupted
- [ ] The API should be constructed in a way that will enable the addition of new tools and features

Here are some thoughts: 

- [ ] How will we evaluate model performance? 
- [ ] How will we ensure the system is self improving? 
- [ ] What are we not thinking about that would be nice to have (whether in development or production)? 