#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class BoostLevel11GroupConan(ConanFile):
    # This is now Level 15
    name = "boost_level11group"
    version = "1.67.0"
    author = "Bincrafters <bincrafters@gmail.com>"
    exports = ["LICENSE.md"]
    is_cycle_group = True
    lib_short_names = [
        "date_time", "pool", "serialization", "spirit", "thread"]

    is_header_only = {
        "date_time":False,
        "pool":True,
        "serialization":False,
        "spirit":True,
        "thread":False }

    options = {"shared": [True, False]}
    default_options = "shared=False"

    requires = (
        "boost_package_tools/1.67.0@bincrafters/testing",
        "boost_algorithm/1.67.0@bincrafters/testing",
        "boost_array/1.67.0@bincrafters/testing",
        "boost_assert/1.67.0@bincrafters/testing",
        "boost_atomic/1.67.0@bincrafters/testing",
        "boost_bind/1.67.0@bincrafters/testing",
        "boost_chrono/1.67.0@bincrafters/testing",
        "boost_concept_check/1.67.0@bincrafters/testing",
        "boost_config/1.67.0@bincrafters/testing",
        "boost_container/1.67.0@bincrafters/testing",
        "boost_container_hash/1.67.0@bincrafters/testing",
        "boost_core/1.67.0@bincrafters/testing",
        "boost_detail/1.67.0@bincrafters/testing",
        "boost_endian/1.67.0@bincrafters/testing",
        "boost_exception/1.67.0@bincrafters/testing",
        "boost_filesystem/1.67.0@bincrafters/testing",
        "boost_foreach/1.67.0@bincrafters/testing",
        "boost_function/1.67.0@bincrafters/testing",
        "boost_function_types/1.67.0@bincrafters/testing",
        "boost_fusion/1.67.0@bincrafters/testing",
        "boost_integer/1.67.0@bincrafters/testing",
        "boost_intrusive/1.67.0@bincrafters/testing",
        "boost_io/1.67.0@bincrafters/testing",
        "boost_iostreams/1.67.0@bincrafters/testing",
        "boost_iterator/1.67.0@bincrafters/testing",
        "boost_lexical_cast/1.67.0@bincrafters/testing",
        "boost_math/1.67.0@bincrafters/testing",
        "boost_move/1.67.0@bincrafters/testing",
        "boost_mpl/1.67.0@bincrafters/testing",
        "boost_numeric_conversion/1.67.0@bincrafters/testing",
        "boost_optional/1.67.0@bincrafters/testing",
        "boost_phoenix/1.67.0@bincrafters/testing",
        "boost_predef/1.67.0@bincrafters/testing",
        "boost_preprocessor/1.67.0@bincrafters/testing",
        "boost_proto/1.67.0@bincrafters/testing",
        "boost_range/1.67.0@bincrafters/testing",
        "boost_regex/1.67.0@bincrafters/testing",
        "boost_smart_ptr/1.67.0@bincrafters/testing",
        "boost_static_assert/1.67.0@bincrafters/testing",
        "boost_system/1.67.0@bincrafters/testing",
        "boost_throw_exception/1.67.0@bincrafters/testing",
        "boost_tokenizer/1.67.0@bincrafters/testing",
        "boost_tti/1.67.0@bincrafters/testing",
        "boost_tuple/1.67.0@bincrafters/testing",
        "boost_type_traits/1.67.0@bincrafters/testing",
        "boost_typeof/1.67.0@bincrafters/testing",
        "boost_unordered/1.67.0@bincrafters/testing",
        "boost_utility/1.67.0@bincrafters/testing",
        "boost_variant/1.67.0@bincrafters/testing",
        "boost_winapi/1.67.0@bincrafters/testing"
    )

    def package_info_additional(self):
        if self.settings.os != "Windows":
            self.cpp_info.libs.append("pthread")

    def package_id_additional(self):
        boost_deps_only = [dep_name for dep_name in self.info.requires.pkg_names if dep_name.startswith("boost_")]

        for dep_name in boost_deps_only:
            self.info.requires[dep_name].full_version_mode()

    # BEGIN

    url = "https://github.com/bincrafters/conan-boost_level11group"
    description = "Please visit http://www.boost.org/doc/libs/1_67_0"
    license = "BSL-1.0"
    short_paths = True
    generators = "boost"
    settings = "os", "arch", "compiler", "build_type"
    build_requires = "boost_generator/1.67.0@bincrafters/testing"

    def package_id(self):
        getattr(self, "package_id_additional", lambda:None)()

    def source(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.source(self)
        getattr(self, "source_additional", lambda:None)()

    def build(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.build(self)
        getattr(self, "build_additional", lambda:None)()

    def package(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package(self)
        getattr(self, "package_additional", lambda:None)()

    def package_info(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package_info(self)
        getattr(self, "package_info_additional", lambda:None)()

    # END
