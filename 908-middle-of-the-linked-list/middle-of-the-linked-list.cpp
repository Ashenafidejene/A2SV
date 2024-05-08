/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* fastes = head; 
        ListNode* slowest = head; 
        while (fastes != nullptr && fastes->next != nullptr) {
            slowest = slowest->next;
            fastes = fastes->next->next;
        }
        return slowest;
    }
};
