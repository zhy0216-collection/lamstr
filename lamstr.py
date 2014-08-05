import re
import uuid


OP_RE = re.compile(r"[-\*/\+\.]")

LEFT_LACK_OP_RE = re.compile(r"^([-\*/\+\.]|\*\*)(\w+)")

RIGHT_LACK_OP_RE = re.compile(r"(\w+[-\*/\+\.]|\*\*)*\w+")


VARIABLE_RE = re.compile(r"([a-zA-Z_]\w*)")


class _LambdaStr(object):

    def __init__(self,expr, config=None):
        self.expr = self.orginal_expr = expr

        self.var_prefix = "_lam__"

        self.arguments = None
        self.return_expr = None

        self.left_lack_march = None
        self.right_lack_march = None


        #config stuff
        if config == None:
            config = {}
        self.return_op = config.get("return_op", "->")

        self._parse()

    def _check_if_left_lack(self):
        self.left_lack_march = LEFT_LACK_OP_RE.search(self.expr)
        return self.left_lack_march is not None

    def _check_if_right_lack(self):
        self.right_lack_march = RIGHT_LACK_OP_RE.search(self.expr)
        return self.right_lack_march is None

    def _add_left_var(self):
            # /2, *2,, single?
        var = self.var_prefix + self._gen_random_var_name()
        self.arguments = [var]
        self.return_expr = self.expr = var + self.expr

    def _add_right_var(self):
        # it is pretty diffcult to find the right rex because of ** op
        # ... struggle with it
        if RIGHT_LACK_OP_RE_CASE0.search(self.expr):
            pass

    def _special_parse(self):
        
        if  self._check_if_left_lack():
            # case *2 +1 suh stuff
            self._add_left_var()
            self._special_parse()

        elif self._check_if_right_lack():
            # recursive
            pass

        else:
            # return function directly
            # 2*x
            if not self.arguments:
                vars = set(VARIABLE_RE.findall(self.expr))
                self.arguments = list(vars)
            self.return_expr = self.expr

    def _parse(self):
        if self.expr.find(self.return_op) == -1:
            self.expr = self.orginal_expr.strip()
            return self._special_parse()

        arguments, self.return_expr = self.expr.split(self.return_op)
        self.arguments = VARIABLE_RE.findall(arguments)
        print "self.arguments", self.arguments, "self.return_expr", self.return_expr

    def _gen_random_var_name(self):
        return self.var_prefix + str(uuid.uuid1()).replace("-", "")


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











