
class SimpleHTTPRequestHandlerFake:
    def __init__(self, name):
        self.name = name

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.root.handler = handler


    def insert(self, lst, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        
        for word in lst:
            if word not in current_node.children:
                current_node.children[word] = RouteTrieNode()
            current_node = current_node.children[word]
        
        current_node.handler = handler

    def find(self, lst):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root

        if lst[-1] == '': # normalize for final slash cases
            lst = lst[:-1]
        
        if lst == ['']: # / root case
            return self.root.handler

        for word in lst:
            if word not in current_node.children:
                return None
            current_node = current_node.children[word]
        
        return current_node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None

    def insert(self):
        # Insert the node as before
        pass

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_msg, pnf_msg):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routeTrie = RouteTrie(SimpleHTTPRequestHandlerFake(root_msg))
        self.pnf_handler = SimpleHTTPRequestHandlerFake(pnf_msg)

    def add_handler(self, path, handler_msg):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.routeTrie.insert(self.split_path(path), SimpleHTTPRequestHandlerFake(handler_msg))

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        handler = self.routeTrie.find(self.split_path(path))
        if handler is not None:
            return handler.name
        else:
            return self.pnf_handler.name

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return path.split("/")



# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one