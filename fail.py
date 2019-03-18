def hello():
    raise Exception("Nope!")
    return "world!"

if __name__ == "__main__":
    print(hello())