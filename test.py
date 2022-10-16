# --------------------------------------------------------------------------
# Unit tests for this coding unit
#  You can run tests by running this file,
#  or using the flask menu in VSCode.
#
# Unit tests do not replace a good manual testing strategy,
# but they can give you some early feedback and some initial
# confidence in your code
#
# Unit tests do not check for good programming practices
# such as meaningful variable names, spacing, etc. You need to
# do this manually
# ---------------------------
from re import T
import unittest
import subprocess
import sys
import os


# ---------------------------------------------
# helper code. Please ignore and do not modify
# ---------------------------------------------
def PerseTestCase(file):
    def wrapper_class(wrapped_class):  # allows the @PerseTestCase("filetotest.py") decorator to be added to a class
        wrapped_init = wrapped_class.__init__
        def run_code(inputs, time_s):  
            try:  # try to run the `code under test` with a timeout, with the given inputs, returning the outputs
                inputs = ("\n".join(str(x) for x in inputs) + "\n").encode('utf-8') if inputs else None
                environ = os.environ.copy()
                environ['PYTHONIOENCODING'] = 'utf-8'
                result = subprocess.run([sys.executable, f"{os.path.dirname(__file__)}/{file}{'.py' if not file.endswith('.py') else ''}"],
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, input=inputs, timeout=time_s, env=environ)
                return result.stdout.decode('utf-8').strip()
            except subprocess.TimeoutExpired:
                raise Exception("Timed out")
        def __init__(self, *args, **kws):
            wrapped_init(self, *args, **kws)
            self.run_code = lambda ins=[], t=1.5: run_code(ins, t)
        wrapped_class.__init__ = __init__
        return wrapped_class
    return wrapper_class

# ---------------------------
# test cases
# ---------------------------

@PerseTestCase("main.py")
class TestNEA(unittest.TestCase): # You can have more classes to test other files
    def test_name_here(self):
        inputs = ["t",3,4,3,3,3,2,6,4,4,3,3,5,6,5,5,3,3,6,4,2,5,2,7,5,6,3,2,2,7,4,3,1,7,6,5,1,2,1,1,1,1,2,1,3,1,4,6,2,2,3,2,4,2,5,2,6,1,6,1,5,4,1,7,3,6,1,8,2,7,2,8,3] # Inputs in a list
        output = self.run_code(inputs) # Don't touch this line
        #self.assertIn("PE (J)", output) # Expect this to be in the output to pass
        #self.assertIn("KE (J)", output) # etc. for as many as you need

    #def another_test_name_here(self):
     #   inputs = [0, 0, 0] # Inputs in a list
      #  output = self.run_code(inputs) # Don't touch this line
       # self.assertIn("PE (J)", output) # Expect this to be in the output to pass
        #self.assertIn("KE (J)", output) # etc. for as many as you need



# run all tests when this file is executed
if __name__ == "__main__":
    unittest.main(verbosity=3)
