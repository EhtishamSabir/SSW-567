class HelloWorld:
    message = ""

    def set_message(self, str):
        self.message = str
    
    def get_message(self):
        return self.message

    def print_message(self):
        print(self.message)

obj = HelloWorld()
obj.set_message("Hello World!")
obj.print_message()
