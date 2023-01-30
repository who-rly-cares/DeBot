"""
put functions and classes here
#turn off word wrapp!!!
"""

def PyDict__to__Json(a:dict):
    return a.__str__().reaplce("\'","\"");


#----------------------------------------------------------------------
class Professor:
    def __init__(self, id:int, fullname:str, majors_teaching:list):
        self.id = id
        self.fullname = fullname
        self.majors_teaching = majors_teaching
    def __hash__(self):
        return hash(self.title)

    def return_as_json(self)->str:
        pass 
#----------------------------------------------------------------------
class ProfessorsTag:
    def __init__(self, title:str, point:int, count:int, owner:Professor):
        self.title = title
        self.point = point
        self.count = count

    def __hash__(self):
        return hash(self.title)


    def __setattr__(self, attrname, value):
        ReadOnly = ["title", "point"]
        if attrname in ReadOnly:
            return None
        else:
            try:
                return self.__dict__["attrname"]
            except Exception as er:
                return er

    @classmethod
    def sub_class_decorator(cls, subclass):
        pass

    def return_as_json(self)->str:
        pass 
        
        
#----------------------------------------------------------------------
class ProfessorRatingData:
    def __init__(self, owner:Professor, tags:list):
        self.owner = owner
        self.tags = tags

    @staticmethod
    def return_ProfessorRatingData_instance_by_json(self):
        "pass"

    def return_as_json(self)->str:
        output = {
        "owner":self.owner.return_as_json(),
        "tags":self.return_tags_as_json(),
        }
        return str
#----------------------------------------------------------------------
#DATA BASE RELATED
def write_ProfessorRatingData_to_db(a:ProfessorRatingData):
    """
    this function accepts an instance of ProfessorRatingData
    and writes it in a standard form to the db
    """
def return_ProfessorRatingData_from_db_by_professor_id(id):
    """
    this function will return an isntance of ProfessorRatingData from data base
    put data base related code here
    """
