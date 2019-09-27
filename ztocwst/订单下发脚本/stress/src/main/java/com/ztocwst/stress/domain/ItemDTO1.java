package com.ztocwst.stress.domain;

import java.util.Random;

/**
 * @version v1.0
 * @program: stress
 * @description:
 * @author: mulan
 * @create: 2019-07-01 11:08
 **/
public class ItemDTO1 {

    private String itemString;

    private String[] itemCode;

    private Integer number;


    private String[] itemName={"E 300H-2 单换气(后壳米白) 氧化银 300*300","E-JC-60BLHF 08 吹风+PTC+换气+照明+显示五合一(后壳灰色) 氧化银 300*600","D0033-D/14W/3000K(黑色)","D0005-X/36W/TR(白色)","D0041-X/24W/TR(原木色)"};

    public ItemDTO1(Integer number,String[] itemCode) {
        this.number = number;
        this.itemCode = itemCode;
    }

    public String getItemString() {
        int num = 0;
        if(number == 1){
            num = new Random().nextInt(5)+5;
        }else if(number == 2){
            num = (int) (Math.random() * 5 + 1);
        }else{
            num = new Random().nextInt(4)+1;
        }
        StringBuffer sb = new StringBuffer();
        for (int i =0; i<num; i++) {
            int a = new Random().nextInt(itemCode.length);
                    sb.append( " <orderLine>\n" +
                    "      <actualPrice>86.0</actualPrice>\n" +
                    "      <discountPrice>0.0</discountPrice>\n" +
                    "      <inventoryType>ZP</inventoryType>\n" +
                    "      <itemCode>"+itemCode[a]+"</itemCode>\n" +
                    "      <itemId/>\n" +
                    "      <itemName>三生花 舒漾细肤沁透保湿喷雾70ml</itemName>\n" +
                    "      <orderLineNo>5</orderLineNo>\n" +
                    "      <ownerCode>CS0758</ownerCode>\n" +
                    "      <planQty>"+(int) (Math.random() * 3 + 1)+"</planQty>\n" +
                    "      <produceCode>BMMBMM005</produceCode>\n" +
                    "      <retailPrice>43.0</retailPrice>\n" +
                    "      <sourceOrderCode>307286412821847607</sourceOrderCode>\n" +
                    "    </orderLine>");
        }

        return sb.toString();
    }



    public void setItemString(String itemString) {
        this.itemString = itemString;
    }


    public static void main(String[] args) {
        System.out.println(Math.random());
    }
}
