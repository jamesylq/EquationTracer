try:
    from main import main
except ModuleNotFoundError:
    from equationtracer.main import main

main()
