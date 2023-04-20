from setuptools import find_packages,setup


required_file_name = "requirements.txt"
hyphen_dot_e = "-e ."

def get_requirements():
    with open(required_file_name) as file:
        required_libs = file.readlines()

    required_libs = [i.replace("\n","") for i in required_libs]
    if hyphen_dot_e in required_libs:
       required_libs.remove(hyphen_dot_e)
    return required_libs

setup(
    name="Caughing_some_Phishing",
    version="0.0.1",
    author="Shripad-Garat",
    author_email="garatshripad09@gmail.com",
    packages=find_packages(),
    install_requirement = get_requirements()
)