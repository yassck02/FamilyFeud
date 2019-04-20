import urwid
import json 
 
class ExampleTreeWidget(urwid.TreeWidget):
    """ Display widget for leaf nodes """

    def get_display_text(self):
        return self.get_node().get_value()["name"]

class ExampleNode(urwid.TreeNode):
    """ Data storage object for leaf nodes """

    def load_widget(self):
        return ExampleTreeWidget(self)
 
class ExampleParentNode(urwid.ParentNode ):
    """ Data storage object for interior/parent nodes """

    def load_widget(self):
        return ExampleTreeWidget(self)

    def load_child_keys(self):
        data = self.get_value()
        return range(len(data["children"]))

    def load_child_node(self, key):
        """Return either an ExampleNode or ExampleParentNode"""

        childdata = self.get_value()["children"][key]
        childdepth = self.get_depth() + 1

        if "children" in childdata:
            childclass = ExampleParentNode
        else:
            childclass = ExampleNode

        return childclass(childdata, parent=self, key=key, depth=childdepth)

class ExampleTreeBrowser:

    def __init__(self, data=None):

        self.topnode = ExampleParentNode(data)
        self.listbox = urwid.TreeListBox(urwid.TreeWalker(self.topnode))
        self.listbox.offset_rows = 1

        self.view = urwid.Frame(
            self.listbox,
            header = urwid.Text( "header" ), 
            footer = urwid.Text( "footer" )
        )

    def main(self):
        """Run the program"""

        self.loop = urwid.MainLoop(self.view, [], unhandled_input = self.unhandled_input)
        self.loop.run()
 
    def unhandled_input(self, k):
        if k in ('q','Q'):
            raise urwid.ExitMainLoop()


def generateTree():
    """generate a quick 100 leaf tree for demo purposes"""

    users_file_path = "/Users/Connor/Documents/School/College/Semester 8/Networking/FamilyFeud/dat/users.json"
    users_file = open(users_file_path, "r").read()
    users = json.loads(users_file)

    root = {
        "name": "Users",
        "children": []
    }

    for user in users: 
        user_node = {
            "name": user["username"],
            "children": []
        }

        for history in user["history"]:

            history_node = {
                "name": history['date'] + ": " + str(history['score']),
                "children": []
            }

            user_node["children"].append(history_node)

        root["children"].append(user_node)

    return root
 
sample = generateTree()
ExampleTreeBrowser(sample).main()
 