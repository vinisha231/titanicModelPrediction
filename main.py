import os 
import struct  
def load_data(train, limit=10):
    train_file_path = "train.csv"
    with open(train_file_path, 'r') as file:
        for i in range(limit):
            line = file.readline()  # Read one line at a time
            print(line.strip())
    print(line)

def main():
    load_data("train.csv")

if __name__ == "__main__":
    main()
