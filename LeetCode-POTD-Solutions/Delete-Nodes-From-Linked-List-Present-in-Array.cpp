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
    ListNode* modifiedList(vector<int>& nums, ListNode* head) {
        unordered_set<int> toRemove(nums.begin(), nums.end());
        ListNode dummy(0, head);
        ListNode* prev = &dummy;
        while (prev->next != nullptr) {
            if (toRemove.count(prev->next->val)) {
                prev->next = prev->next->next;
            } else {
                prev = prev->next;
            }
        }
        return dummy.next;
    }
};
