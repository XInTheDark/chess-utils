from ParseTuneResults import parse_tune_results


# changed replacement strategy: search for the param name instead of the original value
# so this version only works for the tune version
def apply_search_tune_results_by_name(search_cpp, tune_results):
    tune_results = parse_tune_results(tune_results)

    with open(search_cpp, 'r') as f:
        file = f.read()

    cnt = 0

    remaining = tune_results.copy()

    # optimisation: sort params by length (longest first) to reduce number of passes
    remaining.sort(key=lambda x: len(x[0]), reverse=True)

    while True:
        replaced = False

        for param in remaining:
            name, value, original_value = param

            # search file for the NAME
            # if there is only 1 match, replace it like this:
            # "name = old_value" -> "name = new_value"
            if file.count(f"{name} =") == 1:
                file = file.replace(f"{name} = {original_value}", f"{name} = {value}")
                cnt += 1
                replaced = True
                remaining.remove(param)

        if not replaced:
            break

    for param in remaining:
        name, value, original_value = param
        print(f"{name}, {original_value} -> {value}")

    new_path = search_cpp.replace(".cpp", "_tuned.cpp")
    with open(new_path, 'w') as f:
        f.write(file)

        # then, write the TUNE macro
        f.write("\n\n")
        f.write("TUNE(")
        for i in range(len(tune_results)):
            name = f"a{i + 1}"
            f.write(f"{name}{', ' if i < len(tune_results) - 1 else ''}")
        f.write(");")

    print(f"Applied {cnt} results to {new_path} (Total: {len(tune_results)})")


if __name__ == "__main__":
    apply_search_tune_results_by_name("tune_header.cpp", "results/tune_results_20250102_118k.txt")
