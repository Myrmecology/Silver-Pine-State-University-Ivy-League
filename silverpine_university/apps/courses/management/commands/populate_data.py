from django.core.management.base import BaseCommand
from apps.courses.models import Department, Professor, Course, CourseSection
from apps.students.models import Student
from apps.calendar.models import Semester, AcademicEvent, UniversityHoliday
from apps.financial_aid.models import FinancialAccount, FinancialAidPackage, Scholarship
from datetime import datetime, date, time
import random


class Command(BaseCommand):
    help = 'Populate database with sample data for Silver Pine State University'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting data population...')
        
        # Create Departments
        self.create_departments()
        
        # Create Professors
        self.create_professors()
        
        # Create 80+ Courses
        self.create_courses()
        
        # Create Course Sections
        self.create_course_sections()
        
        # Create Sample Students
        self.create_students()
        
        # Create Semesters
        self.create_semesters()
        
        # Create Academic Events
        self.create_academic_events()
        
        # Create Holidays
        self.create_holidays()
        
        # Create Scholarships
        self.create_scholarships()
        
        self.stdout.write(self.style.SUCCESS('Data population completed successfully!'))

    def create_departments(self):
        departments_data = [
            ('CSCI', 'Computer Science', 'Hamilton Hall', '(555) 234-5678', 'csci@silverpine.edu'),
            ('MATH', 'Mathematics', 'Euler Building', '(555) 234-5679', 'math@silverpine.edu'),
            ('ENG', 'English Literature', 'Wordsworth Hall', '(555) 234-5680', 'english@silverpine.edu'),
            ('HIST', 'History', 'Roosevelt Building', '(555) 234-5681', 'history@silverpine.edu'),
            ('BIOL', 'Biology', 'Darwin Science Center', '(555) 234-5682', 'biology@silverpine.edu'),
            ('CHEM', 'Chemistry', 'Curie Laboratory', '(555) 234-5683', 'chemistry@silverpine.edu'),
            ('PHYS', 'Physics', 'Newton Hall', '(555) 234-5684', 'physics@silverpine.edu'),
            ('ECON', 'Economics', 'Smith Business Hall', '(555) 234-5685', 'economics@silverpine.edu'),
            ('PSYC', 'Psychology', 'Freud Center', '(555) 234-5686', 'psychology@silverpine.edu'),
            ('PHIL', 'Philosophy', 'Socrates Hall', '(555) 234-5687', 'philosophy@silverpine.edu'),
            ('ART', 'Fine Arts', 'Picasso Arts Center', '(555) 234-5688', 'art@silverpine.edu'),
            ('MUS', 'Music', 'Mozart Conservatory', '(555) 234-5689', 'music@silverpine.edu'),
            ('POLS', 'Political Science', 'Jefferson Hall', '(555) 234-5690', 'polisci@silverpine.edu'),
        ]
        
        for code, name, building, phone, email in departments_data:
            Department.objects.get_or_create(
                code=code,
                defaults={
                    'name': name,
                    'description': f'The {name} department at Silver Pine State University offers comprehensive programs.',
                    'building': building,
                    'phone': phone,
                    'email': email
                }
            )
        
        self.stdout.write('Created departments')

    def create_professors(self):
        professors_data = [
            # Computer Science
            ('PROF001', 'Sarah', 'Mitchell', 'Professor', 'CSCI', 'Hamilton Hall 301', 'Mon/Wed 2-4pm'),
            ('PROF002', 'James', 'Anderson', 'Associate Professor', 'CSCI', 'Hamilton Hall 305', 'Tue/Thu 10-12pm'),
            ('PROF003', 'Emily', 'Chen', 'Assistant Professor', 'CSCI', 'Hamilton Hall 310', 'Mon/Fri 1-3pm'),
            
            # Mathematics
            ('PROF004', 'Robert', 'Williams', 'Professor', 'MATH', 'Euler Building 201', 'Wed/Fri 3-5pm'),
            ('PROF005', 'Maria', 'Garcia', 'Associate Professor', 'MATH', 'Euler Building 205', 'Tue/Thu 1-3pm'),
            
            # English
            ('PROF006', 'David', 'Thompson', 'Professor', 'ENG', 'Wordsworth Hall 101', 'Mon/Wed 10-12pm'),
            ('PROF007', 'Jennifer', 'Davis', 'Associate Professor', 'ENG', 'Wordsworth Hall 105', 'Tue/Thu 2-4pm'),
            
            # History
            ('PROF008', 'Michael', 'Brown', 'Professor', 'HIST', 'Roosevelt Building 201', 'Mon/Wed 1-3pm'),
            ('PROF009', 'Lisa', 'Wilson', 'Assistant Professor', 'HIST', 'Roosevelt Building 210', 'Tue/Thu 11-1pm'),
            
            # Biology
            ('PROF010', 'Thomas', 'Martinez', 'Professor', 'BIOL', 'Darwin Science Center 301', 'Wed/Fri 10-12pm'),
            ('PROF011', 'Amanda', 'Taylor', 'Associate Professor', 'BIOL', 'Darwin Science Center 305', 'Mon/Wed 2-4pm'),
            
            # Chemistry
            ('PROF012', 'Christopher', 'Lee', 'Professor', 'CHEM', 'Curie Laboratory 401', 'Tue/Thu 1-3pm'),
            ('PROF013', 'Jessica', 'White', 'Assistant Professor', 'CHEM', 'Curie Laboratory 405', 'Mon/Fri 3-5pm'),
            
            # Physics
            ('PROF014', 'Daniel', 'Harris', 'Professor', 'PHYS', 'Newton Hall 501', 'Mon/Wed 10-12pm'),
            ('PROF015', 'Rachel', 'Clark', 'Associate Professor', 'PHYS', 'Newton Hall 505', 'Tue/Thu 2-4pm'),
            
            # Economics
            ('PROF016', 'Steven', 'Lewis', 'Professor', 'ECON', 'Smith Business Hall 601', 'Wed/Fri 1-3pm'),
            ('PROF017', 'Nicole', 'Walker', 'Assistant Professor', 'ECON', 'Smith Business Hall 605', 'Mon/Wed 11-1pm'),
            
            # Psychology
            ('PROF018', 'Kenneth', 'Hall', 'Professor', 'PSYC', 'Freud Center 201', 'Tue/Thu 10-12pm'),
            ('PROF019', 'Michelle', 'Young', 'Associate Professor', 'PSYC', 'Freud Center 205', 'Mon/Fri 2-4pm'),
            
            # Philosophy
            ('PROF020', 'Brian', 'Allen', 'Professor', 'PHIL', 'Socrates Hall 301', 'Wed/Fri 11-1pm'),
        ]
        
        for prof_id, fname, lname, title, dept_code, office, hours in professors_data:
            dept = Department.objects.get(code=dept_code)
            Professor.objects.get_or_create(
                professor_id=prof_id,
                defaults={
                    'first_name': fname,
                    'last_name': lname,
                    'title': title,
                    'department': dept,
                    'email': f'{fname.lower()}.{lname.lower()}@silverpine.edu',
                    'office_location': office,
                    'office_hours': hours,
                    'bio': f'Professor {fname} {lname} is a distinguished member of the {dept.name} department.'
                }
            )
        
        self.stdout.write('Created professors')

    def create_courses(self):
        courses_data = [
            # Computer Science (15 courses)
            ('CSCI 1010', 'Introduction to Programming', 'CSCI', 'Learn fundamental programming concepts using Python.', 3, 'Undergraduate', ''),
            ('CSCI 1020', 'Data Structures', 'CSCI', 'Study of abstract data types and algorithms.', 3, 'Undergraduate', 'CSCI 1010'),
            ('CSCI 2010', 'Computer Organization', 'CSCI', 'Introduction to computer architecture and assembly language.', 3, 'Undergraduate', 'CSCI 1010'),
            ('CSCI 2020', 'Object-Oriented Programming', 'CSCI', 'Advanced programming using OOP principles.', 3, 'Undergraduate', 'CSCI 1020'),
            ('CSCI 3010', 'Database Systems', 'CSCI', 'Design and implementation of database systems.', 3, 'Undergraduate', 'CSCI 1020'),
            ('CSCI 3020', 'Web Development', 'CSCI', 'Modern web application development.', 3, 'Undergraduate', 'CSCI 2020'),
            ('CSCI 3030', 'Software Engineering', 'CSCI', 'Software development methodologies and practices.', 3, 'Undergraduate', 'CSCI 2020'),
            ('CSCI 3040', 'Algorithms', 'CSCI', 'Design and analysis of algorithms.', 3, 'Undergraduate', 'CSCI 1020'),
            ('CSCI 4010', 'Artificial Intelligence', 'CSCI', 'Introduction to AI and machine learning.', 3, 'Undergraduate', 'CSCI 3040'),
            ('CSCI 4020', 'Computer Networks', 'CSCI', 'Networking protocols and architectures.', 3, 'Undergraduate', 'CSCI 2010'),
            ('CSCI 4030', 'Cybersecurity', 'CSCI', 'Security principles and practices.', 3, 'Undergraduate', 'CSCI 2010'),
            ('CSCI 4040', 'Operating Systems', 'CSCI', 'OS design and implementation.', 3, 'Undergraduate', 'CSCI 2010'),
            ('CSCI 5010', 'Advanced Machine Learning', 'CSCI', 'Deep learning and neural networks.', 3, 'Graduate', 'CSCI 4010'),
            ('CSCI 5020', 'Cloud Computing', 'CSCI', 'Distributed systems and cloud architectures.', 3, 'Graduate', 'CSCI 4020'),
            ('CSCI 5030', 'Big Data Analytics', 'CSCI', 'Processing and analyzing large datasets.', 3, 'Graduate', 'CSCI 3010'),
            
            # Mathematics (12 courses)
            ('MATH 1010', 'Calculus I', 'MATH', 'Differential calculus and applications.', 4, 'Undergraduate', ''),
            ('MATH 1020', 'Calculus II', 'MATH', 'Integral calculus and series.', 4, 'Undergraduate', 'MATH 1010'),
            ('MATH 2010', 'Calculus III', 'MATH', 'Multivariable calculus.', 4, 'Undergraduate', 'MATH 1020'),
            ('MATH 2020', 'Linear Algebra', 'MATH', 'Vector spaces and matrices.', 3, 'Undergraduate', 'MATH 1010'),
            ('MATH 2030', 'Discrete Mathematics', 'MATH', 'Logic, sets, and combinatorics.', 3, 'Undergraduate', ''),
            ('MATH 3010', 'Differential Equations', 'MATH', 'Ordinary differential equations.', 3, 'Undergraduate', 'MATH 2010'),
            ('MATH 3020', 'Probability and Statistics', 'MATH', 'Statistical analysis and probability theory.', 3, 'Undergraduate', 'MATH 1020'),
            ('MATH 3030', 'Abstract Algebra', 'MATH', 'Groups, rings, and fields.', 3, 'Undergraduate', 'MATH 2020'),
            ('MATH 4010', 'Real Analysis', 'MATH', 'Advanced calculus and analysis.', 3, 'Undergraduate', 'MATH 2010'),
            ('MATH 4020', 'Complex Analysis', 'MATH', 'Functions of complex variables.', 3, 'Undergraduate', 'MATH 4010'),
            ('MATH 5010', 'Advanced Statistics', 'MATH', 'Graduate-level statistical methods.', 3, 'Graduate', 'MATH 3020'),
            ('MATH 5020', 'Number Theory', 'MATH', 'Properties of integers and primes.', 3, 'Graduate', 'MATH 3030'),
            
            # English (10 courses)
            ('ENG 1010', 'Composition I', 'ENG', 'Fundamentals of academic writing.', 3, 'Undergraduate', ''),
            ('ENG 1020', 'Composition II', 'ENG', 'Advanced composition and research.', 3, 'Undergraduate', 'ENG 1010'),
            ('ENG 2010', 'World Literature', 'ENG', 'Survey of global literary traditions.', 3, 'Undergraduate', 'ENG 1020'),
            ('ENG 2020', 'American Literature', 'ENG', 'American literary history and major works.', 3, 'Undergraduate', 'ENG 1020'),
            ('ENG 2030', 'British Literature', 'ENG', 'British literary tradition from Anglo-Saxon to modern.', 3, 'Undergraduate', 'ENG 1020'),
            ('ENG 3010', 'Shakespeare', 'ENG', 'Study of Shakespeare\'s major works.', 3, 'Undergraduate', 'ENG 2030'),
            ('ENG 3020', 'Modern Poetry', 'ENG', 'Contemporary poetic forms and movements.', 3, 'Undergraduate', 'ENG 2010'),
            ('ENG 3030', 'Creative Writing', 'ENG', 'Fiction and creative non-fiction writing.', 3, 'Undergraduate', 'ENG 1020'),
            ('ENG 4010', 'Literary Theory', 'ENG', 'Critical approaches to literature.', 3, 'Undergraduate', 'ENG 2010'),
            ('ENG 5010', 'Graduate Seminar in Literature', 'ENG', 'Advanced topics in literary studies.', 3, 'Graduate', 'ENG 4010'),
            
            # History (10 courses)
            ('HIST 1010', 'World History I', 'HIST', 'Ancient civilizations to 1500.', 3, 'Undergraduate', ''),
            ('HIST 1020', 'World History II', 'HIST', '1500 to present.', 3, 'Undergraduate', ''),
            ('HIST 2010', 'American History I', 'HIST', 'Colonial period to Civil War.', 3, 'Undergraduate', ''),
            ('HIST 2020', 'American History II', 'HIST', 'Reconstruction to present.', 3, 'Undergraduate', ''),
            ('HIST 3010', 'Ancient Greece and Rome', 'HIST', 'Classical civilizations.', 3, 'Undergraduate', 'HIST 1010'),
            ('HIST 3020', 'Medieval Europe', 'HIST', 'European history 500-1500.', 3, 'Undergraduate', 'HIST 1010'),
            ('HIST 3030', 'The Renaissance', 'HIST', 'Cultural rebirth in Europe.', 3, 'Undergraduate', 'HIST 3020'),
            ('HIST 4010', 'Modern European History', 'HIST', 'Europe 1800-present.', 3, 'Undergraduate', 'HIST 1020'),
            ('HIST 4020', 'Asian History', 'HIST', 'East and Southeast Asian civilizations.', 3, 'Undergraduate', 'HIST 1020'),
            ('HIST 5010', 'Historical Research Methods', 'HIST', 'Graduate research methodologies.', 3, 'Graduate', ''),
            
            # Biology (10 courses)
            ('BIOL 1010', 'General Biology I', 'BIOL', 'Introduction to cellular and molecular biology.', 4, 'Undergraduate', ''),
            ('BIOL 1020', 'General Biology II', 'BIOL', 'Ecology, evolution, and diversity.', 4, 'Undergraduate', 'BIOL 1010'),
            ('BIOL 2010', 'Genetics', 'BIOL', 'Principles of heredity and molecular genetics.', 3, 'Undergraduate', 'BIOL 1010'),
            ('BIOL 2020', 'Cell Biology', 'BIOL', 'Structure and function of cells.', 3, 'Undergraduate', 'BIOL 1010'),
            ('BIOL 3010', 'Microbiology', 'BIOL', 'Study of microorganisms.', 4, 'Undergraduate', 'BIOL 1020'),
            ('BIOL 3020', 'Anatomy and Physiology', 'BIOL', 'Human body systems.', 4, 'Undergraduate', 'BIOL 1020'),
            ('BIOL 3030', 'Ecology', 'BIOL', 'Organisms and their environments.', 3, 'Undergraduate', 'BIOL 1020'),
            ('BIOL 4010', 'Molecular Biology', 'BIOL', 'Advanced molecular mechanisms.', 3, 'Undergraduate', 'BIOL 2010'),
            ('BIOL 4020', 'Evolution', 'BIOL', 'Evolutionary theory and evidence.', 3, 'Undergraduate', 'BIOL 2010'),
            ('BIOL 5010', 'Advanced Genetics', 'BIOL', 'Graduate-level genetic analysis.', 3, 'Graduate', 'BIOL 2010'),
            
            # Chemistry (8 courses)
            ('CHEM 1010', 'General Chemistry I', 'CHEM', 'Fundamental chemical principles.', 4, 'Undergraduate', ''),
            ('CHEM 1020', 'General Chemistry II', 'CHEM', 'Chemical reactions and equilibrium.', 4, 'Undergraduate', 'CHEM 1010'),
            ('CHEM 2010', 'Organic Chemistry I', 'CHEM', 'Structure and reactions of organic compounds.', 4, 'Undergraduate', 'CHEM 1020'),
            ('CHEM 2020', 'Organic Chemistry II', 'CHEM', 'Advanced organic synthesis.', 4, 'Undergraduate', 'CHEM 2010'),
            ('CHEM 3010', 'Physical Chemistry', 'CHEM', 'Thermodynamics and kinetics.', 3, 'Undergraduate', 'CHEM 1020'),
            ('CHEM 3020', 'Analytical Chemistry', 'CHEM', 'Chemical analysis techniques.', 3, 'Undergraduate', 'CHEM 1020'),
            ('CHEM 4010', 'Biochemistry', 'CHEM', 'Chemistry of biological systems.', 3, 'Undergraduate', 'CHEM 2020'),
            ('CHEM 5010', 'Advanced Organic Chemistry', 'CHEM', 'Graduate organic chemistry.', 3, 'Graduate', 'CHEM 2020'),
            
            # Physics (8 courses)
            ('PHYS 1010', 'Physics I', 'PHYS', 'Mechanics and waves.', 4, 'Undergraduate', ''),
            ('PHYS 1020', 'Physics II', 'PHYS', 'Electricity and magnetism.', 4, 'Undergraduate', 'PHYS 1010'),
            ('PHYS 2010', 'Modern Physics', 'PHYS', 'Quantum mechanics and relativity.', 3, 'Undergraduate', 'PHYS 1020'),
            ('PHYS 3010', 'Classical Mechanics', 'PHYS', 'Advanced Newtonian mechanics.', 3, 'Undergraduate', 'PHYS 1010'),
            ('PHYS 3020', 'Thermodynamics', 'PHYS', 'Heat and statistical mechanics.', 3, 'Undergraduate', 'PHYS 1020'),
            ('PHYS 4010', 'Quantum Mechanics', 'PHYS', 'Principles of quantum theory.', 3, 'Undergraduate', 'PHYS 2010'),
            ('PHYS 4020', 'Electrodynamics', 'PHYS', 'Maxwell\'s equations and applications.', 3, 'Undergraduate', 'PHYS 1020'),
            ('PHYS 5010', 'Particle Physics', 'PHYS', 'Elementary particles and forces.', 3, 'Graduate', 'PHYS 4010'),
            
            # Economics (7 courses)
            ('ECON 1010', 'Principles of Microeconomics', 'ECON', 'Individual economic decisions.', 3, 'Undergraduate', ''),
            ('ECON 1020', 'Principles of Macroeconomics', 'ECON', 'National and global economic systems.', 3, 'Undergraduate', ''),
            ('ECON 2010', 'Intermediate Microeconomics', 'ECON', 'Advanced microeconomic theory.', 3, 'Undergraduate', 'ECON 1010'),
            ('ECON 2020', 'Intermediate Macroeconomics', 'ECON', 'Advanced macroeconomic analysis.', 3, 'Undergraduate', 'ECON 1020'),
            ('ECON 3010', 'Econometrics', 'ECON', 'Statistical methods in economics.', 3, 'Undergraduate', 'ECON 1010'),
            ('ECON 4010', 'International Economics', 'ECON', 'Global trade and finance.', 3, 'Undergraduate', 'ECON 2020'),
            ('ECON 5010', 'Advanced Economic Theory', 'ECON', 'Graduate economic analysis.', 3, 'Graduate', 'ECON 2010'),
            
            # Psychology (7 courses)
            ('PSYC 1010', 'Introduction to Psychology', 'PSYC', 'Survey of psychological science.', 3, 'Undergraduate', ''),
            ('PSYC 2010', 'Developmental Psychology', 'PSYC', 'Human development across lifespan.', 3, 'Undergraduate', 'PSYC 1010'),
            ('PSYC 2020', 'Social Psychology', 'PSYC', 'Social influences on behavior.', 3, 'Undergraduate', 'PSYC 1010'),
            ('PSYC 3010', 'Cognitive Psychology', 'PSYC', 'Mental processes and cognition.', 3, 'Undergraduate', 'PSYC 1010'),
            ('PSYC 3020', 'Abnormal Psychology', 'PSYC', 'Psychological disorders and treatment.', 3, 'Undergraduate', 'PSYC 1010'),
            ('PSYC 4010', 'Research Methods in Psychology', 'PSYC', 'Experimental design and statistics.', 3, 'Undergraduate', 'PSYC 1010'),
            ('PSYC 5010', 'Clinical Psychology', 'PSYC', 'Graduate clinical training.', 3, 'Graduate', 'PSYC 3020'),
            
            # Philosophy (5 courses)
            ('PHIL 1010', 'Introduction to Philosophy', 'PHIL', 'Major philosophical questions.', 3, 'Undergraduate', ''),
            ('PHIL 2010', 'Ethics', 'PHIL', 'Moral philosophy and ethical theory.', 3, 'Undergraduate', 'PHIL 1010'),
            ('PHIL 2020', 'Logic', 'PHIL', 'Formal and informal reasoning.', 3, 'Undergraduate', ''),
            ('PHIL 3010', 'Ancient Philosophy', 'PHIL', 'Greek and Roman philosophy.', 3, 'Undergraduate', 'PHIL 1010'),
            ('PHIL 4010', 'Modern Philosophy', 'PHIL', 'Descartes to Kant.', 3, 'Undergraduate', 'PHIL 3010'),
        ]
        
        for code, title, dept_code, desc, credits, level, prereq in courses_data:
            dept = Department.objects.get(code=dept_code)
            Course.objects.get_or_create(
                course_code=code,
                defaults={
                    'title': title,
                    'department': dept,
                    'description': desc,
                    'credits': credits,
                    'level': level,
                    'prerequisites': prereq
                }
            )
        
        self.stdout.write(f'Created {len(courses_data)} courses')

    def create_course_sections(self):
        courses = Course.objects.all()
        professors = list(Professor.objects.all())
        
        days_options = ['MWF', 'TR', 'MW', 'WF', 'T', 'R']
        times = [
            (time(8, 0), time(9, 15)),
            (time(9, 30), time(10, 45)),
            (time(11, 0), time(12, 15)),
            (time(12, 30), time(1, 45)),
            (time(2, 0), time(3, 15)),
            (time(3, 30), time(4, 45)),
        ]
        
        buildings = [
            'Hamilton Hall', 'Euler Building', 'Wordsworth Hall', 
            'Roosevelt Building', 'Darwin Science Center', 'Curie Laboratory',
            'Newton Hall', 'Smith Business Hall', 'Freud Center', 'Socrates Hall'
        ]
        
        section_count = 0
        for course in courses:
            # Create 1-2 sections per course
            num_sections = random.randint(1, 2)
            
            for i in range(num_sections):
                section_id = f"{course.course_code.replace(' ', '')}-{chr(65+i)}"
                days = random.choice(days_options)
                start_time, end_time = random.choice(times)
                building = random.choice(buildings)
                room = f"{random.randint(100, 500)}"
                professor = random.choice([p for p in professors if p.department == course.department])
                
                CourseSection.objects.get_or_create(
                    section_id=section_id,
                    defaults={
                        'course': course,
                        'professor': professor,
                        'semester': 'Spring 2026',
                        'days': days,
                        'start_time': start_time,
                        'end_time': end_time,
                        'building': building,
                        'room_number': room,
                        'max_capacity': random.randint(25, 40),
                        'enrolled_count': random.randint(0, 20),
                        'is_active': True,
                        'registration_open': True
                    }
                )
                section_count += 1
        
        self.stdout.write(f'Created {section_count} course sections')

    def create_students(self):
        students_data = [
            ('STU001', 'John', 'Smith', 'Computer Science', 'Mathematics', 'Junior', date(2023, 8, 15), date(2027, 5, 15)),
            ('STU002', 'Emma', 'Johnson', 'Biology', '', 'Sophomore', date(2024, 8, 15), date(2028, 5, 15)),
            ('STU003', 'Michael', 'Williams', 'Economics', 'Political Science', 'Senior', date(2022, 8, 15), date(2026, 5, 15)),
            ('STU004', 'Sophia', 'Brown', 'English Literature', 'History', 'Freshman', date(2025, 8, 15), date(2029, 5, 15)),
            ('STU005', 'James', 'Davis', 'Physics', '', 'Junior', date(2023, 8, 15), date(2027, 5, 15)),
        ]
        
        for sid, fname, lname, major, minor, year, enroll, grad in students_data:
            Student.objects.get_or_create(
                student_id=sid,
                defaults={
                    'first_name': fname,
                    'last_name': lname,
                    'email': f'{fname.lower()}.{lname.lower()}@student.silverpine.edu',
                    'major': major,
                    'minor': minor,
                    'academic_year': year,
                    'enrollment_date': enroll,
                    'expected_graduation': grad,
                    'gpa': round(random.uniform(3.0, 4.0), 2),
                    'total_credits': random.randint(30, 90),
                    'is_active': True,
                    'academic_standing': 'Good Standing'
                }
            )
        
        self.stdout.write('Created sample students')

    def create_semesters(self):
        Semester.objects.get_or_create(
            name='Spring 2026',
            defaults={
                'academic_year': '2025-2026',
                'start_date': date(2026, 1, 15),
                'end_date': date(2026, 5, 10),
                'registration_start': date(2025, 11, 1),
                'registration_end': date(2026, 1, 10),
                'add_drop_deadline': date(2026, 1, 25),
                'withdrawal_deadline': date(2026, 4, 1),
                'final_exams_start': date(2026, 5, 3),
                'final_exams_end': date(2026, 5, 10),
                'is_current': True,
                'is_active': True
            }
        )
        
        self.stdout.write('Created semesters')

    def create_academic_events(self):
        events_data = [
            ('Classes Begin', 'Spring semester classes start', 'Classes', date(2026, 1, 15), None, 'Spring 2026'),
            ('Add/Drop Deadline', 'Last day to add or drop courses', 'Deadline', date(2026, 1, 25), None, 'Spring 2026'),
            ('Spring Break', 'University closed for spring break', 'Break', date(2026, 3, 15), date(2026, 3, 22), 'Spring 2026'),
            ('Withdrawal Deadline', 'Last day to withdraw from courses', 'Deadline', date(2026, 4, 1), None, 'Spring 2026'),
            ('Final Exams', 'Final examination period', 'Exam', date(2026, 5, 3), date(2026, 5, 10), 'Spring 2026'),
            ('Commencement', 'Graduation ceremony', 'Commencement', date(2026, 5, 15), None, 'Spring 2026'),
        ]
        
        for title, desc, etype, start, end, semester in events_data:
            AcademicEvent.objects.get_or_create(
                title=title,
                semester=semester,
                start_date=start,
                defaults={
                    'description': desc,
                    'event_type': etype,
                    'end_date': end,
                    'all_day': True,
                    'is_active': True
                }
            )
        
        self.stdout.write('Created academic events')

    def create_holidays(self):
        holidays_data = [
            ('Martin Luther King Jr. Day', date(2026, 1, 19), True, True),
            ('Presidents Day', date(2026, 2, 16), True, True),
            ('Memorial Day', date(2026, 5, 25), True, True),
        ]
        
        for name, hdate, closed, cancelled in holidays_data:
            UniversityHoliday.objects.get_or_create(
                name=name,
                date=hdate,
                defaults={
                    'description': f'{name} - University holiday',
                    'university_closed': closed,
                    'classes_cancelled': cancelled
                }
            )
        
        self.stdout.write('Created holidays')

    def create_scholarships(self):
        scholarships_data = [
            ('Presidential Scholarship', 'Academic Merit', 25000, 3.8, 'Full-time enrollment, maintain 3.8 GPA', date(2026, 3, 1)),
            ('Dean\'s Excellence Award', 'Academic Merit', 15000, 3.5, 'Full-time enrollment, maintain 3.5 GPA', date(2026, 3, 15)),
            ('STEM Leadership Grant', 'Departmental', 10000, 3.0, 'STEM major, leadership experience', date(2026, 4, 1)),
            ('Diversity Scholarship', 'Diversity', 12000, 3.0, 'Underrepresented students', date(2026, 3, 20)),
            ('Athletic Achievement Award', 'Athletic', 8000, 2.5, 'Varsity athlete, good standing', date(2026, 2, 15)),
        ]
        
        for name, stype, amount, gpa, req, deadline in scholarships_data:
            Scholarship.objects.get_or_create(
                name=name,
                defaults={
                    'scholarship_type': stype,
                    'description': f'{name} provides financial support to deserving students.',
                    'amount': amount,
                    'minimum_gpa': gpa,
                    'eligibility_requirements': req,
                    'application_deadline': deadline,
                    'is_active': True,
                    'renewable': True
                }
            )
        
        self.stdout.write('Created scholarships')