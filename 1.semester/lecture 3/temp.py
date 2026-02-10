def read_file(name:str)->str:
    """Reads a file called 'name'. Returns a string."""
    with open(name) as f:
        return f.read()
    
print(read_file("supplementary/25ZS/poem.txt"))