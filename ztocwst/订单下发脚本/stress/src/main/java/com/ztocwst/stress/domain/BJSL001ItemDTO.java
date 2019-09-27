package com.ztocwst.stress.domain;

import java.util.Random;

/**
 * @version v1.0
 * @program: stress
 * @description:
 * @author: mulan
 * @create: 2019-07-01 11:08
 **/
public class BJSL001ItemDTO {

    private String itemString;

    private String[] itemCode;

    private String[] itemName={"短袖T恤","速干长袖","袜子","北京森林户外防水登山鞋反毛牛皮透气耐磨徒步鞋减震防滑登山女鞋","速干T恤"};

    public BJSL001ItemDTO(String[] itemCode) {
        this.itemCode = itemCode;
    }

    public String getItemString() {
        int num = (int) (Math.random() * 5 + 1);
        StringBuffer sb = new StringBuffer();
        for (int i =0;i<num;i++) {
            int a = new Random().nextInt(itemCode.length);
          //  System.out.println(a + "===" + itemCode[a]);
            sb.append( " <orderLine>\n" +
                    "      <actualPrice>86.0</actualPrice>\n" +
                    "      <discountPrice>0.0</discountPrice>\n" +
                    "      <inventoryType>ZP</inventoryType>\n" +
                    "      <itemCode>"+itemCode[a]+"</itemCode>\n" +
                    "      <itemId/>\n" +
                    "      <itemName>"+itemName[0]+"</itemName>\n" +
                    "      <orderLineNo>"+(i+1)+"</orderLineNo>\n" +
                    "      <ownerCode>BJSL001</ownerCode>\n" +
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
