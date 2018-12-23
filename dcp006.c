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
#include <inttypes.h>


typedef struct Node {
    int val;
    struct Node* both;
} Node;


Node* xor(Node *a, Node *b)
{
  return (Node *)((uintptr_t) (a) ^ (uintptr_t)(b));
}


Node* add(Node **head_ref, int element)
{
  Node *new_node = (Node *)malloc(sizeof(Node));
  new_node->val = element;

  if (*head_ref != NULL) {
    Node *prev = xor((*head_ref)->both, NULL);
    (*head_ref)->both = xor(prev, new_node);
    new_node->both = xor(*head_ref, NULL);
  }

  *head_ref = new_node;
  return new_node;
}

int get(Node *head, int index)
{
  int i;
  Node *prev = NULL;
  Node *curr = head;
  Node *next;
  for (i = 0; i < index; i++) {
    next = xor(prev, curr->both);
    prev = curr;
    curr = next;
  }

  return curr->val;
}


int main()
{
  Node *head = NULL;
  Node *tail = NULL;
  tail = add(&head, 10);
  add(&head, 20);
  add(&head, 30);
  add(&head, 40);

  for (int i=0; i<4; i++) {
    printf("index %d = %d\n", i, get(tail, i));
  }
  return 0;
}
