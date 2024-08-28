from ParseTuneResults import parse_tune_results


# changed replacement strategy: search for the param name instead of the original value
# so this version only works for the tune version
def apply_search_tune_results_by_name(search_cpp, tune_results):
    tune_results = parse_tune_results(tune_results)
    
    with open(search_cpp, 'r') as f:
        file = f.read()
        
    cnt = 0
    
    for param in tune_results:
        name, value, original_value = param
        
        # search file for the NAME
        # if there is only 1 match, replace it with the tuned value
        if file.count(str(name)) == 1:
            file = file.replace(str(name), str(value))
            cnt += 1
        else:
            print(f"{name}, {original_value} -> {value}")
        
    new_path = search_cpp.replace(".cpp", "_tuned.cpp")
    with open(new_path, 'w') as f:
        f.write(file)
        
    print(f"Applied {cnt} results to {new_path}")
        

if __name__ == "__main__":
    apply_search_tune_results_by_name("tune_search.cpp", "tune_results_230824_67.5k.txt")