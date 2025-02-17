package com.ztocwst.stress.util;

import java.io.*;
import java.text.SimpleDateFormat;
import java.util.*;
import java.util.concurrent.*;

public class CallableDemo3 {

    final static SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");

    public static void main(String[] args) {
        CountDownLatch latch = new CountDownLatch(1);
        ExecutorService pool = Executors.newFixedThreadPool(10);
        BlockingQueue<Future<Map<String, FileInputStream>>> queue =
                new ArrayBlockingQueue<Future<Map<String, FileInputStream>>>(100);

        System.out.println("-------------文件读、写任务开始时间：" + sdf.format(new Date()));
        File file = new File("D:/ztocwst/stress/src/main/resources/run_flag_2019-08-08.txt");
        Future<Map<String, FileInputStream>> future = pool.submit(new MyCallableProducer(latch, file));
        queue.add(future);

        pool.execute(new MyCallableConsumer(queue));

        try {
            latch.await();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("-------------文件读、写任务结束时间：" + sdf.format(new Date()));
        pool.shutdownNow();
    }


    // 文件读线程
    static class MyCallableProducer implements Callable<Map<String, FileInputStream>>
    {
        private CountDownLatch latch;
        private File file;
        private FileInputStream fis = null;
        private Map<String, FileInputStream> fileMap = new HashMap<String, FileInputStream>();

        public MyCallableProducer(CountDownLatch latch, File file) {
            this.latch = latch;
            this.file = file;
        }

        @Override
        public Map<String, FileInputStream> call() throws Exception
        {
            System.out.println(Thread.currentThread().getName() + " 线程开始读取文件 ：" + file.getName() + " ,时间为 "+ sdf.format(new Date()));
            fis = new FileInputStream(file);
            fileMap.put(file.getName(), fis);
            doWork();
            System.out.println(Thread.currentThread().getName() + " 线程读取文件 ：" + file.getName() + " 完毕"  + " ,时间为 "+ sdf.format(new Date()));
            latch.countDown();
            return fileMap;
        }

        private void doWork() {
            //此方法可以添加一些业务逻辑，比如包装pojo等等操作，返回的值可以是任何类型
            Random rand = new Random();
            int time = rand.nextInt(10) * 1000;
            try {
                Thread.sleep(time);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }


    // 文件写线程
    static class MyCallableConsumer implements Runnable
    {
        private String fileName = "";
        private BlockingQueue<Future<Map<String, FileInputStream>>> queue;
        private FileInputStream fis = null;
        private File dirFile = null;
        private BufferedReader br = null;
        private InputStreamReader isr = null;
        private FileWriter fw = null;
        private BufferedWriter bw = null;

        public MyCallableConsumer(BlockingQueue<Future<Map<String, FileInputStream>>> queue2)
        {
            this.queue = queue2;
        }

        @Override
        public void run()
        {
            try {
                Future<Map<String, FileInputStream>> future = queue.take();
                Map<String, FileInputStream> map = future.get();

                Set<String> set = map.keySet();
                for (Iterator<String> iter = set.iterator(); iter.hasNext();) {
                    fileName = iter.next().toString();
                    fis = map.get(fileName);
                    System.out.println(Thread.currentThread().getName() + " 线程开始写文件 ：" + fileName  + " ,时间为 "+ sdf.format(new Date()));
                    try {
                        isr = new InputStreamReader(fis, "utf-8");

                        br = new BufferedReader(isr);
                        dirFile = new File("D:/ztocwst/stress/src/main/resources/run.txt");
                        fw = new FileWriter(dirFile);
                        bw = new BufferedWriter(fw);
                        String data = "";
                        while ((data = br.readLine()) != null) {
                           // !data.contains("=======run========") && !data.contains("<response><flag>success</flag><code>200</code><message>Success</message></response>")
                            if(data.contains("=======run========")) {
                                bw.write(data + "\r");
                            }

                        }
                    } catch (FileNotFoundException e) {
                        e.printStackTrace();
                    } catch (IOException e) {
                        e.printStackTrace();
                    } finally {
                        try {
                            bw.close();
                            br.close();
                        } catch (IOException e) {
                            e.printStackTrace();
                        }
                    }
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            } catch (ExecutionException e) {
                e.printStackTrace();
            }
        }
    }

}