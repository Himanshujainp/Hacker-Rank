
  struct node
  {
     int data;
     struct node *next;
  }node;

void Print(Node *head)
{
  // This is a "method-only" submission. 
  // You only need to complete this method. 
    if(head!=NULL)
        {
        Node *temp=head;
        while(temp!=NULL){
            printf("%d\n",temp->data);
            temp=temp->next;
        }
        
    }
}
