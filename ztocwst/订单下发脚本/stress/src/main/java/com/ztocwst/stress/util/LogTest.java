package com.ztocwst.stress.util;

import com.ztocwst.stress.task.SendTask;
import com.ztocwst.stress.task.SendTask1;
import com.ztocwst.stress.task.SendTask2;
import com.ztocwst.stress.task.StartMain;

import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class LogTest {

    public static void main(String[] args) {

        boolean flag = true;
        String[] bjslcode = new SkuBjslItemCode().readTxtFile("sku_BJSL001.txt");
        String[] lszmcode = new SkuBjslItemCode().readTxtFile("itemCode.txt");
        String[] lszmcode2 = new SkuBjslItemCode().readTxtFile("itemCode2.txt");

        ExecutorService exec = Executors.newFixedThreadPool(20);

        int count250 = 0;
        int count150 = 0;
        int count100 = 0;
        double a = 125 * 10000;
        double b = 825 * 1000;
        double c = 25  * 10000;
        while (flag) {
            int num = (int) (Math.random() * 3 + 1);
            //250万
//            if (count250 * 300  <= a) {
//                for (int i = 0; i < 300; i++) {
//                    exec.execute(new SendTask(i, bjslcode, lszmcode));
//                }
//                count250++;
//            }

//            //150万
            if (count150 * 300  <= b) {
                for (int i = 0; i < 300; i++) {
                    if(num == 1 && b * 0.1 > count150 * 300){
                        //10%
                        exec.execute(new SendTask1(1,i, bjslcode, lszmcode2));
                    }
                    if(num == 2 && b * 0.33 > count150){
                        //30%
                        exec.execute(new SendTask1(2,i, bjslcode, lszmcode2));
                    }else{
                        //50%
                        exec.execute(new SendTask1(3,i, bjslcode, lszmcode2));
                    }

                }
                count150++;
            }

            //100万
//            if (count100 * 300  <= c) {
//                for (int i = 0; i < 300; i++) {
//                    if(num == 1 && c * 0.1 > count100 * 300){
//                        //10%
//                        exec.execute(new SendTask2(1,i, bjslcode, lszmcode2));
//                    }
//                    if(num == 2 && c * 0.33 > count150){
//                        //30%
//                        exec.execute(new SendTask2(2,i, bjslcode, lszmcode2));
//                    }else{
//                        //50%
//                        exec.execute(new SendTask2(3,i, bjslcode, lszmcode2));
//                    }
//                }
//                count100++;
//            }


//            if ((count250 + count150 + count100) == 1500000) {
//                exec.shutdown();
//                System.exit(0);
//            }


            try {
                Thread.sleep(200L);
            } catch (InterruptedException e) {

            }
        }

    }
}


