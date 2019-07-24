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
    os.chdir(path)
    list_dir = os.listdir(path)
    output = []

    for elem in list_dir:
      if os.path.isdir(elem):
        output.extend(find_files(suffix, path + '/' + elem))
        os.chdir(path)
      if elem.endswith(suffix):
        elem_path = path + '/' + elem
        output.append(elem_path)

    return output

# absolute path to be adjusted in order to correctly run the tests
abs_path = "/Users/riccardo/Documents/P1"
#Test 1
print("#Test 1")
print(find_files("c", abs_path))

#Test 2
print("#Test 2")
print(find_files("h", abs_path))

#Test 3
print("#Test 3")
print(find_files("cpp", abs_path))