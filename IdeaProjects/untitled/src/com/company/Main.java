package com.company;


import edu.princeton.cs.algs4.StdDraw;
import edu.princeton.cs.algs4.StdRandom;

import java.sql.Array;
import java.util.Arrays;


public class Main {

    public static void main(String[] args) {
        System.out.print("hello\n");
        System.out.print(sqrt(56874));
        drawRandom();
        //StdDraw.circle(0.1,0.3,0.3);
        //StdDraw.line(0.1,0.2,0.5,0.6);
	// write your code here
    }
    public static double sqrt(double c)
    {
        if (c < 0) return Double.NaN;
        double err = 1e-15;
        double t = c;
        while (Math.abs(t - c/t) > err * t)
            t = (c/t + t) / 2.0;
        return t;

    }
    public static void drawRandom(){
        int N = 50;
        double[] a = new double[N];
        for (int i = 0; i < N; i++)
            a[i] = StdRandom.random();
        Arrays.sort(a);
        for (int i = 0; i < N; i++)
        {
            double x = 1.0*i/N;
            double y = a[i]/2.0;
            double rw = 0.5/N;
            double rh = a[i]/2.0;
            StdDraw.filledRectangle(x, y, rw, rh);
        }
    }
}
