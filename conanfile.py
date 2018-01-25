#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class BoostLevel11GroupConan(ConanFile):
    name = "boost_level11group"
    version = "1.66.0"
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
        "boost_package_tools/1.66.0@bincrafters/stable",
        "boost_algorithm/1.66.0@bincrafters/stable",
        "boost_array/1.66.0@bincrafters/stable",
        "boost_assert/1.66.0@bincrafters/stable",
        "boost_atomic/1.66.0@bincrafters/stable",
        "boost_bind/1.66.0@bincrafters/stable",
        "boost_chrono/1.66.0@bincrafters/stable",
        "boost_concept_check/1.66.0@bincrafters/stable",
        "boost_config/1.66.0@bincrafters/stable",
        "boost_container/1.66.0@bincrafters/stable",
        "boost_core/1.66.0@bincrafters/stable",
        "boost_detail/1.66.0@bincrafters/stable",
        "boost_endian/1.66.0@bincrafters/stable",
        "boost_exception/1.66.0@bincrafters/stable",
        "boost_filesystem/1.66.0@bincrafters/stable",
        "boost_foreach/1.66.0@bincrafters/stable",
        "boost_function/1.66.0@bincrafters/stable",
        "boost_function_types/1.66.0@bincrafters/stable",
        "boost_functional/1.66.0@bincrafters/stable",
        "boost_fusion/1.66.0@bincrafters/stable",
        "boost_integer/1.66.0@bincrafters/stable",
        "boost_intrusive/1.66.0@bincrafters/stable",
        "boost_io/1.66.0@bincrafters/stable",
        "boost_iostreams/1.66.0@bincrafters/stable",
        "boost_iterator/1.66.0@bincrafters/stable",
        "boost_lexical_cast/1.66.0@bincrafters/stable",
        "boost_math/1.66.0@bincrafters/stable",
        "boost_move/1.66.0@bincrafters/stable",
        "boost_mpl/1.66.0@bincrafters/stable",
        "boost_optional/1.66.0@bincrafters/stable",
        "boost_phoenix/1.66.0@bincrafters/stable",
        "boost_predef/1.66.0@bincrafters/stable",
        "boost_preprocessor/1.66.0@bincrafters/stable",
        "boost_proto/1.66.0@bincrafters/stable",
        "boost_range/1.66.0@bincrafters/stable",
        "boost_regex/1.66.0@bincrafters/stable",
        "boost_smart_ptr/1.66.0@bincrafters/stable",
        "boost_static_assert/1.66.0@bincrafters/stable",
        "boost_system/1.66.0@bincrafters/stable",
        "boost_throw_exception/1.66.0@bincrafters/stable",
        "boost_tokenizer/1.66.0@bincrafters/stable",
        "boost_tti/1.66.0@bincrafters/stable",
        "boost_tuple/1.66.0@bincrafters/stable",
        "boost_type_traits/1.66.0@bincrafters/stable",
        "boost_typeof/1.66.0@bincrafters/stable",
        "boost_unordered/1.66.0@bincrafters/stable",
        "boost_utility/1.66.0@bincrafters/stable",
        "boost_variant/1.66.0@bincrafters/stable",
        "boost_winapi/1.66.0@bincrafters/stable"
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

    # BEGIN

    description = "Please visit http://www.boost.org/doc/libs/1_66_0"
    license = "BSL-1.0"
    short_paths = True
    generators = "boost"
    settings = "os", "arch", "compiler", "build_type"
    build_requires = "boost_generator/1.66.0@bincrafters/stable"

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
