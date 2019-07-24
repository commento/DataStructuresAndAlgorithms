class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.users:
        return True

    result = False
    for gr in group.groups:
        value = is_user_in_group(user, gr)
        if value is True:
            result = True

    return result

print("#Test 1: Check parent for subchild user")

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group(sub_child_user, parent)) # True

print("#Test 2: Check absence subchild user in empty parent")

child2 = Group("child2")
print(is_user_in_group(sub_child_user, child2)) # False

print("#Test 3: Check user in same level group")

child2_user = "child2_user"
child2.add_user(child2_user)
print(is_user_in_group(child2_user, child2)) # True
