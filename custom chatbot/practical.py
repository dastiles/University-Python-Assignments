
import uuid
import random

from numpy import average

student_data_records = []
marks = []

for i in range(100):
    marks.append(random.randint(10,95))
    
print(uuid.uuid4())


modules = ['module 1', 'module 2', 'module 3', 'module 4', 'module 5', 'module 6', 'module 7']
programmes = ['programme 1', 'programme 2', 'programme 3', 'programme 4', 'programme 5', 'programme 6', 'programme 7']

def store_student_data(module_name: str, practical_assignments: list,prac_assign_theory: int,practical_test: list,mini_proj: int, theory_assignments: list,theory_tests:list,theo_mini_proj: int, theo_exam_mark: int, prac_exam_mark: int) -> dict:
    return{
        "module" :{"module_name": module_name, "marks": {
            "practical_module_marks":{
                "practical_assignments":practical_assignments,
                "practical_assign_theory":prac_assign_theory,
                "practical_test":practical_test,
                "practical_mini_proj":mini_proj,
                "exam_mark":prac_exam_mark,
                "overall_practical_mark":0,
            }
            ,"theory_module_marks":{
                "theory_assignments":theory_assignments,
                "theory_tests":theory_tests,
                "theo_mini_proj":theo_mini_proj,
                "exam_mark":theo_exam_mark,
                "overall_theory_mark":0,
                
            }
        },
                "overall_module_mark":0,
                
        }
    }
    

    
def modules_seven():
    student_mark_modules = []
    for module in modules:
        student_mark_modules.append(store_student_data(
            module_name= module,
            practical_assignments= random.choices(marks,k = 3),
            prac_assign_theory= random.choice(marks),
            practical_test=random.choices(marks,k=2),
            mini_proj=random.choice(marks),
            theory_assignments=random.choices(marks,k=2),
            theo_mini_proj=random.choice(marks),
            theory_tests=random.choices(marks,k=2),
            theo_exam_mark=random.choice(marks),
            prac_exam_mark=random.choice(marks),
        ))
    return student_mark_modules
  
def students_record(modules: list) -> list:
    student_record = {}    
    student_id = uuid.uuid4()        
    student_record['programme'] = random.choice(programmes)
    student_record['reg_numner'] = str(student_id)[:8]
    student_record['modules'] = modules
    student_record['semester_overall_mark'] = 0
    
    
    return student_record
   
# input data for 100 students
for student in range(3):
    student_data_records.append(students_record(modules_seven()))   
    
# print(student_data_records)

for i in student_data_records:
    
    for module in i['modules']:
        marks = module['module']['marks']
        practical_marks = marks['practical_module_marks']
        average_practical_mark = average(practical_marks['practical_assignments']) * 0.155  
        mini_project_marks_practical = practical_marks['practical_mini_proj'] * 0.205 
        practical_exam = practical_marks['exam_mark'] * 0.5
        overall_practical_mark= ((sum(practical_marks['practical_test']) + practical_marks['practical_assign_theory'])// 2) *0.14
        
        practical_marks['overall_practical_mark'] = sum([mini_project_marks_practical,practical_exam, average_practical_mark, overall_practical_mark])
        
        theory_marks = marks['theory_module_marks']
         
        mini_project_marks_theory = theory_marks['theo_mini_proj'] * 0.2 
        theory_exam = theory_marks['exam_mark'] * 0.6
        average_theory_mark= ((sum(theory_marks['theory_assignments']) + sum(theory_marks['theory_tests']))// 2) *0.2
        theory_marks['overall_theory_mark'] = sum([mini_project_marks_theory, theory_exam,average_theory_mark])
        # print(practical_marks['overall_practical_mark'] )
        # print(theory_marks['overall_theory_mark'] )
        module['module']['overall_module_mark'] = (practical_marks['overall_practical_mark'] + theory_marks['overall_theory_mark'])
        i['semester_overall_mark'] = i['semester_overall_mark'] + module['module']['overall_module_mark']
        
        
    # print(i['semester_overall_mark'] / 7)
    
print(student_data_records)

for i in student_data_records:
    print(i['programme'], i['reg_numner'],)