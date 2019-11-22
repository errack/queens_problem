
import sqlalchemy as db

class DBManager():

    def __init__(self, config):
        engine = db.create_engine('sqlite:///solutions.db') #Create test.sqlite automatically
        self.conn = engine.connect()
        self.metadata = None
        self.__create_db()


    def __create_db(self):
        self.metadata = db.MetaData()
        self.solutions = db.Table('solutions', self.metadata,
              db.Column('n_solution', db.Integer()),
              db.Column('solution', db.String(255), nullable=False)
              )

    def insert_solution_by_n(self, element, n_solution):
        query = db.insert(self.solutions) 
        values_list = []
        [values_list.append({"n_solution": n_solution, "solution": str(x)}) 
         for x in element[0]]
        ResultProxy = self.conn.execute(query,values_list)