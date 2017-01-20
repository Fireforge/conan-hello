import os
from pathlib import Path
from conans import ConanFile, CMake


class HelloConan(ConanFile):
    name = "conan-hello"
    description = '"Hello world" project for testing Conan build and package setups'
    version = "0.1"
    license = "MIT"
    url = "https://github.com/memsharded/conan-hello-embed.git"

    settings = "os", "compiler", "arch"
    exports = "CMakeLists.txt", "hello.*", "main.cpp", "LICENSE", "README.md"

    def build(self):
        builddir = Path.cwd() / "build"
        self.build_type("Debug", builddir)
        self.build_type("Release", builddir)

    def package(self):
        self.copy("*.h", dst="include")
        self.copy("*.lib", dst="lib", src="lib")
        self.copy("*.a", dst="lib", src="lib")

    def package_info(self):
        self.cpp_info.libs=["hello"]

    def build_type(self, build_type, build_dir):
        bdir = build_dir / build_type
        # Debug install build
        bdir.mkdir(parents=True, exist_ok=True)
        os.chdir(str(bdir))
        self.run(str.format('conan install ../.. -s build_type={}', build_type))
        cmake = CMake(self.settings)
        self.run(str.format('cmake {src} {args}',
                 src="../../src", args=cmake.command_line))
        self.run(str.format('cmake --build . --config {} {}', build_type, cmake.build_config))
