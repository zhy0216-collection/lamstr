import re



OP_RE = re.compile(r"[\+\.-\*\%]")

VARIABLE_RE = ""








class _LambdaStr(object):

    def __init__(self,expr, config=None):
        self.expr = expr
        self.function = None


        #config stuff
        if config == None:
            config = {}
        self.return_op = config.get("return_op", "->")

        self._parse()

    def special(self):
        pass

    def _parse(self):
        if self.expr.find(self.return_op) == -1:
            return self._special_parse(self.expr)

        arguments, return_expr = self.expr.split(self.return_op)
        print "arguments", arguments, "return_expr", return_expr

        code = "_lam = lambda %s: %s"%(arguments,return_expr)
        print "code:", code
        result = {}
        exec compile(code, '<string>', 'exec') in result
        print "result", result["_lam"]

        self.function = result["_lam"]


    def __call__(self, *arg):
        return self.function(*arg)




def lam(expr):
    return _LambdaStr(expr)











