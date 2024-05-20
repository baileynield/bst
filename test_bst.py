import pytest

from bst import BST


@pytest.fixture
def tree() -> BST:
    tree = BST()
    tree.insert(4)
    tree.insert(6)
    tree.insert(7)
    tree.insert(11)
    return tree


def test_insert():
    tree = BST()
    assert tree.search(5) == False
    tree.insert(5)
    assert tree.search(5)
    assert tree.root is not None
    assert tree.root.value == 5


def test_search(tree: BST):
    assert tree.root is not None
    assert tree.root.value == 4
    assert tree.search(8) == False
    assert tree.search(4) == True
    assert tree.search(7) == True
    assert tree.search(11) == True
    assert tree.search(6) == True
    assert tree.search(0) == False


def test_in_order_traversal(tree: BST):
    expected = [4, 6, 7, 11]
    actual = tree.in_order_traversal()
    assert expected == actual
 
 
def test_find_min(tree: BST):
    expected = 4
    actual = tree.find_min()
    assert expected == actual
 

def test_find_max(tree: BST):
    expected = 11
    actual = tree.find_max()
    assert expected == actual


def test_height(tree: BST):
    expected = 4
    actual = tree.height()
    assert tree.root is not None
    assert expected == actual


def test_count_leaves(tree: BST):
    expected = 1
    actual = tree.count_leaves()
    print(tree)
    assert expected == actual


def test_serialize(tree: BST):
    expected = "4\xa06\xa07\xa011"
    actual = tree.serialize()
    assert expected == actual


def test_deserialize():
    tree = BST()
    nums = "4\xa06\xa07\xa011"
    tree.deserialize(nums)
    assert tree.root.value == 4
    assert tree.root.left == None
    assert tree.root.right.value == 6
    assert tree.root.right.left == None
    assert tree.root.right.right.value == 7
    assert tree.root.right.right.left == None
    assert tree.root.right.right.right.value == 11
    assert tree.root.right.right.right.left == None
    assert tree.root.right.right.right.right == None
