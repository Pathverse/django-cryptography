VERSION = (2, 0, 0, "alpha", 0)


def _get_version(version):
    main = ".".join(str(value) for value in version[:3])
    stage = version[3]
    serial = version[4]

    if stage == "final":
        return main

    suffixes = {
        "alpha": "a",
        "beta": "b",
        "rc": "rc",
    }
    return f"{main}{suffixes[stage]}{serial}"


__version__ = _get_version(VERSION)
