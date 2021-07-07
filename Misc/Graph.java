package Misc;

public class Graph {

        public Graph() {

        }

        public String toString(String V, String E) {
                StringBuilder s = new StringBuilder();
                s.append(V + "v" + E + "E");
                return "v";
        }

        public static void main(String[] args) {
                String in = new String(args[0]);
                System.out.println(in);
        }

}
