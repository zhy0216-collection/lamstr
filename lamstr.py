import re



OP_RE = re.compile(r"[-\*/\+\.]")

VARIABLE_RE = ""








class _LambdaStr(object):

    def __init__(self,expr, config=None):
        self.expr = expr

        self.arguments = None
        self.return_expr = None


        #config stuff
        if config == None:
            config = {}
        self.return_op = config.get("return_op", "->")

        self._parse()

    def _special_parse(self):
        if OP_RE.search(self.expr) == None:
            pass
        else:
            pass


    def _parse(self):
        if self.expr.find(self.return_op) == -1:
            return self._special_parse()

        arguments, self.return_expr = self.expr.split(self.return_op)
        self.arguments = arguments.split(",")
        print "self.arguments", self.arguments, "self.return_expr", self.return_expr


    @property
    def function(self):
        code = "_lam = lambda %s: %s"%(",".join(self.arguments),self.return_expr)
        print "code:", code
        result = {}
        exec compile(code, '<string>', 'exec') in result
        print "result", result["_lam"]
        return result["_lam"]



    def __call__(self, *arg):
        return self.function(*arg)




def lam(expr):
    return _LambdaStr(expr)











