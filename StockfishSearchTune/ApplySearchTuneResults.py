from ParseTuneResults import parse_tune_results


def apply_search_tune_results(search_cpp, tune_results):
    tune_results = parse_tune_results(tune_results)
    
    with open(search_cpp, 'r') as f:
        file = f.read()
        
    cnt = 0
    
    for param in tune_results:
        name, value, original_value = param
        
        if value == original_value:
            cnt += 1
            continue
        
        # search file for the original value
        # if there is only 1 match, replace it with the tuned value
        if file.count(str(original_value)) == 1:
            file = file.replace(str(original_value), str(value))
            cnt += 1
        else:
            print(f"{name}, {original_value} -> {value}")
        
    new_path = search_cpp.replace(".cpp", "_tuned.cpp")
    with open(new_path, 'w') as f:
        f.write(file)
        
    print(f"Applied {cnt} results to {new_path}")
        

if __name__ == "__main__":
    # apply_search_tune_results("search.cpp", "tune_results_230824_31k.txt")
    apply_search_tune_results("tune_header.cpp", "results/tune_results_20250102_118k.txt")
