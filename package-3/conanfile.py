
from conans import ConanFile, CMake, tools

class Package3Conan(ConanFile):
    name = "package-3"
    settings = "os", "compiler", "build_type", "arch", "toolchain"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
    }
    default_options = (
        "shared=False",
        "fPIC=True"
    )

    requires = (
        "package-2/[=1.0]@error/test"
    )

    def package_id(self):
        self.info.shared_library_package_id()