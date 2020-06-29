
from conans import ConanFile, CMake, tools

class Package2Conan(ConanFile):
    name = "package-2"
    settings = "os", "compiler", "build_type", "arch", "toolchain"
    options = {"shared": [True, False]}
    default_options = ("shared=False")
    generators = "cmake"

    requires = (
        "package-1/[=1.0]@error/test",
    )
