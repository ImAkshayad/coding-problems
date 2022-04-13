class IsPathExists {
    // DFS Approach to find if a path exists in graph
    public boolean seen;
    public boolean validPath(int n, int[][] edges, int source, int destination) {

        boolean[] visited=new boolean[n];
        HashSet<Integer>[] graph=new HashSet[n];
        int i,j;
        for(i=0;i<n;i++)
            graph[i]=new HashSet<Integer>();

        for(int[] edge: edges)
        {
            graph[edge[0]].add(edge[1]);
            graph[edge[1]].add(edge[0]);
        }

        if(graph[source].contains(destination))
            return true;

        seen=false;
        dfs(graph,visited,source,destination);
        return seen;
    }
    private void dfs(HashSet<Integer>[] graph,boolean[] visited,int source, int destination)
    {
        if(!visited[source])
            if(source==destination)
            {
                seen=true;
                return;
            }

        visited[source]=true;
        if(graph[source].size()!=0)
            for(Integer neighbor:graph[source])
                if(visited[neighbor]==false)
                {
                    dfs(graph,visited,neighbor,destination);
                }
    }
}