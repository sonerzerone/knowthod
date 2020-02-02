import subprocess
import sys
import os

class RunPyCode(object):
    def __init__(self, code=None, input=None):
        self.code = code
        self.input = input
        if not os.path.exists('running'):
            os.mkdir('running')

    def _run_py_prog(self, cmd="a.py", input=None):
        cmd = [sys.executable, cmd]
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        a = p.communicate(input = bytes(input, encoding='utf-8'))[0]
        b = p.communicate()[1]
        self.stdout, self.stderr = a.decode("utf-8"), b.decode("utf-8")

    def run_py_code(self, code=None, input=None):
        filename = './running/a.py'
        if not code:
            code = self.code
        if not input:
            input = self.input
        with open(filename, "w") as f:
            f.write(code)
        self._run_py_prog(filename, input)
        return self.stderr, self.stdout



class RunCppCode(object):
    def __init__(self, code=None, input=None):
        self.code = code
        self.input = input
        if not os.path.exists('running'):
            os.mkdir('running')

    def _run_cpp_prog(self, cmd="b.cpp", input=None):
        p = subprocess.Popen("g++ -o b ./running/b.cpp", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        err = p.stderr.read().decode('utf-8')
        self.stderr = err
        self.stdout = ''
        if err == '':
            p = subprocess.Popen("./b", stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
            out = p.communicate(input = bytes(input, encoding='utf-8'))[0]
            self.stdout = out.decode('utf-8')

    def run_cpp_code(self, code=None, input=None):
        filename = './running/b.cpp'
        if not code:
            code = self.code
        if not input:
            input = self.input
        with open(filename, "w") as f:
            f.write(code)
        self._run_cpp_prog(filename, input)
        return self.stderr, self.stdout
