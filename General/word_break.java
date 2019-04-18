class Solution {
    public List<String> wordBreak(String s, List<String> wordDict) {
    return backtrack(s,wordDict,new HashMap<String, List<String>>());
}
// backtrack returns an array including all substrings derived from s.
public List<String> backtrack(String s, List<String> wordDict, Map<String,List<String>> mem){
    if(mem.containsKey(s)) return mem.get(s);
    List<String> result = new ArrayList<String>();
    for(String word: wordDict)
        if(s.startsWith(word)) {
            String next = s.substring(word.length());
            if(next.length()==0) result.add(word);
            else for(String sub: backtrack(next, wordDict, mem)) result.add(word+" "+sub);
        }
    mem.put(s, result);
    return result;
	}
}




/*

public class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> wordDictSet=new HashSet(wordDict);
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;
        for (int i = 1; i <= s.length(); i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] && wordDictSet.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[s.length()];
    }
}

*/