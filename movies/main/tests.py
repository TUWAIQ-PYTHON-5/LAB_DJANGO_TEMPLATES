from django.test import TestCase
from password_generator import PasswordGenerator

password = PasswordGenerator().generate()
print(password)
# Create your tests here.
