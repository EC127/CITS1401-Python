def main(csvfile):
    with open(csvfile) as f:
        content = []
        line = f.readline()
        while line:
            content.append(line)
            line = f.readline()
        print(content)
    
    
            