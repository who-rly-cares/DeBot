"""
put functions and classes here
#turn off word wrapp!!!
"""
import json


def PyDict__to__Json(a:dict):
    return json.dumps(a, indent=4);


#----------------------------------------------------------------------
class Professor:
    def __init__(self, id:int, fullname:str, fullname_farsi:str, majors_teaching:list):
        self.id = id
        self.fullname = fullname
        self.fullname_farsi = fullname_farsi
        self.majors_teaching = majors_teaching


    def __hash__(self):
        return hash(self.title)



    def return_as_dict(self)->str:
        out = {
        "id":self.id,
        "fullname":self.fullname,
        "fullname_farsi":self.fullname_farsi,
        "majors_teaching":self.majors_teaching,
        }
        return out
#================================================================================
class ProfessorsTag:
    def __init__(self, title:str, farsi_title:str, point:int, count:int, owner:Professor):
        self.title =title
        self.point = point
        self.count = count
        self.farsi_title = farsi_title
        self.owner = owner


    def __hash__(self):
        return hash(self.title)




    @classmethod
    def sub_class_decorator(cls, subclass):
        pass

    def return_as_dict(self)->str:
        out = {
        "title":self.title,
        "point":str(self.point),
        "count":str(self.count),
        "farsi_title":str(self.farsi_title)
        }
        return out
#===============ProfessorsTag Subclasses
class TestingProfessorTag(ProfessorsTag):
    def __init__(self, owner, count):
        title="A TESTING TAG"
        farsi_title="فارسی"
        point=+1
        ProfessorsTag.__init__(self, title, farsi_title, point, count, owner)

#================================================================================
class ProfessorProfile:
    def __init__(self, owner:Professor, tags:list):
        self.owner = owner
        self.tags = tags

    @staticmethod
    def return_ProfessorRatingData_instance_by_json(self):
        "pass"

    def return_tags_as_json(self):
        out = []
        for i1 in self.tags:
            out.append(i1.return_as_dict())
        return out.__str__()

    def return_as_json(self)->str:
        output = {
        "owner":self.owner.return_as_dict(),
        "tags":self.return_tags_as_json(),
        }
        return PyDict__to__Json(output)
#----------------------------------------------------------------------
#DATA BASE RELATED
def write_ProfessorProfile_to_db(a:ProfessorProfile):
    """
    this function accepts an instance of ProfessorRatingData
    and writes it in a standard form to the db
    """
def return_ProfessorProfile_from_db_by_professor_id(id)->ProfessorProfile:
    """
    this function will return an isntance of ProfessorRatingData from data base
    put data base related code here
    """



def GenralTest():
    test_professor = Professor(id=0, fullname="Reza", fullname_farsi="رضا", majors_teaching=["math"])
    test_profile = ProfessorProfile(owner=test_professor, tags=[TestingProfessorTag(test_professor, 0)])
    print(test_profile.return_as_json())




GenralTest()
