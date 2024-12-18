# from django.test import TestCase
# from .models import SpyCat, Mission, Target

# class SpyCatModelTest(TestCase):
#     def test_create_spycat(self):
#         cat = SpyCat.objects.create(
#             name="Whiskers",
#             years_of_experience=5,
#             breed="Siberian",
#             salary=70000
#         )
#         self.assertEqual(cat.name, "Whiskers")
#         self.assertEqual(cat.breed, "Siberian")

# class MissionTest(TestCase):
#     def test_create_mission(self):
#         cat = SpyCat.objects.create(
#             name="Shadow",
#             years_of_experience=3,
#             breed="Bengal",
#             salary=50000
#         )
#         mission = Mission.objects.create(cat=cat, complete=False)
#         target = Target.objects.create(
#             mission=mission, name="Target 1", country="USA", notes="Spy on HQ", complete=False
#         )
#         self.assertEqual(mission.cat.name, "Shadow")
#         self.assertEqual(target.name, "Target 1")
