"""
    Description:

    Author:           {{cookiecutter.author_name}}
    Created:
"""
try:
    import sys

except ImportError as error:
    print(error)
    print(f"error.name: {error.name}")
    print(f"error.path: {error.path}")
    
def main():
    print("Hello, {{cookiecutter.author_name}}!")

if __name__ == "__main__":
    main()