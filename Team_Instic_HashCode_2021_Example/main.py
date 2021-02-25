class TeamInsticSolution:
    def __init__(self) -> None:
        super().__init__()
        self.data = None
        self.input_file_name = './input/a.txt'
        self.output_file_name = 'main.txt'
        self.STREETS = {}
        self.CARS = {}
        self.STREETS_LENS = {}
        self.DURATION = None
        self.NUM_INTER = None
        self.NUM_STREETS = None
        self.NUM_CARS = None
        self.BONUS = None


    def read_input(self, file_name):
        with open(file_name) as f:
            self.data = [i.strip() for i in f.readlines()]
            line_num_get = 0
            self.DURATION, self.NUM_INTER, self.NUM_STREETS, self.NUM_CARS, self.BONUS = map(int, self.data[0].split(' '))
            for _ in range(self.NUM_STREETS):
                line_num_get += 1
                line = self.data[line_num_get]
                START, END, NAME, LEN = line.split(' ')
                self.STREETS[NAME] = {'start': int(START), 'end': int(END), 'len': int(LEN)}
                self.STREETS_LENS[NAME] = LEN

            for i in range(self.NUM_CARS):
                line_num_get += 1
                line = self.data[line_num_get]
                CAR_STREETS = line.split(' ')[1:]
                self.CARS[i] = list(CAR_STREETS)


    def run(self):
        self.read_input(self.input_file_name)
        with open(self.output_file_name, 'w') as f:
            f.writelines(self.data)


solution = TeamInsticSolution()
solution.run()