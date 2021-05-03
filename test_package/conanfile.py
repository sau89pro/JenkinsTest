import os

from conans import ConanFile, tools

class JenkinsTestTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"

    def test(self):
        if not tools.cross_building(self):
            os.chdir(self.deps_cpp_info.bindirs[0])
            self.run(".%sjenkins_test" % os.sep)
