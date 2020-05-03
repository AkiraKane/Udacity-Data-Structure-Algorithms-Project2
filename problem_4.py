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

    if user in group.get_users():
        return True
    
    elif len(group.get_groups()) != 0:
        for child_group in group.get_groups():
            isfound = is_user_in_group(user, child_group)
            if isfound:
                return True

    return False


########################################### Test Function ################################################

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

def test_function(test_case):
    output = is_user_in_group(test_case[0], test_case[1])
    expected_output = test_case[2]
    if output == expected_output:
        print("Pass")
    else:
        print("Fail")

test_case1 = (sub_child_user, parent, True)
test_function(test_case1)    # return Pass

test_case2 = ("parent", parent, False)
test_function(test_case2)    # return Pass

test_case3 = ("parent", child, False)
test_function(test_case3)    # return Pass

test_case4 = ("parent", sub_child, False)
test_function(test_case4)    # return Pass

# Now if I add "child" user name in child group
child_user = "child"
child.add_user(child_user)

test_case5 = (child_user, parent, True)
test_function(test_case5)    # return Pass

test_case6 = (child_user, child, True)
test_function(test_case6)    # return Pass

test_case7 = (child_user, sub_child, False)
test_function(test_case7)    # return Pass

