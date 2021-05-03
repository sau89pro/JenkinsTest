from conans import ConanFile, CMake, tools

class JenkinsTestConan(ConanFile):
    name = "jenkins_test"
    version = "1.0"
    author = "A.U.Sokolov sau_89@bk.ru"
    description = "Package for testing CD"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    exports_sources = "src*"
    generators = "cmake"
    no_copy_source = True

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()
        cmake.install()
    
    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC
            