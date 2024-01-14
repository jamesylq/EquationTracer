try:
    from main import main
except (NameError, FileNotFoundError, ModuleNotFoundError):
    from equationtracer.main import main

main()
