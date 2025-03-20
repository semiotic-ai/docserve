# docserve

## Task

This is a psuedo-coding exercise, your solution does not have to work or even run properly. Our goal is simply to see how you think. 

Your goal is to create an API Server for automating the documentation of GraphQL schemas. We have provided you with an entrypoint to do so in `docserve/docserve/main.py`. The setup instruction are below. 

Here are some goals: 

- [ ] The API should serve a selectable LLM model
- [ ] The API should ensure the user's schema is not corrupted
- [ ] The API should be constructed in a way that will enable the addition of new tools and features

Here are some thoughts: 

- [ ] How will we evaluate model performance? 
- [ ] How will we ensure the system is self improving? 
- [ ] What are we not thinking about that would be nice to have (whether in development or production)? 

## setup

Install the submodules. 

```bash
# Initialize and update submodules
git submodule update --init --recursive
```

### docker 

make sure you have [docker](https://www.docker.com/) up and running. 

### python

you will need python 3.13.0

```bash 
# install pyenv
brew install pyenv

# install python 3.13.0
pyenv install 3.13.0

# set the python version
pyenv local 3.13.0

# check the python version
python --version
```

### graphdoc and docserve

let's start!

```bash
# make the root run.sh executable 
chmod +x ./run.sh

# set up everything (hopefully)
./run.sh good-luck
```

## troubleshooting

maybe helpful for macos if you have issues with `python3` != `python`

```bash 
# export the pyenv path
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# reload the shell
source ~/.zshrc

# check the versions
python --version  # Should show 3.13.0
which python  # Should show ~/.pyenv/shims/python
```