import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    return get_file_files(suffix, path, [])

def get_file_files(suffix, path, list_paths):

    # check if suffix is empty 
    if suffix == "":
        return []

    # check if the test folder is empty
    if len(os.listdir(path)) == 0:
        return []

    list_items = os.listdir(path)

    for item in list_items:
        new_path = os.path.join(path, item)
        if os.path.isdir(new_path):
            get_file_files(suffix, new_path, list_paths)
        
        if os.path.isfile(new_path):
            if new_path.endswith(suffix):
                list_paths.append(new_path)

    return sorted(list_paths)


######################################## Test ##################################################

def test_function(test_case):
    output = find_files(test_case[0], test_case[1])
    expected_output = test_case[2]
    if expected_output == output:
        print("Pass")
    else:
        print("Fail")

## Test 1 
test_case1 = (".c", "../testdir", ['../testdir/subdir1/a.c', '../testdir/subdir3/subsubdir1/b.c', '../testdir/subdir5/a.c', '../testdir/t1.c'])
test_function(test_case1)  # return Pass

## Test 2
test_case2 = (".c", "../emptydir", [])
test_function(test_case2)  # return Pass

## Test 3
test_case3 = (".b", "../testdir", [])
test_function(test_case3)  # return Pass



    

