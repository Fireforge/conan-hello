# conan-hello
"Hello world" project for testing Conan build and package setups 

This is test package to see how simply I could set up Conan, CMake, and Visual Studio Code to build and debug 

## One-time Setup

Build dependencies:
- Install Python (3.5 or later)
- Install CMake
- Install the build tool:  
    - **Windows:** Visual C++ Build Tools (http://landinghub.visualstudio.com/visual-cpp-build-tools)  
      *Note: If you already have Visual Studio installed, you can skip this step. Also, when installing Visual C++ Build Tools, you may need to include the optional Windows SDK. I needed it to build on Windows 10.*
- `pip install conan`

## Build Default Configuration

A single command builds it:
```
conan build
```

Outputs go into the `exports` folder.

## Details

This repo is set up for editor debugging in Visual Studio Code: https://code.visualstudio.com/.
- `ctrl+shift+B` builds the project
- `F5` runs the Debug build with breakpoint debugging enabled

More detailed official docs for C/C++ in VS Code is here: https://code.visualstudio.com/docs/languages/cpp

## TODO

- [ ] Cross-platform, current config is for Windows only
- [ ] Set up a trivial package test run by `conan test_package`
- [ ] Set up a trivial unit tests that get run on `conan build`
- [ ] Find an easy way to do configure a "clean" function
