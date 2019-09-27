package com.ztocwst.stress.util;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class SkuBjslItemCode {

    public  String[] readTxtFile(String name){
        try {
            List<String> itemName = new ArrayList<>();
            String encoding="GBK";
            File file=new File(this.getClass().getClassLoader().getResource(name).getPath());
            if(file.isFile() && file.exists()){ //判断文件是否存在
                InputStreamReader read = new InputStreamReader(
                        new FileInputStream(file),encoding);//考虑到编码格式
                BufferedReader bufferedReader = new BufferedReader(read);
                String lineTxt = null;
                while((lineTxt = bufferedReader.readLine()) != null){
                    itemName.add(lineTxt);
                }
                read.close();
                String[] codes = itemName.toArray(new String[itemName.size()]);
                return codes;
            }else{
                System.out.println("找不到指定的文件");
            }
        } catch (Exception e) {
            System.out.println("读取文件内容出错");
            e.printStackTrace();
        }
        return null;
    }
}
