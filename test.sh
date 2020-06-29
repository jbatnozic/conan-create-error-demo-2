#! /bin/bash

   conan create ./package-1/ 1.0@error/test --profile=default --build=outdated \
&& conan create ./package-2/ 1.0@error/test --profile=default --build=outdated \
&& conan create ./package-3/ 1.0@error/test --profile=default -o package-3:shared=True --build=outdated \
&& conan create ./package-3/ 1.0@error/test --profile=default -o package-3:shared=True --build=libcurl