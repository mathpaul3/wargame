from base64 import (
    b16decode,
    b16encode,
    b32decode,
    b32encode,
    b64decode,
    b64encode,
    b85decode,
    b85encode,
)
from typing import Literal, Callable, get_args

MethodLiteral = Literal["base16", "base32", "base64", "base85", "custom"]


def decode(
    string,
    method: MethodLiteral,
    form: Literal["string", "hex"] = "string",
    iteration: int = 1,
    custom_func: Callable[[str], str] = None,
    print_step: int = 0,
) -> str:
    if method not in list(get_args(MethodLiteral)):
        raise RuntimeError("No method selected!")
    for iter in range(iteration):
        if method == "base16":
            string = b16decode(bytes(string, "utf-8")).decode("utf-8")
        elif method == "base32":
            string = b32decode(bytes(string, "utf-8")).decode("utf-8")
        elif method == "base64":
            string = b64decode(bytes(string, "utf-8")).decode("utf-8")
        elif method == "base85":
            string = b85decode(bytes(string, "utf-8")).decode("utf-8")
        elif method == "custom":
            if custom_func == None:
                raise RuntimeError("No custom function!")
            string = custom_func(string)
        if print_step and not iter % print_step:
            print(f"Iteration {iter+1}: {string}")
    return string


if __name__ == "__main__":
    string = "Vm0wd2QyUXlWa1pPVldoVFYwZFNUMVpzWkZOWFZsbDNXa1JTVjFac2JETlhhMXBQVm14S2MxWnFUbGhoTVVwVVZtcEtTMUl5U2tWVWJHaG9UVlZ3VlZadE1UUlpWMDE1Vkd0c2FGSnNjSEJXYTFwaFpWWmtWMVp0UmxSTmF6RTFWVEowVjFaWFNrbFJiR2hYWWxob00xWldXbXRXTVdSMFVteHdWMDFWY0VsV2JUQXhWREpHVjFOdVRsaGlSMmhoV1ZSR2QwMHhjRmRYYlhSWVVqRktTVnBGV2xOVWJGcFZWbXhzVjFaNlFYaFdSRVpyVTBaT2NtRkdXbWhsYlhoWlYxZDRiMVV3TUhoV2JrNVlZbGhTV1ZWcVJtRlRWbFowWlVkMFZXSkdjREZWVjNodlZqRktjMk5HYUZkaGEzQklWVEJhWVdSV1NuTlRiR1JUVFRBd01RPT0="
    print(decode(string, "base64", iteration=15, print_step=1))
