//
// Created by caizixiang on 2019-07-30.
//

#include <iostream>
#include <queue>
#include <deque>

using namespace std;

int main()
{
    // usage of queue
    queue<int> myQueue;
    cout << "queue" << endl;
    cout << myQueue.empty() << endl;
    cout << myQueue.size()<< endl;
    myQueue.push(1);
    myQueue.push(2);
    myQueue.push(3);
    cout << myQueue.front()<<endl;
    cout << myQueue.back()<<endl;
    myQueue.pop();// pop the first element from the front, return void
    cout << myQueue.front()<<endl;
    cout << myQueue.back()<<endl;

    // usage of deque
    deque<int> myDeque;
    cout << "deque" << endl;
    myDeque.push_front(1);
    myDeque.push_front(2);
    myDeque.push_back(3);
    myDeque.push_back(4);
    myDeque.push_back(5);
    myDeque.push_front(6);
    myDeque.pop_back();// pop the first element from the back, return void
    myDeque.pop_front();// pop the first element from the front, return void
    deque<int>::iterator myItor;
    for(myItor=myDeque.begin(); myItor!=myDeque.end(); myItor++)
        cout<<*myItor<<endl;

    return 0;
}
