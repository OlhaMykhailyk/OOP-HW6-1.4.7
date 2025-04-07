class Calculator:
    def __init__(self):
        self.expression = ""
        self.variables = {}
    def set_expression(self, expr):
        self.expression = expr
        self.variables = {var: None for var in self.__find_variables()}
    def __find_variables(self):
        variables = set()
        for ch in self.expression:
            if ch.isalpha():
                variables.add(ch)
        return sorted(list(variables))
    def get_variables(self):
        return list(self.variables.keys())
    def set_variable_value(self, var, value):
        if var in self.variables:
            self.variables[var] = value
        else:
            print("error - variable {var} is bad")
    def all_variables_set(self):
        return all(value is not None for value in self.variables.values())
    def evaluate(self):
        if not self.all_variables_set():
            raise ValueError("Не для всіх змінних задані значення")
        eval_expr = self.expression
        for var, value in self.variables.items():
            eval_expr = eval_expr.replace(var, str(value))
        try:
            return eval(eval_expr)
        except Exception as e:
            raise ValueError(f"Помилка обчислення: {e}")


