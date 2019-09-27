package com.ztocwst.stress.util;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;

public class Test003 {

    public String[] readTxtFile(String name) {
        try {
            List<String> itemName = new ArrayList<>();
            String encoding = "GBK";
            File file = new File(this.getClass().getClassLoader().getResource(name).getPath());
            if (file.isFile() && file.exists()) { //判断文件是否存在
                InputStreamReader read = new InputStreamReader(
                        new FileInputStream(file), encoding);//考虑到编码格式
                BufferedReader bufferedReader = new BufferedReader(read);
                String lineTxt = null;
                while ((lineTxt = bufferedReader.readLine()) != null) {
                    itemName.add(lineTxt);
                }
                read.close();
                String[] codes = itemName.toArray(new String[itemName.size()]);
                return codes;
            } else {
                System.out.println("找不到指定的文件");
            }
        } catch (Exception e) {
            System.out.println("读取文件内容出错");
            e.printStackTrace();
        }
        return null;
    }


    public static void main(String[] args) throws ParseException {
      //  String[] strings = new Test003().readTxtFile("sku_BJSL001.txt");
   //     int a = new Random().nextInt(strings.length);
      //  System.out.println((int)((Math.random()*9+1)*100000));
      //  System.out.println(System.currentTimeMillis());
        String  a =   Calendar.getInstance().getTimeInMillis() + "" +  ((long)(Math.random()*(99999l - 10000l)) + 10000l) + "";
        System.out.println(a.length());

     //   System.out.println(b);

//        SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
//        String dateStr = format.format(new Date());
//        System.out.println(dateStr);
//        format.setTimeZone(TimeZone.getTimeZone("GMT+0"));
//        Date date = format.parse(dateStr);
//        format.setTimeZone(TimeZone.getTimeZone("GMT+2"));
//        String dateStrs = format.format(date);
//        System.out.println(dateStrs);
//        String a = "2019-08-29 19:16:40";
//        String b = "2019-08-29 19:16:40";
//        System.out.println(a.equals(b));

    }
}
