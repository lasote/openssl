from conans import python_requires

base = python_requires("OpenSSL/1.0.2r@conan/stable")

class PkgTest(base.OpenSSLConan):
    name = "OpenSSL"
    version = "1.0.2r"
    scm = {"type": "git", "url": "auto", "revision": "auto"}

    @property
    def subfolder(self):
        return "."

    def source(self):
        pass
