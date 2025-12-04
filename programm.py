class programm:
    def __init__(self,name,language,num_of_lines):
        self.name = name
        self.language = language
        self.num_of_lines = num_of_lines
    def compile(self):
        print("Your code of "+self.num_of_lines+" lines is compiling which was wriiten in "+self.language+" language")
    def run(self):
        print("Your programm "+self.name+" is running!")
    def debug(self):
        print("Checking fo error in "+self.name)
    def display_info(self):
        print("Programm name: "+self.name+" Language: "+self.language+" Number of Lines: "+self.num_of_lines)

programm1 = programm("Chatbot","Python","250")
programm1.display_info()
programm1.compile()
programm1.run()
programm1.debug()
print(" ")

programm2 = programm("Facial recognition","java","550")
programm2.display_info()
programm2.compile()
programm2.run()
programm2.debug()
print(" ")

programm3 = programm("Weather forecast","C++","800")
programm3.display_info()
programm3.compile()
programm3.run()
programm3.debug()




