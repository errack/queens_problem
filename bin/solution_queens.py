from chess import Queens
import configuration
from manager_db.db_manager import DBManager

def main():
    run()

def get_solutions(size):
    queens = Queens(size)
    return queens.resolve()

def save_solution(config):
    return DBManager(config)

def run():
    config = configuration.load_config("config/config.yml")
    db = save_solution(config.get("", ""))
    solutions = get_solutions(config.get("sizeBoard", ""))
    _keys = solutions.keys()
    [db.insert_solution_by_n(solutions[x], x) for x in _keys
     if len(solutions[x]) > 0]

if __name__ == '__main__':
    main()