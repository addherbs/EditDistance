class Sub ():
    def __init__(self):
        self.list = []

    def _calculate(self, input, output):
        if (len (input) == 0):
            if (output != '' and (output not in self.list) and len (output) > 1):
                self.list.append (output)
            return None
        else:
            self._calculate (input[1:], output)
            self._calculate (input[1:], output + input[0])

    def return_list(self):
        return self.list

    def calculate(self, string):
        self._calculate (string, '')


object = Sub ()
object.calculate ('aaabc')
print (object.return_list ())
