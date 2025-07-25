import io

from conan import ConanFile
from conan.tools.build import can_run


class TestPackageConan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "VirtualRunEnv"
    test_type = "explicit"

    def requirements(self):
        self.requires(self.tested_reference_str)

    def test(self):
        if can_run(self):
            stderr = io.StringIO()
            self.run(f"guetzli", env="conanrun", stderr=stderr, ignore_errors=True)
            assert "Guetzli JPEG compressor" in stderr.getvalue()
