"""
    Description:

    Author:           {{cookiecutter.author_name}}
    Created:
"""
try:
    import sys
    from setups.s01 import main as s01

except ImportError as error:
    print(error)
    print(f"error.name: {error.name}")
    print(f"error.path: {error.path}")

def main():
    ## s01
    print("Rodando Script s01.py")
    s01()

if __name__ == "__main__":
    main()