class Solution(object):
    __ops = {
        '(': (0, None), ')': (0, None), 
        '+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y), 
        '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x // y)}
    
    class Mono(object):
        def __init__(self, var):
            self.coef = 1
            self.degree = 1
            self.vars = {}
            self.vars[var] = 1
        def mul(self, other):
            self.coef *= other.coef
            self.degree += other.degree
            for var in other.vars:
                if self.vars.__contains__(var):
                    self.vars[var] += other.vars[var]
                else:
                    self.vars[var] = other.vars[var]
        def __str__(self):
            return str(self.coef) + ' * ' + str(self.vars)
    
    class Poly(object):
        def __init__(self, mono, coef):
            self.monos = {}
            self.monos[mono] = coef

    def basicCalculatorIV(self, expression, evalvars, evalints):
        """
        :type expression: str
        :type evalvars: List[str]
        :type evalints: List[int]
        :rtype: List[str]
        """
        m = self.Mono('a')
        m.mul(self.Mono('b'))
        m.mul(self.Mono('a'))
        print(m)
        # stack = [('(', 0)]
        # def expr(value, level=None):
        #     if level is not None and value is not '(':
        #         while stack[-2][1] >= level:
        #             if stack[-2][0] is '(':
        #                 stack[-1] = stack.pop()[0], None
        #                 return
        #             else:
        #                 num2 = stack.pop()[0]
        #                 op_cur = stack.pop()[0]
        #                 stack[-1] = self.__ops[op_cur][1](stack[-1][0], num2), None
        #     if value is not None:
        #         stack.append((value, level))
        # num = None
        # for ch in expression:
        #     if ch.isdigit():
        #         num = int(ch) if num is None else int(ch) + num * 10
        #     elif ch in self.__ops:
        #         expr(num)
        #         expr(ch, self.__ops[ch][0])
        #         num = None
        # expr(num)
        # expr(')', 0)
        # return stack[0][0]
        pass


print('["-1*a","14"]', Solution().basicCalculatorIV(expression = "e + 8 - a + 5", evalvars = ["e"], evalints = [1]))
# print('["-1*pressure","5"]', Solution().basicCalculatorIV(expression = "e - 8 + temperature - pressure", evalvars = ["e", "temperature"], evalints = [1, 12]))
# print('["1*e*e","-64"]', Solution().basicCalculatorIV(expression = "(e + 8) * (e - 8)", evalvars = [], evalints = []))
# print('[]', Solution().basicCalculatorIV(expression = "7 - 7", evalvars = [], evalints = []))
# print('["5*a*b*c"]', Solution().basicCalculatorIV("a * b * c + b * a * c * 4", evalvars = [], evalints = []))
# print('["-1*a*a*b*b","2*a*a*b*c","-1*a*a*c*c","1*a*b*b*b","-1*a*b*b*c","-1*a*b*c*c","1*a*c*c*c","-1*b*b*b*c","2*b*b*c*c","-1*b*c*c*c","2*a*a*b","-2*a*a*c","-2*a*b*b","2*a*c*c","1*b*b*b","-1*b*b*c","1*b*c*c","-1*c*c*c","-1*a*a","1*a*b","1*a*c","-1*b*c"]\n', \
#     Solution().basicCalculatorIV(expression = "((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))", evalvars = [], evalints = []))


# Given an expression such as expression = "e + 8 - a + 5" and an evaluation map such as {"e": 1} (given in terms of evalvars = ["e"] and evalints = [1]), return a list of tokens representing the simplified expression, such as ["-1*a","14"]

# An expression alternates chunks and symbols, with a space separating each chunk and symbol.
# A chunk is either an expression in parentheses, a variable, or a non-negative integer.
# A variable is a string of lowercase letters (not including digits.) Note that variables can be multiple letters, and note that variables never have a leading coefficient or unary operator like "2x" or "-x".
# Expressions are evaluated in the usual order: brackets first, then multiplication, then addition and subtraction. For example, expression = "1 + 2 * 3" has an answer of ["7"].

# The format of the output is as follows:

# For each term of free variables with non-zero coefficient, we write the free variables within a term in sorted order lexicographically. For example, we would never write a term like "b*a*c", only "a*b*c".
# Terms have degree equal to the number of free variables being multiplied, counting multiplicity. (For example, "a*a*b*c" has degree 4.) We write the largest degree terms of our answer first, breaking ties by lexicographic order ignoring the leading coefficient of the term.
# The leading coefficient of the term is placed directly to the left with an asterisk separating it from the variables (if they exist.)  A leading coefficient of 1 is still printed.
# An example of a well formatted answer is ["-2*a*a*a", "3*a*a*b", "3*b*b", "4*a", "5*c", "-6"] 
# Terms (including constant terms) with coefficient 0 are not included.  For example, an expression of "0" has an output of [].
# Examples:

# Input: expression = "e + 8 - a + 5", evalvars = ["e"], evalints = [1]
# Output: ["-1*a","14"]

# Input: expression = "e - 8 + temperature - pressure",
# evalvars = ["e", "temperature"], evalints = [1, 12]
# Output: ["-1*pressure","5"]

# Input: expression = "(e + 8) * (e - 8)", evalvars = [], evalints = []
# Output: ["1*e*e","-64"]

# Input: expression = "7 - 7", evalvars = [], evalints = []
# Output: []

# Input: expression = "a * b * c + b * a * c * 4", evalvars = [], evalints = []
# Output: ["5*a*b*c"]

# Input: expression = "((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))",
# evalvars = [], evalints = []
# Output: ["-1*a*a*b*b","2*a*a*b*c","-1*a*a*c*c","1*a*b*b*b","-1*a*b*b*c","-1*a*b*c*c","1*a*c*c*c","-1*b*b*b*c","2*b*b*c*c","-1*b*c*c*c","2*a*a*b","-2*a*a*c","-2*a*b*b","2*a*c*c","1*b*b*b","-1*b*b*c","1*b*c*c","-1*c*c*c","-1*a*a","1*a*b","1*a*c","-1*b*c"]
# Note:

# expression will have length in range [1, 250].
# evalvars, evalints will have equal lengths in range [0, 100].

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/basic-calculator-iv
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
