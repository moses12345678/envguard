from cli import parse_args
from logic import operation_logic

def main():
    args = parse_args()
    operation_logic(args)

if __name__ == "__main__":
    main()







