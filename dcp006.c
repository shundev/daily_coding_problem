/*
This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list.
Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node.
Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python),
you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
*/

#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int val;
    struct Node* both;
} Node;

typedef struct {
    Node *head;
    Node *tail;
    int size;
} XORLinkedList;

Node *new_node(int val)
{
    Node *node = calloc(1, sizeof(node));
    node->val = val;
    return node;
}

XORLinkedList *new_linked_list()
{
    XORLinkedList *ll = calloc(1, sizeof(XORLinkedList));
    ll->size = 0;
    return ll;
}

void add(XORLinkedList *ll, int element)
{
    Node *node = new_node(element);
    if (ll->size == 0) {
        ll->head = node;
        ll->tail = node;
    } else {
        ll->head->both = node;
        ll->head = node;
    }
    
    ll->size++;
}

int get(XORLinkedList *ll, int index)
{
    if (index >= ll->size) {
        fprintf(stderr, "Out of index: index=%d size=%d", index, ll->size);
        exit(1);
    }
    
    Node *node = ll->tail;
    for (int i=0; i<index; i++) {
        node = node->both;
    }
    
    return node->val;
}

void check(int actual, int expected)
{
  if (actual != expected) {
    fprintf(stderr, "Expected %d, but got %d\n", expected, actual);
    exit(1);
  }

  printf("OK\n");
}

int main(void){
    XORLinkedList *ll = new_linked_list();
    add(ll, 10);
    add(ll, 20);
    add(ll, 30);
    add(ll, 40);
    add(ll, 50);

    check(get(ll, 0), 10);
    check(get(ll, 2), 30);
    check(get(ll, 4), 50);
}
