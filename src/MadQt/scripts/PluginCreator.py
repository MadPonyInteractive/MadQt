def main():
    from MadQt.Apps import PluginCreator
    import os, subprocess
    os.chdir(os.path.dirname(PluginCreator.__file__))
    subprocess.check_output(["python","main.py"])
