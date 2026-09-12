class Node {
    int key;
    int val;
    Node prev;
    Node next;

    public Node(int key, int val) {
        this.key = key;
        this.val = val;
        this.prev = null;
        this.next = null;
    }
}

class LRUCache {
    private int capacity;
    private HashMap<Integer, Node> cache;
    private Node left;
    private Node right;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new HashMap<>();

        // Dummy nodes
        this.left = new Node(0, 0);
        this.right = new Node(0, 0);

        this.left.next = this.right;
        this.right.prev = this.left;
    }

    // Remove node from linked list
    public void remove(Node node) {
        Node prev = node.prev;
        Node next = node.next;

        prev.next = next;
        next.prev = prev;
    }

    // Insert node at the right (most recently used)
    public void insert(Node node) {
        Node prev = this.right.prev;
        Node next = this.right;

        prev.next = node;
        next.prev = node;

        node.prev = prev;
        node.next = next;
    }

    public int get(int key) {
        if (cache.containsKey(key)) {
            Node node = cache.get(key);

            // Move to most recently used
            remove(node);
            insert(node);

            return node.val;
        }

        return -1;
    }

    public void put(int key, int value) {
        if (cache.containsKey(key)) {
            Node node = cache.get(key);

            // Remove old node
            remove(node);
        }

        Node node = new Node(key, value);
        cache.put(key, node);
        insert(node);

        // Evict least recently used
        if (cache.size() > capacity) {
            Node lru = left.next;

            remove(lru);
            cache.remove(lru.key);
        }
    }
}