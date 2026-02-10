import java.util.*;

class Solution {
    public int minimumPairRemoval(int[] nums) {
        List<Long> arr = new ArrayList<>();
        for (int x : nums) arr.add((long) x);

        int ops = 0;

        while (true) {
            boolean ok = true;
            for (int i = 1; i < arr.size(); i++) {
                if (arr.get(i) < arr.get(i - 1)) {
                    ok = false;
                    break;
                }
            }
            if (ok) break;

            long minSum = Long.MAX_VALUE;
            int idx = 0;
            for (int i = 0; i < arr.size() - 1; i++) {
                long s = arr.get(i) + arr.get(i + 1);
                if (s < minSum) {
                    minSum = s;
                    idx = i;
                }
            }

            long merged = arr.get(idx) + arr.get(idx + 1);
            arr.remove(idx + 1);
            arr.set(idx, merged);
            ops++;
        }
        return ops;
    }
}
