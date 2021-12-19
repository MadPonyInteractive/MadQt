def main():
    from MadQt.Apps import ProjectManager
    import os, subprocess
    os.chdir(os.path.dirname(ProjectManager.__file__))
    subprocess.check_output(["python","main.py"])
