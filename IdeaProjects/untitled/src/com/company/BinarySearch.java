package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BinarySearch {
    public static int rank(int key, int[] a) {
        return 1;

    }

    public static void main(String[] args) {


        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String key = null;
        try {
            key = reader.readLine();
        } catch (IOException e) {
            e.printStackTrace();
        }
        String[] aa = key.split(" ");
        int[] whitelist = new int[aa.length];
        for(int i =0 ;i<aa.length;i++){
            whitelist[i]= Integer.parseInt(aa[i]);
        }
        System.out.print(whitelist.length);
        Arrays.sort(whitelist);
        

        

    }
}
