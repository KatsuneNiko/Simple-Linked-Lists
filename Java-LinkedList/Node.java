public class Node<X> {
	
	private X data;
	private Node<X> next;
	
	public Node(X data) {
		this(data, null);
	}
	
	public Node(X data, Node next) {
		this.data = data;
		this.next = next;
	}
	
	public X getData() {
		return this.data;
	}
	
	public void setNext(Node next) {
		this.next = next;
	}
	
	public Node<X> getNext() {
		return this.next;
	}
	
	@Override
	public String toString() {
		return "[Node: " + this.data + "]";
	}

}
