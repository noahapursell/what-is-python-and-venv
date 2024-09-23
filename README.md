# Intro to Python + venv
By: Noah Pursell & OUAI

## What is Python / Venv?
[Powerpoint](https://docs.google.com/presentation/d/1cNOBa9t9LPkleax8VRlOglnpo0f4VCdzyyu9hxR3Fxc/edit?usp=sharing)

## Creating venv Example
1. In terminal, navigate to project directory
2. Run the following command to create a virtual environment (you can use a different environment name): `python -m venv project1_env`
3. Activate the virtual environment:
    - Windows: run `project1_env\Scripts\Activate` (your command will be different if you had a different venv name)
    - max/Linux: run `project1_env/bin/activate` (your command will be different if you had a different venv name)
4. Install packages. For example, `pip install numpy`
5. When done, deactivate environment with `deactivate`

## Sharing Environment
### Save environment to a `requirements.txt`
1. Activate your virtual environment
2. Run the following command: `pip freeze > requirements.txt`. This will save a list of all the packages in your current environment, as well as their version numbers, to a file called `requirements.txt`. Look at the `requirements.txt` file in this repository as an example.

After creating this requirements file, you can share it with other people/computers. They can then use it to create their own environment with the same packages as yours.

### Loading an environment from a `requirements.txt` file
1. Create a new virtual environment and activate it
2. Run the following command: `pip install -r requirements.txt`. This will install the list of packages from the `requirements.txt` file into your local environment. 