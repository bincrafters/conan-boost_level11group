#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class BoostLevel11GroupConan(ConanFile):
    name = "boost_level11group"
    version = "1.65.1"
    url = "https://github.com/bincrafters/conan-boost_level11group"
    author = "Bincrafters <bincrafters@gmail.com>"
    exports = ["LICENSE.md"]
    lib_short_names = [
        "date_time", "locale", "pool", "serialization", "spirit", "thread"]
        
    is_cycle_group = True
    is_header_only = {
        "date_time":False,
        "locale":False,
        "pool":True,
        "serialization":False,
        "spirit":True,
        "thread":False }
        
    options = {"shared": [True, False], "use_icu": [True, False]}
    default_options = "shared=False", "use_icu=False"

    requires = (
        "boost_package_tools/1.65.1@bincrafters/testing",
        "boost_algorithm/1.65.1@bincrafters/testing",
        "boost_array/1.65.1@bincrafters/testing",
        "boost_assert/1.65.1@bincrafters/testing",
        "boost_atomic/1.65.1@bincrafters/testing",
        "boost_bind/1.65.1@bincrafters/testing",
        "boost_chrono/1.65.1@bincrafters/testing",
        "boost_concept_check/1.65.1@bincrafters/testing",
        "boost_config/1.65.1@bincrafters/testing",
        "boost_container/1.65.1@bincrafters/testing",
        "boost_core/1.65.1@bincrafters/testing",
        "boost_detail/1.65.1@bincrafters/testing",
        "boost_endian/1.65.1@bincrafters/testing",
        "boost_exception/1.65.1@bincrafters/testing",
        "boost_filesystem/1.65.1@bincrafters/testing",
        "boost_foreach/1.65.1@bincrafters/testing",
        "boost_function/1.65.1@bincrafters/testing",
        "boost_function_types/1.65.1@bincrafters/testing",
        "boost_functional/1.65.1@bincrafters/testing",
        "boost_fusion/1.65.1@bincrafters/testing",
        "boost_integer/1.65.1@bincrafters/testing",
        "boost_intrusive/1.65.1@bincrafters/testing",
        "boost_io/1.65.1@bincrafters/testing",
        "boost_iostreams/1.65.1@bincrafters/testing",
        "boost_iterator/1.65.1@bincrafters/testing",
        "boost_lexical_cast/1.65.1@bincrafters/testing",
        "boost_math/1.65.1@bincrafters/testing",
        "boost_move/1.65.1@bincrafters/testing",
        "boost_mpl/1.65.1@bincrafters/testing",
        "boost_optional/1.65.1@bincrafters/testing",
        "boost_phoenix/1.65.1@bincrafters/testing",
        "boost_predef/1.65.1@bincrafters/testing",
        "boost_preprocessor/1.65.1@bincrafters/testing",
        "boost_proto/1.65.1@bincrafters/testing",
        "boost_range/1.65.1@bincrafters/testing",
        "boost_regex/1.65.1@bincrafters/testing",
        "boost_smart_ptr/1.65.1@bincrafters/testing",
        "boost_static_assert/1.65.1@bincrafters/testing",
        "boost_system/1.65.1@bincrafters/testing",
        "boost_throw_exception/1.65.1@bincrafters/testing",
        "boost_tokenizer/1.65.1@bincrafters/testing",
        "boost_tti/1.65.1@bincrafters/testing",
        "boost_tuple/1.65.1@bincrafters/testing",
        "boost_type_traits/1.65.1@bincrafters/testing",
        "boost_typeof/1.65.1@bincrafters/testing",
        "boost_unordered/1.65.1@bincrafters/testing",
        "boost_utility/1.65.1@bincrafters/testing",
        "boost_variant/1.65.1@bincrafters/testing",
        "boost_winapi/1.65.1@bincrafters/testing"
    )

    def requirements(self):
        if self.options.use_icu:
            self.requires("icu/59.1@bincrafters/stable")

    def b2_options(self, lib_name=None):
        # pylint: disable=unused-argument
        if self.options.use_icu:
            return " boost.locale.iconv=off boost.locale.icu=on"
        else:
            return " boost.locale.icu=off"

    def package_info_additional(self):
        if self.options.use_icu:
            self.cpp_info.defines.append("BOOST_LOCALE_WITH_ICU=1")
        elif self.settings.os == "Macos":
            self.cpp_info.libs.append("iconv")
        if self.settings.os != "Windows":
            self.cpp_info.libs.append("pthread")

    def package_id_additional(self):
        boost_deps_only = [dep_name for dep_name in self.info.requires.pkg_names if dep_name.startswith("boost_")]

        for dep_name in boost_deps_only:
            self.info.requires[dep_name].full_version_mode()

    # BEGIN

    description = "Please visit http://www.boost.org/doc/libs/1_65_1"
    license = "BSL-1.0"
    short_paths = True
    generators = "boost"
    settings = "os", "arch", "compiler", "build_type"
    build_requires = "boost_generator/1.65.1@bincrafters/testing"

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
