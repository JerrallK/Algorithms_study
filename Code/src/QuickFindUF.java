public class QuickFindUF{
    private int[] id;
    public QuickFindUF(int N) {
        id=new int[N];
        for (int i=0;i<N;i++){
            id[i]=i;
        }
    }
    public boolean connected(int p,int q){
        return id[p]==id[q];
    }
    public void union(int p,int q){
        int pid=id[p];
        int qid=id[q];
        for (int i =0;i<id.length;i++){
            if (id[i]==pid){
                id[i]=qid;
            }
        }
    }

    public static void main(String args[]){
        QuickFindUF Q =new QuickFindUF(10);
        Q.union(1,2);
        System.out.print(Q.connected(1,2));
        for (int i=0;i<Q.id.length;i++){
            System.out.print(Q.id[i]);
        }



    }
}