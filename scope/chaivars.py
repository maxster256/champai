# chaivars.py


class Variable:
    """
    Defines common interface for variables
    """
    def __init__(self, pidentifier, lineno):
        self.pidentifier = pidentifier
        self.lineno = lineno
        self.value_has_been_set = False

        # self.value = None
        # self.updated_after_compilation = True
        # super().__init__()

    # def set_updated_after_compilation(self):
    #     self.updated_after_compilation = True
    #     self.value = None

    def set_value_has_been_set(self):
        self.value_has_been_set = True

    def get_value_has_been_set_status(self):
        return self.value_has_been_set


class Int(Variable):
    """
    Defines integer representation in Champai.
    """
    def __init__(self, pidentifier, lineno):
        self.is_iterator = False
        super().__init__(pidentifier=pidentifier, lineno=lineno)

    def __repr__(self):
        return str("[Integer {}, line {}]".format(self.pidentifier, self.lineno))

    def set_as_iterator(self):
        self.is_iterator = True

    def get_is_iterator(self):
        return self.is_iterator


class IntArray(Variable):
    def __init__(self, pidentifier, lineno, from_val, to_val):
        self.from_val = int(from_val)
        self.to_val = int(to_val)
        self.value_has_been_set = True

        if self.to_val >= self.from_val:
            self.offset = self.from_val
            self.length = self.to_val - self.from_val + 1 + 1 # because of storing offset
        else:
            raise Exception("chaivars IntArray: invalid array bounds for declared IntArray[{}:{}], line {}".format(
                self.from_val, self.to_val, lineno))

        super().__init__(pidentifier, lineno)

    def __repr__(self):
        return self.pidentifier


class IntArrayElement(Variable):
    def __init__(self, array, value_holder, lineno):
        self.array = array
        self.value_holder = value_holder # int or variable
        self.value_has_been_set = True
        super().__init__(array.pidentifier, lineno)

    def get_value_holder(self):
        return self.value_holder




