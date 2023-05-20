/*
Make Graph generator
<FUNCTIONAL REQUIREMENT>
1. It should add edge, vertices
2. It should contains traversal function such as bfs, and dfs
*/
#include <stdio.h>
#include <vector>
#include <queue>
#include <stack>
using namespace std;

class Graph{
private:
    int Num_vertex;
    int Num_edges;
    vector<vector<int>> adjlist; 
    vector<char> checklist;
    void dfs(int beginV)
    {
        for (int idxV:adjlist[beginV])
        {
            if (checklist[idxV] == 0)
            {
                checklist[idxV] = 1;
                printf("%d ",idxV);
                dfs(idxV);
            }
        }
    }
public:
    // Constructor
    Graph(int Num_vertex){
        this->Num_vertex = Num_vertex;
        this->Num_edges = 0;
        this->adjlist.resize(Num_vertex);
        this->checklist.resize(Num_vertex);
    }
    // Add edge
    void Add_Edge(int vertexA, int vertexB)
    {
        if ((vertexA > Num_vertex - 1) || (vertexB > Num_vertex - 1))
        {
            printf("The Number of vertex is %d. You should make edge where its vertex is smaller than the %d.\n", Num_vertex, Num_vertex - 1);
            return;
        }
        else
        {
            for (int elem: adjlist[vertexA]){
                if (elem == vertexB)
                {
                    printf("The edge linked by vertex %d and vertex %d is already defined.\n", vertexA, vertexB);
                    return;
                }
            }
            adjlist[vertexA].push_back(vertexB);
            adjlist[vertexB].push_back(vertexA);
            this->Num_edges++;
        }
    }
    // Show Information
    void Show_Graph()
    {
        printf("\nThis is adjacent list of the following graph.\n");
        for(int idxV = 0; idxV < adjlist.size(); idxV++)
        {
            printf("%d: ",idxV);
            for (int elem:adjlist[idxV])
            {
                printf("%d ",elem);
            }
            printf("\n");
        }
    }
    // search by bfs
    void bfs(int beginV)
    {
        this->InitChecklist();
        queue<int> myQ;
        myQ.push(beginV);
        checklist[beginV] = 1;
        printf("\nSearch by bfs, starting from vertex %d.\n",beginV);
        while(!myQ.empty())
        {
            int current = myQ.front();
            printf("%d ", current);
            myQ.pop();
            for (int idxV:adjlist[current])
            {
                if (checklist[idxV] == 0)
                {
                    myQ.push(idxV);
                    checklist[idxV] = 1;
                }
            }
        }
        printf("\nbfs done.\n");
    }
    // search by dfs (using stack frame(recursive function))
    void dfs_recursion(int beginV)
    {
        this->InitChecklist();
        printf("\nSearch by dfs(using recursive function), starting from vertex %d.\n",beginV);
        checklist[beginV] = 1;
        printf("%d ",beginV);
        dfs(beginV);
        printf("\ndfs done.\n");
    }
    // serach by dfs (using stack container)
    void dfs_stack(int beginV)
    {
        this->InitChecklist();
        printf("\nSearch by dfs(using stack container), starting from vertex %d.\n",beginV);
        stack<int> mystack;
        int current = beginV;
        mystack.push(current);
        checklist[current] = 1;
        while(!mystack.empty())
        {
            current = mystack.top();
            printf("%d ",current);
            vector<int>::reverse_iterator rit = adjlist[current].rbegin();
            mystack.pop();
            for(;rit!=adjlist[current].rend();++rit)
            {
                if (checklist[*rit] == 0)
                {
                    checklist[*rit] = 1;
                    mystack.push(*rit);
                }
            }
        }
        printf("\ndfs done.\n");
    }
    // Initialize Check list
    void InitChecklist()
    {
        for (int idxV=0; idxV < Num_vertex; idxV++)
        {
            checklist[idxV] = 0;
        }
    }
};

int main()
{
    Graph MyGraph(6);
    MyGraph.Add_Edge(1,0);
    MyGraph.Add_Edge(0,3);
    MyGraph.Add_Edge(3,4);
    MyGraph.Add_Edge(4,2);
    MyGraph.Add_Edge(2,5);
    MyGraph.Show_Graph();
    MyGraph.bfs(3);
    MyGraph.dfs_recursion(3);
    MyGraph.dfs_stack(3);
    return 0;
}