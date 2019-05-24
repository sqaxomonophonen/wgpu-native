This is an active GitHub mirror of the WebGPU native implementation in Rust, which now lives in [Mozilla-central](https://hg.mozilla.org/mozilla-central). Issues and pull requests are accepted, but we merge them in m-c manually and then sync to GitHub instead of landing directly here.

---
# WebGPU
[![Build Status](https://travis-ci.org/gfx-rs/wgpu.svg)](https://travis-ci.org/gfx-rs/wgpu)
[![Crates.io](https://img.shields.io/crates/v/wgpu-native.svg?label=wgpu-native)](https://crates.io/crates/wgpu-native)
[![Gitter](https://badges.gitter.im/gfx-rs/webgpu.svg)](https://gitter.im/gfx-rs/webgpu)

This is an experimental [WebGPU](https://www.w3.org/community/gpu/) implementation as a native static library. It's written in Rust and is based on [gfx-hal](https://github.com/gfx-rs/gfx) and [Rendy](https://github.com/amethyst/rendy) libraries. The corresponding WebIDL specification can be found at [gpuweb project](https://github.com/gpuweb/gpuweb/blob/master/spec/index.bs).

The implementation consists of the following parts:
  1. `wgpu-native` - the native implementation of WebGPU as a C API library
  2. `wgpu-remote` - remoting layer to work with WebGPU across the process boundary
  3. `ffi` - the C headers generated by [cbindgen](https://github.com/eqrion/cbindgen) for both of the libraries

Supported platforms:
  - Vulkan on Windows and Linux
  - D3D12 and D3D11 on Windows
  - Metal on macOS and iOS

## Usage

This repository contains C-language examples that link to the native library targets and perform basic rendering and computation.
To run the C triangle example, install a C compiler + glfw 3, then run these commands at the root of the repo:
```
rustup toolchain install nightly
cargo install cbindgen
make examples-native
cd examples/hello_triangle_c/build
./hello_triangle
```

The idiomatic Rust wrapper lives in https://github.com/gfx-rs/wgpu-rs and provides a number of more complex examples to get a feel of the API.