public String toString(){
        StringBuilder s=new StringBuilder();
        s.append(V+"v"+E+"E"+NEWLINE);
        }


public static void main(String[]args){
        In in=new In(args[0]);
        Graph G=new Graph(in);
        StdOut.println(G);
        }
