#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostLevel11GroupConan(base.BoostBaseConan):
    # This is now Level 15
    name = "boost_level11group"
    url = "https://github.com/bincrafters/conan-boost_level11group"
    lib_short_names = ["date_time", "pool", "serialization", "spirit", "thread"]
    header_only_libs = ["pool", "spirit"]
    options = {"shared": [True, False]}
    default_options = "shared=False"
    b2_requires = [
        "boost_algorithm",
        "boost_array",
        "boost_assert",
        "boost_atomic",
        "boost_bind",
        "boost_chrono",
        "boost_concept_check",
        "boost_config",
        "boost_container",
        "boost_container_hash",
        "boost_core",
        "boost_detail",
        "boost_endian",
        "boost_exception",
        "boost_filesystem",
        "boost_foreach",
        "boost_function",
        "boost_function_types",
        "boost_fusion",
        "boost_integer",
        "boost_intrusive",
        "boost_io",
        "boost_iostreams",
        "boost_iterator",
        "boost_lexical_cast",
        "boost_math",
        "boost_move",
        "boost_mpl",
        "boost_numeric_conversion",
        "boost_optional",
        "boost_phoenix",
        "boost_predef",
        "boost_preprocessor",
        "boost_proto",
        "boost_range",
        "boost_regex",
        "boost_smart_ptr",
        "boost_static_assert",
        "boost_system",
        "boost_throw_exception",
        "boost_tokenizer",
        "boost_tti",
        "boost_tuple",
        "boost_type_traits",
        "boost_typeof",
        "boost_unordered",
        "boost_utility",
        "boost_variant",
        "boost_winapi"
    ]

    def package_info_additional(self):
        if self.settings.os != "Windows":
            self.cpp_info.libs.append("pthread")


