import os
import re

def check_unimplemented_functions():
    fnset = set()

    def xfn(s):
        xs = s.split("(")
        if len(xs) < 2: return None
        fn = xs[0]
        if not fn.startswith("wgpu"): return None
        return fn

    def see_fn(s):
        fn = xfn(s)
        if fn is not None:
            fnset.add(fn)

    with open("ffi/webgpu-headers/webgpu.h", "rb") as f:
        for line in f.read().decode().splitlines():
            if not line.startswith("WGPU_EXPORT"):
                continue
            tup = line.split(" ")
            if len(tup) < 2:
                continue
            see_fn(tup[2])

    with open("ffi/wgpu.h", "rb") as f:
        for line in f.read().decode().splitlines():
            tup = line.split(" ")
            if len(tup) < 2:
                continue
            see_fn(tup[1])

    impl_re = re.compile("^pub .*extern \"C\" fn (wgpu[a-zA-Z]+)\(")
    for fname in os.listdir("src"):
        if not fname.endswith(".rs"):
            continue
        path = os.path.join("src", fname)
        with open(path, "rb") as f:
            for line in f.read().decode().splitlines():
                mo = impl_re.match(line)
                if mo is None: continue
                fn = mo[1]
                if fn in fnset:
                    fnset.remove(fn)

    fails = []
    if len(fnset) > 0:
        fails.append(f"✖ %d unimplemented webgpu.h / wgpu.h functions:" % len(fnset))
        for fn in sorted(fnset):
            fails.append(f"  %s()" % fn)

    return fails

for f in check_unimplemented_functions(): print(f)

