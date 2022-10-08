from assignment.models import Subject, User
from django.test import TestCase

class TestModels(TestCase):
    
    def setUp(self):

        self.k = User.objects.create(id=1, pk=2, username="tester", is_staff = True, is_active = True, is_superuser= False)

        self.subject = Subject.objects.create(
            code = 'cn000',
            name = 'test model',
            teacher = self.k,
            semester = 1,
            max_seat = 100,
            credit = 3,
            active = True
        )
        
    def test_subject_is_created(self):
        self.assertEquals(self.subject.code, 'cn000')

    def test_add_course_not_full(self):
        subjectInfo = self.subject
        subjectInfo.enroll.add(self.k)
        self.assertEquals(subjectInfo.enroll.count(), 1)
