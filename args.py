class Arguments:
    def __init__(self, argv):
        self.argv = argv
        self.argc = len(argv)
        self.cmd = argv[0]