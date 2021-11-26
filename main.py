from app import current_location
from app import create_basic_config

def main():
    create_basic_config(current_location, force=False)
    

if __name__ == '__main__':
    main()